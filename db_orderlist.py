import pymysql

conn = pymysql.connect(
host='localhost',
database='baking_cafe',
user='root',
password='password')
cur = conn.cursor()


def order_list_menu():           # Order list menu
    print("=====Order List Menu====")
    print("===========================")
    print("======1) List by ID========")
    print("=====2) List by Couries====")
    print("=====3) List by Status=====")
    print("===0) Back to Couriers Menu====")
    print("===========================")

def order_list():       # print order list by different features
    order_list_menu()
    order_list_options = input("Product List By: ")
    if order_list_options == "1":  # print order list by order id
        cur.execute("select * from orders")
        over_orders_list = cur.fetchall()
        for order in over_orders_list:
            print(order)
    elif order_list_options == "2": # print order list by couriers
        print("List by Ascending(A) or Decending(D) Order? ")
        order_c_options = ("Please Enter A or D ! ")
        if order_c_options == "A": # print order list by couriers in ascending
            cur.execute("SELECT * FROM orders ORDER BY courier")
            orders_a_list = cur.fetchall()
            for order in orders_a_list:
                print(order)
        if order_c_options == "D": # print order list by couriers in ascending
            cur.execute("SELECT * FROM orders ORDER BY courier desc")
            orders_d_list = cur.fetchall()
            for order in orders_d_list:
                print(order)
        else:     # for pytest
            pass  #raise typeerror
    elif order_list_options == "3":
        cur.execute("SELECT * FROM orders o JOIN order_status os on o.order_status_id = os.order_status_id ORDER BY os.order_status")
        ori_orders_list = cur.fetchall()
        for order in ori_orders_list:
            print(order)