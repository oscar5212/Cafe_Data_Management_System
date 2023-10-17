
prodcuts = []                               # stores items for sales
products_file = open('generation_mini_project/products.txt', 'r+') # Load products lsit
products_doc= products_file.readlines()
for product in products_doc:
  prodcuts.append(product.strip('\n'))

couriers_list = []                               # stores items for sales
couriers_file = open('generation_mini_project/delivery.txt', 'r+') # Load products lsit
for couriers_name in couriers_file.readlines():
  couriers_list.append(couriers_name.strip('\n'))
products_menu=("""
      Baking Cafe Product Menu
    ===========================
    1. Products
    2. Add New Products
    3. Update Products
    4. Delete Products
    0. Back to Main Menu""") # Layout of Products Menu
couriers_menu =("""
       Baking Cafe Couriers Menu
    =============================
    1. Couriers
    2. Add New Couriers
    3. Update Couriers
    4. Delete Couriers
    0. Back to Main Menu""") # Layout of Couriers Menu
orders_menu = ("""
        Baking Cafe Orders Menu
        ======================
        1. Order Record
        2. Start New Orders
        3. Update Orders Status
        4. Update Orders Details
        5. Delete Orders
        0. Back to Main Menu""") # Layout of Orders Menu
order = {'Customer_name':'Ben Conor',
         'Customer_address':'077438379',
         'Customer_phone': 'Unit 2, 12 Main Street, LONDON, WH1 2ER',
         'Courier' : 2,
         'Status': 'Preparaing'}  # dictionary of order
order_list = [] # lsit of orders
status_list = [] # list of order status

keep_looping = True
while keep_looping == True: # main manu
  print("""
        Baking Cafe Main Menu
        ======================
        1. Products Menu
        2. Couriers Menu
        3. Orders Menu
        0. Exit""")
  menu_option = input('Which menu?')

  if menu_option == '0':       #  save lists to txt files
    for product in prodcuts:
        products_file.write("\n" + product + "\n")
    products_file.close()
    for couriers_name in couriers_list:
        couriers_file.write("\n" + couriers_name + "\n")
    couriers_file.close()
    break

  elif menu_option == '1':              # products manu
    while keep_looping == True:
      print(products_menu)
      product_choice = input('What are you going to do? ')

      if product_choice == '1':   # identifies Products in 1
        for p in prodcuts:
          print(f'Products: {p}')

      elif product_choice == '2': #add new products
          option_2 = input ('Please enter a product name! ')
          print(option_2)
          prodcuts.append(option_2)
          print(prodcuts)

      elif product_choice == '3': #update existing products
          products_list = ['{}: {}'.format(p, product) for p, product in enumerate(prodcuts)]
          print(products_list)
          index_product = input ('Please Enter the index of Prodcuts! ')
          update_pro_name = input ('Please Update the name of Prodoucts! ')
          index_item = int(index_product)
          if index_item < len(prodcuts):
            prodcuts[index_item] = update_pro_name
            print(prodcuts)
          elif index_item >= len(prodcuts):
            print(f"Invalid index detected! Please enter index! ")

      elif product_choice == '4': # delete existing products
          products_list = ['{}: {}'.format(p, product) for p, product in enumerate(prodcuts)]
          print(products_list)
          index_product = input ('Please Enter the index of Prodcuts! ')
          index_item = int(index_product)
          if index_item < len(prodcuts):
            del prodcuts[index_item]
            print(prodcuts)
          else:
            print("Please insert a correct index of products! ")

      elif product_choice == '0': # exit product manu
          break

  elif menu_option == '2':
      while keep_looping == True:
          print(couriers_menu)
          couriers_choice = input("Anything Related to Couriers ? ")

          if couriers_choice == '0': # back to Main Menu
            break

          elif couriers_choice == '1': # print couriers list
                print(f"Couriers List\n{couriers_list}".lstrip())

          elif couriers_choice == '2':  # add new couriers
            courier_name = input("Please Enter Couriers Name! ")
            couriers_list.append(courier_name)
            print(f"New Couriers List\n{couriers_list}".lstrip())

          elif couriers_choice == '3': # update existed couriers
            ori_couriers_list = ['{}: {}'.format(c, courier) for c, courier in enumerate(couriers_list)]
            print(ori_couriers_list)
            courier_index = int(input("Please Enter the index of Couriers! "))
            new_name = input("Please Type New Courier Name ! ")
            if courier_index < len(ori_couriers_list):
              couriers_list[courier_index] = new_name
              print(f"Updated Couriers List\n{couriers_list}".lstrip())
            else:
              print("Please Enter Corect Index! ")

          elif couriers_choice == '4' : # delete couriers
            ori_couriers_list = ['{}: {}'.format(c, courier) for c, courier in enumerate(couriers_list)]
            print(ori_couriers_list)
            courier_index = int(input("Who need to be deleted? Please Enter Index! "))
            if courier_index < len(ori_couriers_list):
              del couriers_list[courier_index]
              print(f"Reduced Couriers List\n{couriers_list}".lstrip())
            else:
              print("Please Enter Correct Index Value! ")

  elif menu_option == '3':  # enter orders manu
        while keep_looping == True:
            print(orders_menu)
            order_choice = input('Any orders? ')
            if order_choice == '1':    # show orders
                print(str(order_list).replace("{", " ").replace("}", " ").replace(",", "\n").replace('"', ' ').replace("'", " ").replace("[", "\n").replace("]", "\n********").lstrip())

            elif order_choice == '2': # add order
                name =  input ("Waht's your name? ")
                address = input ("What's your address? ")
                phone = input ("What's your phone number? ")
                ori_couriers_list = ['Available Couriers {} : {}'.format(c, courier) for c, courier in enumerate(couriers_list)]
                print(ori_couriers_list)
                courier = int(input ("Who deliver the order? Please enter the index"))
                order['Customer_name'] = name
                order['Customer_address'] = address
                order['Customer_phone'] = phone
                order['Courier'] = courier
                order['Status'] = 'preparaing'
                status_list.append('preparaing')
                for i in range(1):
                  order_list.append(order.copy())
                print("New Order\n" + str(order_list).replace("{", " ").replace("}", " ").replace(",", "\n").replace('"', ' ').replace("'", " ").replace("[", "\n").replace("]", "\n********").lstrip())


            elif order_choice == "3":
                print("Orders:")
                for index, order in enumerate(order_list):
                    print("Order ID :", index, "\n", str(order).replace("{", " ").replace("}", " ").replace(",", "\n").replace('"', ' ').replace("'", " "),"\n********")
                    order_index = int(input("Enter order index to update status: "))
                    if order_index < len(order_list):
                        print("1. Preparing")
                        print("2. Ready to Deliver / Collect")
                        print("3. Delivered / Collected")
                        status_choice = int(input("Enter status option: "))
                        if status_choice == 1:
                            order_list[order_index]["Status"] = "Preparing"
                        elif status_choice == 2:
                            order_list[order_index]["Status"] = "Ready to Deliver / Collect"
                        elif status_choice == 3:
                            order_list[order_index]["Status"] = "Delivered / Collected"
                        else:
                            print("Invalid status option. Please try again.")
                            print("Amended Order\n" + str(order_list).replace("{", " ").replace("}", " ").replace(",", "\n").replace('"', ' ').replace("'", " ").replace("[", "\n").replace("]", "\n********"))
                    else:
                        print("Invalid status option. Please try again.")

                for index, status in enumerate(status_list): # update of status list
                  print("Order ID :", index, "\n", str(status).replace("{", " ").replace("}", " ").replace(",", "\n").replace('"', ' ').replace("'", " "),"\n********")
                  status_index = int(input("Enter status index to update status list: "))
                  if status_index < len(status_list):
                        print("1. Preparing")
                        print("2. Ready to Deliver / Collect")
                        print("3. Delivered / Collected")
                        status_choice = int(input("Enter status option: "))
                        if status_choice == 1:
                            status_list[status_index] = "Preparing"
                        elif status_choice == 2:
                            status_list[status_index] = "Ready to Deliver / Collect"
                        elif status_choice == 3:
                            status_list[status_index] = "Delivered / Collected"


            elif order_choice == "4":
                print("Orders:")
                for index, order in enumerate(order_list):
                    print("Order ID :", index, "\n", str(order).replace("{", " ").replace("}", " ").replace(",", "\n").replace('"', ' ').replace("'", " "),"\n********")
                    order_index = input("Enter order index to update: ")
                    order_index = int(order_index)
                    if order_index < len(order_list):
                        for key in order_list[order_index]:
                            new_value = input(f"Enter new {key} (press enter to keep current value): ")
                            if new_value != "":
                                order_list[order_index][key] = new_value
                                print("Order updated successfully.")
                                print("Updated Order\n" + str(order_list).replace("{", " ").replace("}", " ").replace(",", "\n").replace('"', ' ').replace("'", " ").replace("[", "\n").replace("]", "\n********"))
                    else:
                        print("Invalid input or index. Please try again.")

            elif order_choice == '5': # delete order
                order_list = ['{}: {}'.format(o, orders) for o, orders in enumerate(order_list)]
                print(str(order_list).replace("{", " ").replace("}", " ").replace(",", "\n").replace('"', ' ').replace("'", " ").replace("[", "\n").replace("]", "\n********"))
                delete_order_in = input('Please enter an index value to delete order! ')
                delete_order_in = int(delete_order_in)
                if delete_order_in < len(order_list):
                    del order_list[delete_order_in]
                if delete_order_in >= len(order_list):
                    print("Please entre the correct index! ")

            elif order_choice == '0':
                break