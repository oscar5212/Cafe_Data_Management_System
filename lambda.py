import logging
import boto3
import pandas as pd
import hashlib
import psycopg2
from io import StringIO

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def generate_pseudo_random_id(value):
    return hashlib.md5(str(value).encode()).hexdigest()

ssm_client = boto3.client('ssm')

# Get the SSM Param from AWS and turn it into JSON
# Don't log the password!
def get_ssm_param(param_name):
    print(f'get_ssm_param: getting param_name={param_name}')
    parameter_details = ssm_client.get_parameter(Name=param_name)
    redshift_details = json.loads(parameter_details['Parameter']['Value'])

    host = redshift_details['redshiftcluster-h0ppssmszukx.cyedtoskxrzl.eu-west-1.redshift.amazonaws.com:5439/dev']
    user = redshift_details['user']
    db = redshift_details['database-name']
    print(f'get_ssm_param loaded for db={db}, user={user}, host={host}')
    return redshift_details

    # Create a temporary buffer to upload the DataFrame to Redshift
    buffer = StringIO()
    df.to_csv(buffer, index=False, header=True)
    buffer.seek(0)

    # Copy data from the buffer to the Redshift table
    cursor.copy_from(buffer, redshift_params['table'], sep=',')

    conn.commit()
    cursor.close()
    conn.close()

def index_handler(event, context):
    LOGGER.info(f'Event structure: {event}')

    # Get the S3 bucket and key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    local_file_path = f'/tmp/{key.split("/")[-1]}'  # path needs to be tmp/'filename.csv

    # Use boto3 to download the S3 object to the /tmp directory
    s3 = boto3.client('s3')
    s3.download_file(bucket, key, local_file_path)

    # Use pandas to read the CSV
    df = pd.read_csv(local_file_path)

    # Log the DataFrame head
    LOGGER.info(f'DataFrame Head raw:\n{df.head()}')

    # ETL logic
    def order_price_cleaning(df):
        df['Order'] = df['Order'].str.split(",")
        df = df.explode('Order')
        df[['Product', 'Price']] = df['Order'].str.rsplit('-', n=1, expand=True)

        print("DataFrame Shape Before:", df.shape)
        print("Columns Before:", df.columns)

        df[['Product_Name', 'Flavour']] = df['Product'].str.rsplit('-', n=1, expand=True)

        print("DataFrame Shape After:", df.shape)
        print("Columns After:", df.columns)

        df[['Size','Product']] = df['Product'].str.split(n=1, expand=True)
        return df

    df = order_price_cleaning(df)
    df.drop(['Order'], axis=1, inplace=True)
    df.drop(['CardNumber'], axis=1, inplace=True)

    df['Product_id'] = df.apply(lambda row: generate_pseudo_random_id(str(row['Flavour']) + str(row['Size']) + str(row['Product']) + str(row['Price'])), axis=1)
    df['Customer_id'] = df['Name'].apply(lambda _: generate_pseudo_random_id(_))
    df['Order_id'] = df.apply(lambda row: generate_pseudo_random_id(str(row['DateTime']) + str(row['Location']) + str(row['Name'])), axis=1)
    df['Branch_id'] = df.apply(lambda row: generate_pseudo_random_id(str(row['Location']) + str(row['DateTime'])), axis=1)

    df.drop(['Name'], axis=1, inplace=True)

    transformed_file_path = '/tmp/AWStransformed_data_with_ids.csv'
    df.to_csv(transformed_file_path, index=False)

    # Upload the modified DataFrame back to S3
    transformed_key = key.replace('raw/', 'transformed/')  #  path needs adjusting
    s3.upload_file(transformed_file_path, 'de-x5-lle-marios-test-bucket-2', transformed_key)

    # Log the head again after the transformation
    LOGGER.info(f'DataFrame Head after Transformation:\n{df.head()}')

    # Load the transformed data into Redshift
    redshift_params = {
        'host': '""',
        'port': '5439',
        'user': 'marios_espresso_pipeline_user',
        'password': 'dtFW7wRKfllg',
        'database': 'marios_espresso_pipeline_cafe_db',
        'table': 'your_redshift_table'
    }
    load_data_into_redshift(df, redshift_params)

    LOGGER.info('ETL process completed successfully!')
  