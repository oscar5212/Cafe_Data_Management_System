import pymysql
import db_product
import db_courier
import db_order
import db_customer


def main_menu():              # Main Menu
    print("====Baking Cafe====")
    print("===================")
    print("=1) Products Menu==")
    print("=2) Couriers Menu==")
    print("=3) Orders Menu====")
    print("=4) Customers Menu=")
    print("=0) Exit===========")
    print("===================")

# Start of Baker Cafe Terminal

print('Opening connection...')  # connect to database
conn = pymysql.connect(
host='localhost',
database='baking_cafe',
user='root',
password='password')
cur = conn.DictCursor()
print('Connecting Database Successful! ')

while True:
    main_menu()    # call Main Menu
    main_option = input("What are you going to do? ")

    if main_option == "0": # exit the application
        cur.close()
        break
        exit

    if main_option == "1":  # Enter Product Menu
        db_product.products()   # execute all actions in Product Menu


    elif main_option == "2": # Enter Couriers Menu
        db_courier.couriers()   # execute all actions in Courier Menu


    elif main_option == "3":  # Enter Order Menu
        db_order.orders()   # execute all actions in Order Menu

    elif main_option == "4":  # Enter Customer Menu
        db_customer.customers()  # execute all actions in Cusotmer Menu