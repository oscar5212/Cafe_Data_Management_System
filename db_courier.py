import pymysql

def courier_menu():            # Courier Menu
    print("Couriers Menu")
    print("========================")
    print("====1) Couriers List====")
    print("=====2) Add Couriers====")
    print("=====3) Update List=====")
    print("===4) Delete Couriers===")
    print("==0) Back to Main Menu==")
    print("========================")


conn = pymysql.connect(
host='localhost',
database='baking_cafe',
user='root',
password='password')
cur = conn.cursor()

def couriers():   # run all the actions related to courier menu
    while True:
        courier_menu()
        couriers_option = input("Please Enter a choice! ")
        if couriers_option == "0":         # back to main menu
            break
        elif couriers_option == "1":       # list avaialable couriers
            cur.execute("SELECT * FROM couriers")
            couriers_list = cur.fetchall()
            for courier in couriers_list:
                print(courier)
        elif couriers_option == "2":      # add new products
            new_name = input("Enter New Courier's Name! ")
            new_phone = float(input ("Enter New Phone Number! "))
            try:
                cur.execute("INSERT INTO couriers (name, phone) VALUES (%s, %s)", (new_name, new_phone))
                conn.commit()
                cur.execute("SELECT * FROM couriers")
                couriers_list = cur.fetchall()
                for courier in couriers_list:
                    print(courier)
            except Exception as e:
                print("Error Found:", e)
        elif couriers_option == "3":    # update products list
            cur.execute("SELECT * FROM couriers")
            couriers_list = cur.fetchall()
            for courier in couriers_list:
                print(courier)
            courier_id = int(input("Enter ID of Couriers!"))
            new_name = input("Enter New Name of Courier! ")
            new_phone = (input("Enter New Phone Number! "))
            if  courier_id != "":
                if new_name == "" and new_phone == "":
                    pass
                elif new_phone == "" and new_name != "":
                    cur.execute("UPDATE couriers SET name = %s where id = %s", (new_name, courier_id))
                elif new_phone != "" and new_name == "":
                    cur.execute("UPDATE couriers SET phone = %s where id = %s", (new_phone, courier_id))
                try:
                    cur.execute("UPDATE couriers SET name = %s, phone = %s where id = %s", (new_name, new_phone, courier_id))
                    conn.commit()
                    cur.execute("SELECT * FROM couriers")
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