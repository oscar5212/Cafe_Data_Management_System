import csv

prodcuts_list =[]
def load_products_file():
    with open("products.csv", "r+") as csv_products:
        prodcuts_file = csv.DictReader(csv_products)
        for product in prodcuts_file:
            prodcuts_list.append(product)


couriers_list = []
def load_couriers_file():
    with open("couriers.csv", "r+") as csv_cuoriers:
        couriers_file = csv.DictReader(csv_cuoriers)
        for courier in couriers_file:
            couriers_list.append(courier)

orders_list = []
def load_orders_file():
    with open("orders.csv", "r+") as csv_orders:
        orders_file = csv.DictReader(csv_orders)
        for order in orders_file:
            orders_list.append(order)

def main_menu():              # Main Menu
    print("===Baking Cafe===")
    print("==================")
    print("=1) Products Menu=")
    print("=2) Couriers Menu=")
    print("=3) Orders Menu===")
    print("=0) Exit==========")
    print("==================")

def product_menu():            # Main Menu
    print("=====Products Menu====")
    print("======================")
    print("==1) Products List====")
    print("==2) Add Products=====")
    print("==3) Update Products==")
    print("==4) Delete Products==")
    print("=0) Back to Main Menu=")
    print("======================")

def update_product(): # Updating Product List
    print("Products:")
    for index, product in enumerate(prodcuts_list):
        print("Order ID :", index, "\n", str(product).replace("{", " ").replace("}", " ").replace(",", "\n").replace('"', ' ').replace("'", " "),"\n********")
        product_index = int(input("Enter order index to update: "))
        if product_index < len(prodcuts_list):
            for key in prodcuts_list[product_index]:
                new_value = input(f"Enter new {key} (press enter to keep current value): ")
                if new_value != "":
                    prodcuts_list[product_index][key] = new_value
                    print("Products updated successfully.")
                    print("Updated Product\n" + str(prodcuts_list).replace("{", " ").replace("}", " ").replace(",", "\n").replace('"', ' ').replace("'", " ").replace("[", "\n").replace("]", "\n********"))

def del_product():  # Deleting Product
    print("Products:")
    ori_products_list = ['Index {}: {}\n'.strip('[]"').format(p, product) for p, product in enumerate(prodcuts_list)]
    print(ori_products_list)
    products_index = int(input("Which needs to be deleted? Please Enter Index! "))
    if products_index < len(ori_products_list):
      del prodcuts_list[products_index]
      print(f"Reduced Products List\n{prodcuts_list}".lstrip("{}[").replace(",", "\n").replace("]", "\n"))
    else:
      print("Please Enter Correct Index Value! ")
def courier_menu():            # Main Menu
    print("Couriers Menu")
    print("========================")
    print("====1) Couriers List====")
    print("=====2) Add Couriers====")
    print("=====3) Update List=====")
    print("===4) Delete Couriers===")
    print("==0) Back to Main Menu==")
    print("========================")

def update_couriers(): # Updating Product List
    print("Couriers:")
    for index, courier in enumerate(couriers_list):
        print("Courier ID :", index, "\n", str(courier).lstrip('{}"').replace(",", "\n").replace("'", " "),"\n********")
        courier_index = int(input("Enter order index to update: "))
        if courier_index < len(couriers_list):
            for key in couriers_list[courier_index]:
                new_value = input(f"Enter new {key} (press enter to keep current value): ")
                if new_value != "":
                    couriers_list[courier_index][key] = new_value
                    print("Couriers updated successfully.")
                    print("Updated Courier\n" + str(couriers_list).lstrip('{}"').replace(",", "\n").replace("[", "\n").replace("]", "\n********"))

def del_courier():  # Deleting Couriers
    print("Couriers:")
    ori_couriers_list = ['Index {}: {}\n'.strip('[]"').format(c, courier) for c, courier in enumerate(couriers_list)]
    print(ori_couriers_list)
    couriers_index = int(input("Which needs to be deleted? Please Enter Index! "))
    if couriers_index < len(ori_couriers_list):
      del couriers_list[couriers_index]
      print(f"Updated Couriers List\n{couriers_list}".lstrip("{}[").replace(",", "\n").replace("]", "\n"))
    else:
      print("Please Enter Correct Index Value! ")


def order_menu():             # Main Menu
    print("=====Orders Menu====")
    print("======================")
    print("==1) Orders List====")
    print("==2) Add Orders=====")
    print("==3) Update Status==")
    print("==4) Update Orders")
    print("==5) Delete Products==")
    print("=0) Back to Main Menu=")
    print("======================")

# Start of Baker Cafe Terminal

load_products_file() # Loading Product File
load_couriers_file() # Loading Couriers File
load_orders_file()   # Loading Orders File
keep_looping = True
while keep_looping == True:
    main_menu()    # calling Main Menu
    main_option = input("What are you going to do? ")


    if main_option == "0": # Storing all the Orders, Products, and Couriers
        with open("couriers.csv", "w+") as new_couriers_csv:   # overwriting couriers file
            fieldnames_c = ["name", "phone"]
            writer_c = csv.DictWriter(new_couriers_csv, fieldnames=fieldnames_c)

            writer_c.writeheader()
            writer_c.writerows({
                "name": "John",
                "phone": "077774466746",
            })

        with open("prodcuts.csv", "w+") as new_products_csv:    # writing products file
            fieldnames_p = ["name", "price"]
            writer_p = csv.DictWriter(new_products_csv, fieldnames=fieldnames_p)

            writer_p.writeheader()
            writer_p.writerows({
                "name": "Bacon Roll",
                "price": "1.3",
            })

        with open("orders.csv", "w+") as new_orders_csv:    # writing orders file
            fieldnames_o = ["customer_name", "customer_address", "customer_phone", "courier", "status", "items"]
            writer_o = csv.DictWriter(new_orders_csv, fieldnames=fieldnames_o)

            writer_o.writeheader()
            writer_o.writerows({
                "customer_name": "John",
                "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
                "customer_phone": "0789887334",
                "courier": 2,
                "status": "preparing",
                "items": "1, 3, 4"
            })
        exit
    if main_option == "1":  # Enter Product Menu
        while True:
            product_menu()
            products_option = input("Please Enter Number for Corresponding Actions! ")
            if products_option == "0":  # Back to Main Menu
                break
            elif products_option == "1":  # Looking for Available Products
                print(str(prodcuts_list).strip("[").replace("]", "\n").replace(",", "\n"))
            elif products_option == "2":  # Adding New Products with Price
                new_product = input("New Product")
                new_price = input("Price")
                new_products_dict = {
                    "name": new_product,
                    "price": new_price
                }
                prodcuts_list.append(new_products_dict)
                print(str(prodcuts_list).strip("[").replace("]", "\n").replace(",", "\n"))
            elif products_option == "3": # Update products list
                update_product()
                print(str(prodcuts_list).lstrip("[").replace("]", "\n").replace(",", "\n"))
            elif products_option == "4": # Delete Products
                del_product()


    elif main_option == "2": # Enter Couriers Menu
        while True:
            courier_menu()
            couriers_option = input("Please Enter Number for Corresponding Actions! ")
            if couriers_option == "0":  # Back to Main Menu
                break
            elif couriers_option == "1":  # Looking for Available Couriers
                print(str(couriers_list).strip("[").replace("]", "\n").replace(",", "\n"))
            elif couriers_option == "2":  # Adding New Products with Price
                new_courier = input("New Courier ")
                new_phone = input("New Phone ")
                new_couriers_dict = {
                    "name": new_courier,
                    "phone": new_phone
                }
                couriers_list.append(new_couriers_dict)
                print(str(couriers_list).strip("[").replace("]", "\n").replace(",", "\n"))
            elif couriers_option == "3":  # Updating Couriers List
                update_couriers()
            elif couriers_option == "4":  # Deleting Couriers from List
                del_courier()


    elif main_option == "3":       # getting into order menu
        while True:
            order_menu()
            orders_option = input("Please Enter Number for Corresponding Actions! ")
            if orders_option == "0":  # Back to Main Menu
                break
            elif orders_option == "1":  # List all the existed orders
                print(str(orders_list).strip("[{}").replace("]", "\n").replace(",", "\n"))
            elif orders_option == "2":   # Add new orders
                new_customer_name = input("Please Enter Your Name. ")
                new_customer_address = input("Please Enter Your Address. ")
                new_customer_phoner = input("Please Enter Your Phone Number.")
                print("Products:")
                ori_products_list = ['Index {}: {}\n'.strip('[]"').format(p, product) for p, product in enumerate(ori_products_list)]
                print(ori_products_list)
                new_item = input("Please Entre ID of Your Items. (with comma separating each item)")
                ori_couriers_list = ['Index {}: {}\n'.strip('[]"').format(c, courier) for c, courier in enumerate(couriers_list)]
                print(ori_couriers_list)
                new_courier = int(input(""))