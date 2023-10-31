import pymysql
import db_orderlist

def order_menu():             # order Menu
    print("=====Orders Menu====")
    print("======================")
    print("===1) Orders List=====")
    print("===2) Add Orders======")
    print("===3) Update Status===")
    print("===4) Update Orders===")
    print("==5) Delete Orderss==")
    print("=0) Back to Main Menu=")
    print("======================")

conn = pymysql.connect(
host='localhost',
database='baking_cafe',
user='root',
password='password',
cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

def orders():       # execute all the actions related to order menu
    while True:
        order_menu()
        orders_option = input("Please Enter a Choice! ")
        if orders_option == "0":         # back to main menu
            break
        elif orders_option == "1":       # list all orders
            db_orderlist.order_list()
        elif orders_option == "2":      # add new orders
            customer_name = input("Enter Customer's Name! ")
            customer_address = input ("Enter Customer Address! ")
            customer_phone = input("Enter Customer Phone Number! ")
            cur.execute("SELECT * FROM products")
            products_list = cur.fetchall()
            for product in products_list:
                print(str(product).strip("{").replace("}","\n"))
            items = input("Entre Products' ID! (seperate with comma for more than 1 item)")
            cur.execute("SELECT * FROM couriers")
            couriers_list = cur.fetchall()
            for courier in couriers_list:
                print(str(courier).strip("{").replace("}","\n"))
            couriers = int(input("Select Couriers by their ID! "))
            status = "preparing"
            cur.execute("INSERT INTO order_status (order_status) VALUES (%s)", (status))
            conn.commit()
            cur.execute("SELECT * FROM order_status")
            order_status_list = cur.fetchall()
            for order_status in order_status_list:
                print(str(order_status).strip("{").replace("}","\n"))
            order_status_id = int(input("Please Entre the last order status id !" ))
            try:
                cur.execute("INSERT INTO orders (customer_name, customer_address, customer_phone, courier, order_status_id, items ) VALUES (%s, %s, %s, %s, %s, %s)", (customer_name, customer_address, customer_phone, couriers, order_status_id, items))
                conn.commit()
                cur.execute("SELECT * FROM orders")
                orders_list = cur.fetchall()
                for order in orders_list:
                    print(str(order).strip("{").replace("}","\n"))
            except Exception as e:
                print("Error Found:", e)
        elif orders_option == "3":    # update order status
            cur.execute("SELECT * FROM orders o JOIN order_status os on o.order_status_id = os.order_status_id ")
            orders_list = cur.fetchall()
            for order in orders_list:
                print(str(order).strip("{").replace("}","\n"))
            order_status_id = int(input("Enter Updated Order Status ID! "))
            print("Order Status Can be: preparing / Ready to be Delivered or Collected / Delivered or Collected! ")
            order_status = input("Update Order Status! ")
            try:
                cur.execute("UPDATE order_status SET order_status = %s where order_status_id = %s", (order_status, order_status_id))
                conn.commit()
                orders_status_list = cur.fetchall()
                for status in orders_status_list:
                    print(str(status).strip("{").replace("}","\n"))
            except Exception as e:
                print("Error Found:", e)
        elif orders_option == "4":   # update orders
            cur.execute("SELECT * FROM orders")
            orders_list = cur.fetchall()
            for order in orders_list:
                print(str(order).strip("{").replace("}","\n"))
            order_id = int(input("Enter the id of order to be updated! "))
            if order_id != "":
                print("1: Name, 2: Address, 3:Phone Number, 4:Items, 5:Courier ")
                update_option = input("Which field to be edited? Please Enter Provided Number! ")
                if update_option == "1":     # # update name
                    customer_name = input("Enter Customer's Name! ")
                    cur.execute("UPDATE orders SET customer_name = %s WHERE id = %s", (customer_name, order_id))
                    conn.commit()
                elif update_option == "2":   # update address
                    customer_address = input ("Enter Customer Address! ")
                    cur.execute("UPDATE orders SET  customer_address = %s WHERE id = %s", (customer_address, order_id))
                    conn.commit()
                elif update_option == "3":   # update phone number
                    customer_phone = input("Enter Customer Phone Number! ")
                    cur.execute("UPDATE orders SET  customer_phone = %s WHERE id = %s", (customer_phone, order_id))
                    conn.commit()
                elif update_option == "4":   # update items
                    cur.execute("SELECT * FROM products")
                    products_list = cur.fetchall()
                    for product in products_list:
                        print(str(product).strip("{").replace("}","\n"))
                    items = input("Entre Products' ID! (seperate with comma for more than 1 items)")
                    cur.execute("UPDATE orders SET  items = %s WHERE id = %s", (items, order_id))
                    conn.commit()
                elif update_option == "5":  # update couriers
                    cur.execute("SELECT * FROM couriers")
                    couriers_list = cur.fetchall()
                    for courier in couriers_list:
                        print(str(courier).strip("{").replace("}","\n"))
                    couriers = int(input("Select Couriers by their ID! "))
                    cur.execute("UPDATE orders SET  courier = %s WHERE id = %s", (couriers, order_id))
                    conn.commit()
            elif order_id == "":
                pass
        elif orders_option == "5":   # delete order from order list
            cur.execute("SELECT * FROM orders")
            orders_list = cur.fetchall()
            for order in orders_list:
                print(str(order).strip("{").replace("}","\n"))
            order_id = int(input("Enter the id of order to be deleted! "))
            try:
                cur.execute("DELETE FROM orders WHERE id = %s", order_id)
                orders_list = cur.fetchall()
                conn.commit()
                for order in orders_list:
                    print(str(order).strip("{").replace("}","\n"))
            except Exception as e:
                print("Error Found:", e)