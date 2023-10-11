couriers_file = open('couriers.txt', 'a+') # Load products list
couriers_doc = print(couriers_file.read())
products_file = open('products.txt', 'a+') # Load couriers lsit
products_doc= print(products_file.read())
products = ['Bacon Roll', 'Banana', 'Apple',
            'Ham & Chess Tosties', 'Chocolate',
            'Latte', 'Cappuccino', 'Chia Latte',
            'Macchiato'] # stores items for sales
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
order = {'Customer_name':'Ben Conor',
         'Customer_address':'077438379',
         'Customer_phone': 'Unit 2, 12 Main Street, LONDON, WH1 2ER',
         'Status': 'Preparaing'}  # dictionary of order
order_list = [] # lsit of orders
status_list = [] # list of order status
couriers_list = ['John' , 'Claire'] # list of couriers

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
    for product in products:
        products_file.write(product)
    products_file.close()
    for courier in couriers_list:
        couriers_file.write(courier)
    couriers_file.close()
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

  elif menu_option == '2':
      while keep_looping == True:
          print(couriers_menu)
          couriers_choice = input("Anything Related to Couriers ? ")

          if couriers_choice == '0': # back to Main Menu
            break

          elif couriers_choice == '1': # print couriers list
                print(f"Couriers List\n{couriers_list}")

          elif couriers_choice == '2':  # add new couriers
            courier_name = input("Please Enter Couriers Name! ")
            couriers_list.append(courier_name)
            print(f"New Couriers List\n{couriers_list}")

          elif couriers_choice == '3': # update existed couriers
            ori_couriers_list = ['{}: {}'.format(c, courier) for c, courier in enumerate(couriers_list)]
            print(ori_couriers_list)
            courier_index = int(input("Please Enter the index of Couriers! "))
            new_name = input("Please Type New Courier Name ! ")
            if courier_index < len(ori_couriers_list):
              couriers_list[courier_index] = new_name
              print(f"Updated Couriers List\n{couriers_list}")
            else:
              print("Please Enter Corect Index! ")

          elif couriers_choice == '4' : # delete couriers
            ori_couriers_list = ['{}: {}'.format(c, courier) for c, courier in enumerate(couriers_list)]
            print(ori_couriers_list)
            courier_index = int(input("Who need to be deleted? Please Enter Index! "))
            if courier_index < len(ori_couriers_list):
              del couriers_list[courier_index]
              print(f"Reduced Couriers List\n{couriers_list}")
            else:
              print("Please Enter Correct Index Value! ")