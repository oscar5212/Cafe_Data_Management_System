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
      print(f"Reduced Products List\n{prodcuts_list}".lstrip().strip("{}[").replace(",", "\n").replace("]", "\n"))
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
load_products_file() # Loading Product File
load_couriers_file() # Loading Couriers File
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
        exit
    if main_option == "1":  # Enter Product Menu
        while keep_looping == True:
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

    if main_option == "2": # Enter Couriers Menu
        while keep_looping == True:
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
                






# print(str(couriers_list).strip("[").replace("]", "\n").replace(",", "\n"))