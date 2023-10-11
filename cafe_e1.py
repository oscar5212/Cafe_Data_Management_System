products = ['Bacon Roll', 'Banana', 'Apple',
            'Ham & Chess Tosties', 'Chocolate',
            'Latte', 'Cappuccino', 'Chia Latte',
            'Macchiato'] # stores items for sales
customer_name ='Ben Conor'
customer_number = '077438379'
customer_address = 'Unit 2, 12 Main Street, LONDON, WH1 2ER'
status = 'Preparaing'
orders = {'Customer_name':'Ben Conor', 'Customer_address': 'Unit 2, 12 Main Street, LONDON, WH1 2ER', 'Customer_phone': '077438379', 'Status': 'Preparaing'} # stores orders from customers
order_list = []
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
