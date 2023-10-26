# generation_mini_project

## Project Description

A local cafe shop requested for an application that can store data for their cafe shops in London,
which includes a users terminal for storing on sale products, available couriers, customers' orders,
additional storage for customer information and monitoring of inventory.

## Run the App
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
2) Press 2 to add new prodcuts, follow by entering name and price of new products.
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
1) Explore the existed orders by pressing 1 and follow by borwsing orders by id (1), couriers(2) and order status(3).
2) Add new orders by pressing 2 and inserting name, itmes, courier, address, and phone number.
3) Update order status by pressing 3 and typing status.
4) Update order details by correcting ordered items, and customers' informaiton.
5) Delete finished orders by pressing 5.
6) Return to Main Menu by 0.

### Customer Menu
1) List all the customes' information.
2) Update customsers' personla information such as name, address, phone number.
3) Add or change customers's membership number.
4) Return to Main Menu.

## Run Unite Test
1) Set a new function with arguments that would trigger the valueerror.
2) In the function, set expected result as valueerror and result of function import to the original function.
3) In assert area, assume expected result is the same as result of imported original funciton.


## Design Approach
The design of this application is mainly from the users view, which involves lots of chosing different options by variosu number.\
This is an easy way for employees locating the desire menu for related actions and reduce occurance of inserting wrong instructions.\
By understanding the requirments of the applcation and customer's need, all the simplified process can lower the cost of educating employees.
In order to assuring the functions aligned to project's requirement, the application separated to different aspect of functions as Products, Couriers, Orders and Customers. Thus, each fucntions can be tested individually and troubleshooted bugs.

## Additional Function
As one of the copmany's repsonsibilities is protecting customers' data, applying extra measures for editing and assessing customers' data is essential. The measure cna be only manager can edit or require additional password before assesing sensitive data and available products for the cafe.



##
