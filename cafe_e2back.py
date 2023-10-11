products = ['Bacon Roll', 'Banana', 'Apple',
            'Ham & Chess Tosties', 'Chocolate',
            'Latte', 'Cappuccino', 'Chia Latte',
            'Macchiato'] # stores items for sales
order = {'Customer_name':'Ben Conor',
         'Customer_address':'077438379',
         'Customer_phone': 'Unit 2, 12 Main Street, LONDON, WH1 2ER',
         'Status': 'Preparaing'}
order_list = []
status_list = []
products_menu=("""
      Baking Cafe Product Menu
    ===========================
    1. Products
    2. Add New Products
    3. Update Products
    4. Delete Products
    0. back to Main Menu""")
orders_menu = ("""
        Baking Cafe Orders Menu
        ======================
        1. Order Record
        2. Start New Orders
        3. Update Orders Status
        4. Update Orders Details
        5. Delete Orders
        0. Back to Main Menu""")
keep_looping = True
while keep_looping == True: # main manu
  print("""
        Baking Cafe Main Menu
        ======================
        1. Products Menu
        2. Orders Menu
        0. Exit""")
  menu_option = input('Which menu?')
  if menu_option == '0':
    break
  elif menu_option == '1':              # products manu
    while keep_looping == True:
      print(products_menu)
      product_choice = input('What are you going to do? ')

      if product_choice == '1':   # identifies Products in 1
        for p in products:
          print(f'Products: {p}')

      elif product_choice == '2': #add new products
          option_2 = input ('Please enter a product name! ')
          print(option_2)
          products.append(option_2)
          print(products)

      elif product_choice == '3': #update existing products
          products_list = ['{}: {}'.format(p, product) for p, product in enumerate(products)]
          print(products_list)
          index_product = input ('Please Enter the index of Prodcuts! ')
          update_pro_name = input ('Please Update the name of Prodoucts! ')
          index_item = int(index_product)
          if index_item < len(products):
            products[index_item] = update_pro_name
            print(products)
          elif index_item >= len(products):
            print(f"Invalid index detected! Please enter index! ")

      elif product_choice == '4': # delete existing products
          products_list = ['{}: {}'.format(p, product) for p, product in enumerate(products)]
          print(products_list)
          index_product = input ('Please Enter the index of Prodcuts! ')
          index_item = int(index_product)
          if index_item < len(products):
            del products[index_item]
            print(products)
          else:
            print("Please insert a correct index of products! ")

      elif product_choice == '0': # exit product manu
          break

  elif menu_option == '2':  # enter orders manu
        while keep_looping == True:
            print(orders_menu)
            order_choice = input('Any orders? ')
            if order_choice == '1':    # show orders
                print(str(order_list).replace("{", " ").replace("}", " ").replace(",", "\n").replace('"', ' ').replace("'", " ").replace("[", "\n").replace("]", "\n********"))

            elif order_choice == '2': # add order
                name =  input ("Waht's your name? ")
                address = input ("What's your address? ")
                phone = input ("What's your phone number? ")
                order['Customer_name'] = name
                order['Customer_address'] = address
                order['Customer_phone'] = phone
                order['Status'] = 'PREPARAING'
                status_list.append('preparaing')
                for i in range(1):
                  order_list.append(order.copy())
                print("New Order\n" + str(order_list).replace("{", " ").replace("}", " ").replace(",", "\n").replace('"', ' ').replace("'", " ").replace("[", "\n").replace("]", "\n********"))


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