import pymysql

# Establish a connection to the database
conn = pymysql.connect(host='hostname', user='username', password='password', db='database')

# Create a cursor object
cursor = conn.cursor()

def list_products():
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def add_product(product_id, product_name):
    cursor.execute("INSERT INTO products (id, name) VALUES (%s, %s)", (product_id, product_name))
    conn.commit()

def update_product(product_id, product_name):
    cursor.execute("UPDATE products SET name = %s WHERE id = %s", (product_name, product_id))
    conn.commit()

def delete_product(product_id):
    cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
    conn.commit()
