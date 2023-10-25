import pymysql
from cafeweek6 import product_menu

print('Opening connection...')
conn = pymysql.connect(
host='localhost',
database='baking_cafe',
user='root',
password='password')
cur = conn.cursor()

def products():
    while True:
        product_menu()
        products_option = input("Please Enter a choice! ")
        if products_option == "0":         # back to main menu
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