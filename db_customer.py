import pymysql
import db_altercustomer

def customer_menu():             # order Menu
    print("=====Customers Menu===")
    print("======================")
    print("====1) List Info======")
    print("====2) Add New Info===")
    print("====3) Update Info====")
    print("===4) Delete Info=====")
    print("=0) Back to Main Menu=")
    print("======================")

def alter_menu():
    print("======Data Alteration Menu=====")
    print("===============================")
    print("========1) Customer Name=======")
    print("=======2) Customer Phone=======")
    print("======3) Cusomter Address======")
    print("=====4) Customer Membership====")
    print("===0) Back to Customers Menu===")


conn = pymysql.connect(
host='localhost',
database='baking_cafe',
user='root',
password='password',
cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

def customers():      # execute all the actions of customers
    while True:
        customer_menu()
        customers_option = input("Please Enter a choice! ")
        if customers_option == "0":  # return to main menu
            break
        elif customers_option == "1": # print customer list
            cur.execute("SELECT * FROM customers")
            customers_list = cur.fetchall()
            for customer in customers_list:
                print(str(customer).strip("{").replace("}","\n"))
        elif customers_option == "2":
            customer_name = input("Please Enter Name !")
            customer_address = input ("Please Enter Address! ")
            customer_phone = input("Please Enter Phone Number! ")
            membership_option = input("Are you a member ? Y/N")
            if membership_option == "Y":
                memebr_number = input("Please Entre Your Menemrship Number! ")
                cur.execute("INSERT INTO customers (customer_name, customer_address, customer_phone, member_number) VALUES (%s, %s, %s, %s)", (customer_name, customer_address, customer_phone, memebr_number))
                conn.commit()
            elif membership_option == "N":
                cur.execute("INSERT INTO customers (customer_name, customer_address, customer_phone) VALUES (%s, %s, %s)", (customer_name, customer_address, customer_phone))
                conn.commit()
        elif customers_option == "3": # update customers info
            alter_menu()
            db_altercustomer.alter_info()
        elif customers_option == "3":  # delete opted out customer info
                cur.execute("SELECT * FROM customers")
                customers_list = cur.fetchall()
                for customer in customers_list:
                    print(str(customer).strip("{").replace("}","\n"))
                del_info = int(input("Please Entre ID of Customer"))
                cur.execute("DELETE FROM customers WHERE customer_id = %s", del_info)
                conn.commit()
                cur.execute("SELECT * FROM customers")
                customers_list = cur.fetchall()
                for customer in customers_list:
                    print(str(customer).strip("{").replace("}","\n"))