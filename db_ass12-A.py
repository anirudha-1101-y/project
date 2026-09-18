"""
SSIGNMENT 1: ONLINE SHOPPING ORDER MANAGEMENT SYSTEM
======================================================

An online shopping company wants to manage customers, products, and orders
using Python Database Connectivity (PDBC).

Students must use Python mysql.connector and MySQL.


DATABASE TABLES
===============

TABLE 1: customer_order_pdbc
----------------------------
Column       Data Type
--------------------------------
customer_id  INT PRIMARY KEY
customer_name VARCHAR(60)
city         VARCHAR(40)
email        VARCHAR(80)

SAMPLE DATA
-----------
customer_id  customer_name  city       email
---------------------------------------------------------
1            Amit           Indore     amit@gmail.com
2            Priya          Bhopal     priya@gmail.com
3            Rahul          Indore     rahul@gmail.com
4            Neha           Ujjain     neha@gmail.com
5            Karan          Dewas      karan@gmail.com


TABLE 2: product_order_pdbc
---------------------------
Column       Data Type
--------------------------------
product_id   INT PRIMARY KEY
product_name VARCHAR(80)
category     VARCHAR(40)
price        DECIMAL(10,2)
stock        INT

product_id  product_name  category       price      stock
------------------------------------------------------------
101         Laptop        Electronics    55000.00   10
102         Mouse         Electronics      800.00   50
103         Keyboard      Electronics     1500.00   30
104         Notebook      Stationery       100.00  100
105         Monitor       Electronics    12000.00   15
106         Pen            Stationery        20.00  200


TABLE 3: customer_order_details
-------------------------------
Column       Data Type
--------------------------------
order_id     INT PRIMARY KEY
customer_id  INT
product_id   INT
quantity     INT
order_status VARCHAR(30)

Foreign keys:
customer_id references customer_order_pdbc(customer_id)
product_id references product_order_pdbc(product_id)

SAMPLE DATA
-----------
order_id  customer_id  product_id  quantity  order_status
------------------------------------------------------------
1001      1            101          1         Delivered
1002      1            102          2         Delivered
1003      2            103          1         Shipped
1004      3            105          2         Delivered
1005      3            104          5         Pending
1006      4            101          1         Pending
1007      5            106          10        Delivered


MENU
====

===== ONLINE SHOPPING ORDER MANAGEMENT =====
1. Add Customer
2. Add Product
3. Place Order
4. Display All Orders with Customer and Product Details
5. Search Customer by Name
6. Update Product Price
7. Update Order Status
8. Delete Order
9. Display Customer-wise Total Purchase Amount
10. Display Products Costing More Than Average Product Price
11. Display Customers Who Have Placed at Least One Order
12. Display Customers Who Have Not Placed Any Order
13. Exit

Enter your choice:


TASKS AND EXPECTED INPUT/OUTPUT
==============================

1. ADD CUSTOMER
---------------

INPUT
-----
Enter your choice: 1
Enter Customer ID: 6
Enter Customer Name: Anjali
Enter City: Indore
Enter Email: anjali@gmail.com

OUTPUT
------
Customer inserted successfully.


2. ADD PRODUCT
-------------

INPUT
-----
Enter your choice: 2
Enter Product ID: 107
Enter Product Name: Headphones
Enter Category: Electronics
Enter Price: 2500
Enter Stock: 25

OUTPUT
------
Product inserted successfully.


3. PLACE ORDER
--------------

INPUT
-----
Enter your choice: 3
Enter Order ID: 1008
Enter Customer ID: 6
Enter Product ID: 107
Enter Quantity: 2
Enter Order Status: Pending

OUTPUT
------
Order placed successfully.


4. DISPLAY ALL ORDERS USING INNER JOIN
--------------------------------------

REQUIRED OPERATION
------------------
Display order ID, customer name, product name, quantity, price,
calculated amount, and order status.

Calculated amount = quantity * price

EXPECTED OUTPUT
---------------
Order ID  Customer Name  Product Name  Quantity  Price     Amount    Status
----------------------------------------------------------------------------
1001      Amit           Laptop         1        55000.00  55000.00  Delivered
1002      Amit           Mouse          2          800.00   1600.00  Delivered
1003      Priya          Keyboard       1         1500.00   1500.00  Shipped
1004      Rahul          Monitor        2        12000.00  24000.00  Delivered
1005      Rahul          Notebook       5          100.00    500.00  Pending
1006      Neha           Laptop         1        55000.00  55000.00  Pending
1007      Karan          Pen            10          20.00    200.00  Delivered


5. SEARCH CUSTOMER USING LIKE
-----------------------------

INPUT
-----
Enter your choice: 5
Enter customer name to search: an

OUTPUT
------
Customer ID  Customer Name  City
-------------------------------------
1            Amit           Indore
5            Karan          Dewas

Note:
Use LIKE '%an%' in the SQL query.
The result may include names containing the entered text.


6. UPDATE PRODUCT PRICE
-----------------------

INPUT
-----
Enter your choice: 6
Enter Product ID: 102
Enter New Price: 900

OUTPUT
------
Product price updated successfully.


7. UPDATE ORDER STATUS
----------------------

INPUT
-----
Enter your choice: 7
Enter Order ID: 1005
Enter New Status: Delivered

OUTPUT
------
Order status updated successfully.


8. DELETE ORDER
---------------

INPUT
-----
Enter your choice: 8
Enter Order ID: 1007

OUTPUT
------
Order deleted successfully.


9. CUSTOMER-WISE TOTAL PURCHASE AMOUNT
--------------------------------------

REQUIRED SQL CONCEPTS
---------------------
INNER JOIN
GROUP BY
SUM()
ORDER BY

Required output columns:
Customer ID, Customer Name, Total Purchase Amount

EXPECTED OUTPUT
---------------
Customer ID  Customer Name  Total Purchase Amount
--------------------------------------------------
1            Amit           56600.00
2            Priya           1500.00
3            Rahul          24500.00
4            Neha           55000.00
5            Karan           200.00

Formula:
SUM(order_quantity * product_price)


10. PRODUCTS COSTING MORE THAN AVERAGE PRICE
--------------------------------------------

REQUIRED CONCEPT
----------------
Single-row subquery.

Question:
Display products whose price is greater than the average price
of all products.

EXPECTED OUTPUT
---------------
Product ID  Product Name  Price
-------------------------------------
101         Laptop         55000.00
105         Monitor        12000.00


11. CUSTOMERS WHO HAVE PLACED AT LEAST ONE ORDER
------------------------------------------------

REQUIRED CONCEPT
----------------
Subquery using IN or EXISTS.

Question:
Display customers who have placed at least one order.

EXPECTED OUTPUT
---------------
Customer ID  Customer Name
--------------------------
1            Amit
2            Priya
3            Rahul
4            Neha
5            Karan


12. CUSTOMERS WHO HAVE NOT PLACED ANY ORDER
-------------------------------------------

REQUIRED CONCEPT
----------------
LEFT JOIN with IS NULL
OR NOT EXISTS subquery.

Question:
Display customers who have never placed an order.

EXPECTED OUTPUT
---------------
Customer ID  Customer Name
--------------------------
6            Anjali

Note:
This output assumes customer 6 was inserted but has not placed an order.


13. FOREIGN KEY TEST
--------------------

Try to place an order with a customer ID that does not exist.

INPUT
-----
Enter your choice: 3
Enter Order ID: 1009
Enter Customer ID: 999
Enter Product ID: 101
Enter Quantity: 1
Enter Order Status: Pending

EXPECTED OUTPUT
---------------
Order could not be inserted because the customer ID
does not exist in the parent table.

Students should observe the foreign key constraint error.


14. MENU VALIDATION
-------------------

If the user enters an invalid menu choice:

INPUT
-----
Enter your choice: 20

OUTPUT
------
Invalid choice. Please try again.

"""
"""
mysql> create table customer_order_pdbc(customer_id int primary key,customer_name varchar(60),city varchar(40),email varchar(80));
Query OK, 0 rows affected (0.10 sec)

mysql> desc  customer_order_pdbc;
+---------------+-------------+------+-----+---------+-------+
| Field         | Type        | Null | Key | Default | Extra |
+---------------+-------------+------+-----+---------+-------+
| customer_id   | int         | NO   | PRI | NULL    |       |
| customer_name | varchar(60) | YES  |     | NULL    |       |
| city          | varchar(40) | YES  |     | NULL    |       |
| email         | varchar(80) | YES  |     | NULL    |       |
+---------------+-------------+------+-----+---------+-------+

mysql> INSERT INTO customer_order_pdbc
    -> VALUES
    -> (1, 'Amit', 'Indore', 'amit@gmail.com'),
    -> (2, 'Priya', 'Bhopal', 'priya@gmail.com'),
    -> (3, 'Rahul', 'Indore', 'rahul@gmail.com'),
    -> (4, 'Neha', 'Ujjain', 'neha@gmail.com'),
    -> (5, 'Karan', 'Dewas', 'karan@gmail.com');
Query OK, 5 rows affected (0.03 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select * from customer_order_pdbc;
+-------------+---------------+--------+-----------------+
| customer_id | customer_name | city   | email           |
+-------------+---------------+--------+-----------------+
|           1 | Amit          | Indore | amit@gmail.com  |
|           2 | Priya         | Bhopal | priya@gmail.com |
|           3 | Rahul         | Indore | rahul@gmail.com |
|           4 | Neha          | Ujjain | neha@gmail.com  |
|           5 | Karan         | Dewas  | karan@gmail.com |


mysql> create table product_order_pdbc(product_id int primary key,product_name varchar(80),category varchar(40),price decimal(10,2),stock int);
Query OK, 0 rows affected (0.04 sec)

mysql> desc product_order_pdbc;
+--------------+---------------+------+-----+---------+-------+
| Field        | Type          | Null | Key | Default | Extra |
+--------------+---------------+------+-----+---------+-------+
| product_id   | int           | NO   | PRI | NULL    |       |
| product_name | varchar(80)   | YES  |     | NULL    |       |
| category     | varchar(40)   | YES  |     | NULL    |       |
| price        | decimal(10,2) | YES  |     | NULL    |       |
| stock        | int           | YES  |     | NULL    |       |
+--------------+---------------+------+-----+---------+-------+
5 rows in set (0.01 sec)

mysql> INSERT INTO product_order_pdbc
    -> VALUES
    -> (101, 'Laptop', 'Electronics', 55000.00, 10),
    -> (102, 'Mouse', 'Electronics', 800.00, 50),
    -> (103, 'Keyboard', 'Electronics', 1500.00, 30),
    -> (104, 'Notebook', 'Stationery', 100.00, 100),
    -> (105, 'Monitor', 'Electronics', 12000.00, 15),
    -> (106, 'Pen', 'Stationery', 20.00, 200);
Query OK, 6 rows affected (0.01 sec)
Records: 6  Duplicates: 0  Warnings: 0

mysql> select * from product_order_pdbc;
+------------+--------------+-------------+----------+-------+
| product_id | product_name | category    | price    | stock |
+------------+--------------+-------------+----------+-------+
|        101 | Laptop       | Electronics | 55000.00 |    10 |
|        102 | Mouse        | Electronics |   800.00 |    50 |
|        103 | Keyboard     | Electronics |  1500.00 |    30 |
|        104 | Notebook     | Stationery  |   100.00 |   100 |
|        105 | Monitor      | Electronics | 12000.00 |    15 |
|        106 | Pen          | Stationery  |    20.00 |   200 |
+------------+--------------+-------------+----------+-------+


mysql> create table customer_order_detail(order_id int primary key,customer_id int,product_id int ,quantity int,order_status varchar(30),foreign key(customer_id) references customer_order_pdbc(customer_id) ,foreign key(product_id) references product_order_pdbc(product_id));
Query OK, 0 rows affected (0.07 sec)

mysql> desc customer_order_detail;
+--------------+-------------+------+-----+---------+-------+
| Field        | Type        | Null | Key | Default | Extra |
+--------------+-------------+------+-----+---------+-------+
| order_id     | int         | NO   | PRI | NULL    |       |
| customer_id  | int         | YES  | MUL | NULL    |       |
| product_id   | int         | YES  | MUL | NULL    |       |
| quantity     | int         | YES  |     | NULL    |       |
| order_status | varchar(30) | YES  |     | NULL    |       |
+--------------+-------------+------+-----+---------+-------+

mysql>  INSERT INTO customer_order_detail
    -> values
    -> (1001, 1, 101, 1, 'Delivered'),
    -> (1002, 1, 102, 2, 'Delivered'),(1003, 2, 103, 1, 'Shipped'),
    -> (1004, 3, 105, 2, 'Delivered'),
    -> (1005, 3, 104, 5, 'Pending'),
    -> (1006, 4, 101, 1, 'Pending'),
    -> (1007, 5, 106, 10, 'Delivered');
Query OK, 7 rows affected (0.02 sec)
Records: 7  Duplicates: 0  Warnings: 0

mysql> select * from customer_order_detail;
+----------+-------------+------------+----------+--------------+
| order_id | customer_id | product_id | quantity | order_status |
+----------+-------------+------------+----------+--------------+
|     1001 |           1 |        101 |        1 | Delivered    |
|     1002 |           1 |        102 |        2 | Delivered    |
|     1003 |           2 |        103 |        1 | Shipped      |
|     1004 |           3 |        105 |        2 | Delivered    |
|     1005 |           3 |        104 |        5 | Pending      |
|     1006 |           4 |        101 |        1 | Pending      |
|     1007 |           5 |        106 |       10 | Delivered    |
+----------+-------------+------------+----------+--------------+

"""
import mysql.connector
conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
cursor=conn.cursor()

while True:

    print("""1. Add Customer
             2. Add Product
             3. Place Order
             4. Display All Orders with Customer and Product Details
             5. Search Customer by Name
             6. Update Product Price
             7. Update Order Status
             8. Delete Order
             9. Display Customer-wise Total Purchase Amount
             10. Display Products Costing More Than Average Product Price
             11. Display Customers Who Have Placed at Least One Order
             12. Display Customers Who Have Not Placed Any Order
             13. Exit""")
    ch=int(input("enter your choice :"))
    match ch:
        case 1:
            customer_id=int(input("enter your id :"))
            customer_name=input("enter your name ")
            city=input("enter your city: ")
            email=input("enter your email :")

            query="insert into customer_order_pdbc values(%s,%s,%s,%s)"
            cursor.execute(query,(customer_id,customer_name,city,email,))
            conn.commit()
            print("inserted succesfully...")
            conn.close()
        case 2:
            product_id=int(input("enter your id :"))
            product_name=input("enter your name ")
            category=input("enter category :")
            price=float(input("enter price:"))
            stock=int(input("enter stock :"))
            query="insert into product_order_pdbc values(%s,%s,%s,%s,%s)"
            cursor.execute(query,(product_id,product_name,category,price,stock,))
            conn.commit()
            print("inserted succesfully...")
            conn.close()
        case 3:
            order_id=int(input("enter your order id: "))
            customer_id=int(input("enter your customer id :"))
            product_id=int(input("enter your product id :"))
            quantity=int(input("enter your quantity :"))
            order_status=input("enter order status :")
            query="insert into customer_order_detail values(%s,%s,%s,%s,%s)"
            cursor.execute(query,(order_id,customer_id,product_id,quantity,order_status,))
            conn.commit()
            print("inserted succesfully...")
            conn.close()
        case 4:
            query="select o.order_id,c.customer_name,p.product_name,o.quantity,o.order_status,p.price,o.quantity * p.price as amount from customer_order_pdbc as c inner join customer_order_detail as o on c.customer_id=o.customer_id inner join product_order_pdbc as p on p.product_id=o.product_id "
            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)
                print()
            conn.close()

        case 5:
            name=input("enter name :")
            query="select * from customer_order_pdbc where customer_name like %s"
            cursor.execute(query ,("%" +name+ "%",))
            for row in cursor.fetchall():
                print(row)
            conn.close()
        case 6:
            

            







