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
        couriers_option = input("Please Enter a choice! ")
        print(couriers_menu)
        if couriers_option == "0":         # back to main menu
            conn.close()
            break
        elif couriers_option == "1":       # list avaialable couriers
            cur.execute("select * from couriers")
            couriers_list = cur.fetchall()
            for courier in couriers_list:
                print(courier)


        elif couriers_option == "2":      # add new products
            new_name = input("Enter New Courier's Name! ")
            new_phone = float(input ("Enter New Phone Number! "))
            try:
                cur.execute("INSERT INTO couriers (name, phone) VALUES (%s, %s)", (new_name, new_phone))
                conn.commit()
                couriers_list = cur.fetchall()
                for courier in couriers_list:
                    print(courier)

            except Exception as e:
                print("Error Found:", e)

        elif couriers_option == "3":    # update products list
            couriers_list = cur.fetchall()
            for courier in couriers_list:
                print(courier)
            courier_id = int(input("Enter ID of Couriers!"))
            new_name = input("Enter New Name of Courier! ")
            new_phone = float(input("Enter New Phone Number! "))
            if  courier_id != "":
                try:
                    cur.execute("UPDATE couriers SET name = %s, phone = %s where id = %s", (new_name, new_phone, courier_id))
                    conn.commit()
                    couriers_list = cur.fetchall()
                    for courier in couriers_list:
                        print(courier)
                except Exception as e:
                    print("Error Found:", e)

        elif couriers_option == "4":   # delete product from product list
            couriers_list = cur.fetchall()
            for courier in couriers_list:
                print(courier)
            courier_id = int(input("Enter the id of couriers to be deleted! "))
            try:
                cur.execute("DELETE FROM couriers WHERE id = %s", courier_id)
                couriers_list = cur.fetchall()
                conn.commit()
                for courier in couriers_list:
                    print(courier)
            except Exception as e:
                print("Error Found:", e)