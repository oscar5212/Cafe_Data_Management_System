import pymysql
import db_product
import db_courier
import db_order


def main_menu():              # Main Menu
    print("===Baking Cafe===")
    print("==================")
    print("=1) Products Menu=")
    print("=2) Couriers Menu=")
    print("=3) Orders Menu===")
    print("=0) Exit==========")
    print("==================")

def product_menu():            # Product Menu
    print("=====Products Menu====")
    print("======================")
    print("==1) Products List====")
    print("==2) Add Products=====")
    print("==3) Update Products==")
    print("==4) Delete Products==")
    print("=0) Back to Main Menu=")
    print("======================")


def courier_menu():            # Courier Menu
    print("Couriers Menu")
    print("========================")
    print("====1) Couriers List====")
    print("=====2) Add Couriers====")
    print("=====3) Update List=====")
    print("===4) Delete Couriers===")
    print("==0) Back to Main Menu==")
    print("========================")




def order_menu():             # order Menu
    print("=====Orders Menu====")
    print("======================")
    print("===1) Orders List=====")
    print("===2) Add Orders======")
    print("===3) Update Status===")
    print("===4) Update Orders===")
    print("==5) Delete Products==")
    print("=0) Back to Main Menu=")
    print("======================")




# Start of Baker Cafe Terminal

print('Opening connection...')  # connect to database
conn = pymysql.connect(
host='localhost',
database='baking_cafe',
user='root',
password='password')
cur = conn.cursor()
print('Connecting Database Successful! ')

while True:
    main_menu()    # call Main Menu
    main_option = input("What are you going to do? ")

    if main_option == "0": # exit the application
        conn.close()
        exit
    if main_option == "1":  # Enter Product Menu
        db_product.products()   # execute all actions in Product Menu


    elif main_option == "2": # Enter Couriers Menu
        db_courier.couriers()   # execute all actions in Courier Menu


    elif main_option == "3":  # Enter Order Menu
        db_order.orders()   # execute all actions in Order Menu