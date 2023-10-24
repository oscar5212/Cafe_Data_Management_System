import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

while True:
    def db_connection():
        print('Opening connection...')
        conn = pymysql.connect(
        host=host_name,
        database=database_name,
        user=user_name,
        password=user_password)
        cur = conn.cursor()
        orders_option = input("Please Enter a choice! ")
        print(orders_menu)
        if orders_option == "0":         # back to main menu
            conn.close()
            break
        elif orders_option == "1":       # list all orders
            cur.execute("select * from orders")
            orders_list = cur.fetchall()
            for order in orders_list:
                print(order)


        elif orders_option == "2":      # add new products
            customer_name = input("Enter Customer's Name! ")
            customer_address = input ("Enter Customer Address! ")
            customer_phone = input("Enter Customer Phone Number! ")
            cur.execute("select * from products")
            products_list = cur.fetchall()
            for product in products_list:
                print(product)
            items = input("Entre Products' ID! (seperate with comma or more than 1 items)")
            cur.execute("select * from couriers")
            couriers_list = cur.fetchall()
            for courier in couriers_list:
                print(courier)
            couriers = int(input("Select Couriers by their ID! "))
            status = 1
            try:
                cur.execute("INSERT INTO couriers (customer_name, customer_address, customer_phone, couriers, status, items ) VALUES (%s, %s, %s, %s, %s, %s)", (customer_name, customer_address, customer_phone, couriers, status, items))
                conn.commit()
                orders_list = cur.fetchall()
                for order in orders_list:
                    print(order)

            except Exception as e:
                print("Error Found:", e)

        elif orders_option == "3":    # update order status
            cur.execute("select * from orders")
            orders_list = cur.fetchall()
            for order in orders_list:
                print(order)
            order_id = int(input("Enter ID of Couriers!"))
            cur.execute("select * from orders_status")
            orders_status_list = cur.fetchall()
            for order_status in orders_status_list:
                print(order_status)
            order_status_id = input("Enter Updated Order Status ID! ")

            try:
                cur.execute("UPDATE couriers SET name = %s, phone = %s where id = %s", (new_name, new_phone, courier_id))
                conn.commit()
                orders_list = cur.fetchall()
                for order in orders_list:
                    print(order)
            except Exception as e:
                print("Error Found:", e)

        elif orders_option == "5":   # delete product from product list
            orders_list = cur.fetchall()
            for order in orders_list:
                print(order)
            courier_id = int(input("Enter the id of couriers to be deleted! "))
            try:
                cur.execute("DELETE FROM couriers WHERE id = %s", courier_id)
                orders_list = cur.fetchall()
                conn.commit()
                for order in orders_list:
                    print(order)
            except Exception as e:
                print("Error Found:", e)