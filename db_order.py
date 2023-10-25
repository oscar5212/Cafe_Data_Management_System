import pymysql

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

conn = pymysql.connect(
host='localhost',
database='baking_cafe',
user='root',
password='password')
cur = conn.cursor()

def orders():       # execute all the actions related to order menu
    while True:
        order_menu()
        orders_option = input("Please Enter a Choice! ")
        if orders_option == "0":         # back to main menu
            break
        elif orders_option == "1":       # list all orders
            cur.execute("SELECT * FROM orders")
            orders_list = cur.fetchall()
            for order in orders_list:
                print(order)
        elif orders_option == "2":      # add new orders
            customer_name = input("Enter Customer's Name! ")
            customer_address = input ("Enter Customer Address! ")
            customer_phone = input("Enter Customer Phone Number! ")
            cur.execute("SELECT * FROM products")
            products_list = cur.fetchall()
            for product in products_list:
                print(product)
            items = input("Entre Products' ID! (seperate with comma for more than 1 item)")
            cur.execute("SELECT * FROM couriers")
            couriers_list = cur.fetchall()
            for courier in couriers_list:
                print(courier)
            couriers = int(input("Select Couriers by their ID! "))
            status = 1
            try:
                cur.execute("INSERT INTO orders (customer_name, customer_address, customer_phone, couriers, order_status_id, items ) VALUES (%s, %s, %s, %s, %s, %s)", (customer_name, customer_address, customer_phone, couriers, status, items))
                conn.commit()
                cur.execute("SELECT * FROM orders")
                orders_list = cur.fetchall()
                for order in orders_list:
                    print(order)
            except Exception as e:
                print("Error Found:", e)
        elif orders_option == "3":    # update order status
            cur.execute("SELECT * FROM orders")
            orders_list = cur.fetchall()
            for order in orders_list:
                print(order)
            cur.execute("SELECT * FROM orders_status")
            orders_status_list = cur.fetchall()
            for order_status in orders_status_list:
                print(order_status)
            order_status_id = input("Enter Updated Order Status ID! ")
            order_status = input("Update Order Status! ")
            try:
                cur.execute("UPDATE order_status SET status = %s where id = %s", (order_status, order_status_id))
                conn.commit()
                orders_status_list = cur.fetchall()
                for status in orders_status_list:
                    print(status)
            except Exception as e:
                print("Error Found:", e)
        elif orders_option == "4":   # update orders
            cur.execute("SELECT * FROM orders")
            orders_list = cur.fetchall()
            for order in orders_list:
                print(order)
            order_id = int(input("Enter the id of order to be updated! "))
            customer_name = input("Enter Customer's Name! ")
            customer_address = input ("Enter Customer Address! ")
            customer_phone = input("Enter Customer Phone Number! ")
            cur.execute("SELECT * FROM products")
            products_list = cur.fetchall()
            for product in products_list:
                print(product)
            items = input("Entre Products' ID! (seperate with comma for more than 1 items)")
            cur.execute("SELECT * FROM couriers")
            couriers_list = cur.fetchall()
            for courier in couriers_list:
                print(courier)
            couriers = int(input("Select Couriers by their ID! "))
            if order_id != "":
                cur.execute("UPDATE orders SET (customer_name, customer_address, customer_phone, couriers, items ) VALUES (%s, %s, %s, %s, %s)", (customer_name, customer_address, customer_phone, couriers, items))
                conn.commit()
            elif order_id == "":
                pass
        elif orders_option == "5":   # delete product from product list
            cur.execute("SELECT * FROM orders")
            orders_list = cur.fetchall()
            for order in orders_list:
                print(order)
            order_id = int(input("Enter the id of order to be deleted! "))
            try:
                cur.execute("DELETE FROM orders WHERE id = %s", order_id)
                orders_list = cur.fetchall()
                conn.commit()
                for order in orders_list:
                    print(order)
            except Exception as e:
                print("Error Found:", e)