products = ['Bacon Roll', 'Banana', 'Apple',
            'Ham & Chess Tosties', 'Chocolate',
            'Latte', 'Cappuccino', 'Chia Latte',
            'Macchiato'] # stores items for sales
order = {'Customer_name':'Ben Conor', 'Customer_address':'077438379', 'Customer_phone': 'Unit 2, 12 Main Street, LONDON, WH1 2ER', 'Status': 'Preparaing'}
order_list = []
status_list = []
products_manu=("""
      Baking Cafe Product Manu
    ===========================
    1. Products
    2. Add New Products
    3. Update Products
    4. Delete Products
    0. Exit""")
orders_manu = ("""
        Baking Cafe Orders Manu
        ======================
        1. Order Record
        2. Start New Orders
        3. Update Orders Status
        4. Update Orders Details
        5. Delete Orders""")
keep_looping = True
while keep_looping == True: # main manu
  print("""
        Baking Cafe Main Manu
        ======================
        1. Products Manu
        2. Orders Manu
        0. Exit""")
  manu_option = input('Which manu?')
  if manu_option == '0':
    break
  elif manu_option == '1':              # products manu
    while keep_looping == True:
      print(products_manu)
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

  elif manu_option == '2':  # enter orders manu
        while keep_looping == True:
            print(orders_manu)
            order_choice = input('Any orders? ')
            if order_choice == '1':    # show orders
                print(str(order_list).replace("{", " ").replace("}", " ").replace(",", "\n").replace(('"'), (' ')).replace(("'"), (" ")))

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
                print(str(order_list).replace("{", " ").replace("}", " ").replace(",", "\n").replace(('"'), (' ')).replace(("'"), (" ")))

            elif order_choice == '3':  # edit status of order
                order_list = ["Order Number: {} :{}".format(o, orders) for o, orders in enumerate(order_list)]
                print(str(order_list).replace("{", " ").replace("}", " ").replace(",", "\n").replace(('"'), (' ')).replace(("'"), (" ")))
                edit_status_in = int(input ('Which one to be edited? '))
                if edit_status_in < len(order_list):
                  print("1. Preparing")
                  print("2. Ready to Collect / Deliver")
                  print("3. Delivered / Collected")
                  edit_status = int(input ('Please update the status! '))
                  if edit_status == 1:
                     order_list[edit_status_in]["Status"] = "Preparing"
                  elif edit_status == 2:
                     order_list[edit_status_in]["Status"] = "Ready to Collect / Deliver"
                  elif edit_status == 3:
                     order_list[edit_status_in]["Status"] = "Delivered / Collected"
                     print(str(order_list).replace("{", " ").replace("}", " ").replace(",", "\n").replace('"'), (' '). replace("'"), (" "))
                  else:
                    print("Please Try again")
                else:
                  print("Please Enter Correct Index!")

                status_list = ['Order Number: {}\n {} \n'.format(s, status) for s, status in enumerate(status_list)]
                print(str(status_list).replace("{", " ").replace("}", " ").replace(",", "\n").replace('"', ' ').replace("'", " "))
                status_index = int(input("Please enter the index! "))
                change_status = input("Please enter new status!")
                if status_index < len(status_list):
                    status_list[status_index]= change_status
                    print(str(status_list).replace("{", " ").replace("}", " ").replace(",", "\n").replace('"', ' ').replace("'", " "))
                elif status_index> len(status_list):
                    print("Please enter a correct index")

            elif order_choice == '4': # edit details of order
                order_list = ['{}: {}'.format(o, orders) for o, orders in enumerate(order_list)]
                print(str(order_list).replace("{", " ").replace("}", " ").replace(",", "\n").replace('"', ' ').replace("'", " "))
                edit_order_in = int(input ('Please enter an index value! '))
                for key in order_list[edit_order_in]:
                  edit_option = input (f"Enter new {key}: ")
                  if edit_option != '':
                    order_list[edit_order_in][key] = edit_option
                    print(str(order_list).replace("{", " ").replace("}", " ").replace(",", "\n").replace('"', ' ').replace("'", " "))
                else:
                  print("Please Enter Correct Instruction Again! ")

            elif order_choice == '5': # delete order
                order_list = ['{}: {}'.format(o, orders) for o, orders in enumerate(order_list)]
                print(str(order_list).replace("{", " ").replace("}", " ").replace(",", "\n").replace('"', ' ').replace("'", " "))
                delete_order_in = input('Please enter an index value to delete order! ')
                delete_order_in = int(delete_order_in)
                if delete_order_in < len(order_list):
                    del order_list[delete_order_in]
                if delete_order_in >= len(order_list):
                    print("Please entre the correct index! ")
  else:                       # Exit of main manu
      break
