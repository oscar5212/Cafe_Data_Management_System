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
        products_option = input("Please Enter a choice! ")
        print(products_menu)
        if products_option == "0":         # back to main menu
            conn.close()
            break
        elif products_option == "1":       # list avaialable products
            cur.execute("select * from products")
            products_list = cur.fetchall()
            for product in products_list:
                print(product)


        elif products_option == "2":      # add new products
            new_name = input("Enter New Product's Name! ")
            new_price = float(input ("Enter New Price! "))
            try:
                cur.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (new_name, new_price))
                conn.commit()
                products_list = cur.fetchall()
                for product in products_list:
                    print(product)

            except Exception as e:
                print("Error Found:", e)

        elif products_option == "3":    # update products list
            products_list = cur.fetchall()
            for product in products_list:
                print(product)
            product_id = int(input("Enter ID of Respective Products!"))
            new_name = input("Enter New Name of Product! ")
            new_price = float(input("Enter New Price! "))
            if product_id != "":
                try:
                    cur.execute("UPDATE products SET name = %s, price = %s where id = %s", (new_name, new_price, product_id))
                    conn.commit()
                    products_list = cur.fetchall()
                    for product in products_list:
                        print(product)
                except Exception as e:
                    print("Error Found:", e)

        elif products_option == "4":   # delete product from product list
            products_list = cur.fetchall()
            for product in products_list:
                print(product)
            product_id = int(input("Enter the id of item needs to be deleted! "))
            try:
                cur.execute("DELETE FROM products WHERE id = %s", (product_id))
                products_list = cur.fetchall()
                conn.commit()
                for product in products_list:
                    print(product)
            except Exception as e:
                print("Error Found:", e)