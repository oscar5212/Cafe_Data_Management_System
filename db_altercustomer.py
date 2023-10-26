import pymysql

conn = pymysql.connect(    # connect to database
host='localhost',
database='baking_cafe',
user='root',
password='password')
cur = conn.cursor()

def alter_info():         # adment customer information
    cur.execute("SELECT * FROM customers")    # list all cusomter info with id
    customers_list = cur.fetchall()
    for customer in customers_list:
        print(customer)
    customer_id = int(input("Choose a ID to update reocrd! "))
    alter_options = input("Which info needs to be updated? ")
    if alter_options == "1":   # update cusomter name
        customer_name =  input("Enter Customer's Name! ")
        cur.execute("UPDATE customers SET customer_name = %s where customer_id = %s", (customer_name, customer_id))
        conn.commit()
    elif alter_options == "2": # update cusotmer address
        customer_address = input("Enter Custoemr's Address! ")
        cur.execute("UPDATE customers SET customer_address = %s where customer_id = %s", (customer_address, customer_id))
        conn.commit()
    elif alter_options == "3":  # update customer phone number
        customer_phone = input("Enter Cusotmer's Phone Number! ")
        cur.execute("UPDATE customers SET customer_phone = %s where customer_id = %s", (customer_phone, customer_id))
        conn.commit()
    elif alter_options == "4":  # update customer membership number
        customer_membership = input("Enter Membership Number! ")
        cur.execute("UPDATE customers SET member_number = %s where customer_id = %s", (customer_membership, customer_id))
        conn.commit()
    cur.execute("SELECT * FROM customers")
    customers_list = cur.fetchall()
    for customer in customers_list:
        print(customer)
