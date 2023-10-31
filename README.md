# Café Management System

## Project Description

A local café requested for an application that can store data for their café in London, which includes a users interactive terminal (Command Line Interface) for storing on sale products, available couriers, customers' orders, additional storage for customer information and monitoring of inventory.

## Application Requirements
The main requirements from clients:
1) Tables for Products, Couriers and Orders
2) Access all Products, Couriers and Orders record
3) Update order status and store all data in database
4) Delete and update all three datasets

Additional Features:
1) List orders by status or couriers
2) Create and store customers' data in customer list
3) Check product inventory in real-time

## Run the App
### Upfront Preparation

**Docker**\
Run these Commands to install all the dependencies for the setup of software:
```docker
docker pull debian
docker pull python:3.9
docker pull adminer
docker pull mysql
py -m pip install -r requirements.txt
```
After successful installation of dependencies, run MySQL database with image and connect to the database:


```docker
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=pass mysql

mysql -h 127.0.0.1 -P3306 -uroot -p
```

**PySQL**
```PySQL
pip install pymysql
```

### Main Menu
1) Confirm database is online
2) Type py cafeweek6.py on terminal
3) Press 1 to locate at Product Menu
4) Press 2 to locate at Courier Menu
5) Press 3 to locate at Order Menu
6) Press 4 to locate at Customer Menu
7) Press 0 to Exit this application

### Product Menu
1) Press 1 to list existed products.
2) Press 2 to add new products, follow by entering name and price of new products.
3) Choose number 3 to update existed products.
4) Delete the products by pressing 4 and ID of products.
5) Return to Main Menu by pressing 0.

### Courier Menu
1) Explore the available couriers by pressing 1.
2) Add new couriers by pressing 2 and typing name and phone number.
3) Update couriers' information by pressing 3 and typing name and phone number.
4) Delete unavailable couriers by number 4 and inserting related ID.
5) Return to Main Menu by pressing 0.

### Orders Menu
1) Explore the existed orders by pressing 1 and follow by browsing orders by id (1), couriers (2) and order status (3).
2) Add new orders by pressing 2 and inserting name, items, courier, address, and phone number.
3) Update order status by pressing 3 and typing status.
4) Update order details by correcting ordered items, and customers' information.
5) Delete finished orders by pressing 5.
6) Return to Main Menu by 0.

### Customer Menu
1) List all the customers' information.
2) Update customers' personal information such as name, address, phone number.
3) Add or change customers' membership number.
4) Return to Main Menu.

## Run Unite Test
1) Set a new function with arguments that would trigger the ValueError.
2) In the function, set expected result as valueerror and result of function import to the original function.
3) In assert area, assume expected result is the same as result of imported original function.

# Project Reflection

## Design Approach
The design of this application is mainly from the users view, which involves lots of different options by various number.\
This is an easy way for employees locating the desired menu for related actions and reduce occurrence of inserting wrong instructions.\
By understanding the requirements of the application and customer's need, all the simplified process can lower the cost of educating employees.
In order to assuring the functions aligned to project's requirement, the application separated to different modules of functions as Products, Couriers, Orders and Customers. Thus, each functions can be tested individually and troubleshooted bugs.

## Additional Function
As one of the company's responsibilities is protecting customers' data, applying extra measures for editing and assessing customers' data is essential. The measure can only be handled by manager with additional password before assessing sensitive data and available products for the café.
During the process of editing, importing and exporting customers 'data, the handlers need to confirm the actions with their identification (Staff ID). All the actions and activities in this application will store in a log file.

## Enjoyment
The satisfaction of this project lies in the sense of accomplishment that comes with achieving goals and overcoming challenges while developing an application from scratch to one with multiple options. In this process, persistence and problem-solving skills are essential, as there are numerous errors and bugs that need to be fixed in the development cycle. With a troubleshooting mindset, developing an application is not a daunting task. Additionally, being resourceful is an important quality that shines through in this process, especially when peers are not available to help.

### Author
Oscar Choy