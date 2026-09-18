"""
=========================================================
ASSIGNMENT 3: PRODUCT INVENTORY MANAGEMENT SYSTEM
=========================================================

SCENARIO
--------
A retail shop wants to manage product details, prices,
categories, and available stock using Python PDBC.

CONCEPTS TO PRACTICE
--------------------
1. INSERT
2. SELECT
3. UPDATE
4. DELETE
5. LIKE operator
6. Parameterized queries
7. commit()
8. fetchall()
9. Menu-driven programming


TABLE STRUCTURE
===============

Table Name: product_pdbc

Column       Data Type
--------------------------------
pid          INT PRIMARY KEY
pname        VARCHAR(60)
category     VARCHAR(40)
price        DECIMAL(10,2)
quantity     INT


SAMPLE DATA
===========

pid   pname       category       price       quantity
------------------------------------------------------------
301   Laptop      Electronics    55000.00    10
302   Mouse       Electronics      800.00    50
303   Keyboard    Electronics     1500.00    30
304   Notebook    Stationery       100.00   100
305   Pen         Stationery        20.00   200


MENU
====

===== PRODUCT INVENTORY SYSTEM =====
1. Add Product
2. Display All Products
3. Search Product by Name
4. Update Product Price
5. Delete Product
6. Exit

Enter your choice:


TASK 1: ADD PRODUCT
===================

INPUT
-----
Enter your choice: 1
Enter Product ID: 306
Enter Product Name: Monitor
Enter Category: Electronics
Enter Price: 12000
Enter Quantity: 15

OUTPUT
------
Product inserted successfully.


TASK 2: DISPLAY ALL PRODUCTS
============================

INPUT
-----
Enter your choice: 2

OUTPUT
------
ID    Product       Category       Price       Quantity
------------------------------------------------------------
301   Laptop        Electronics     55000.00    10
302   Mouse         Electronics       800.00    50
303   Keyboard      Electronics      1500.00    30
304   Notebook      Stationery        100.00   100
305   Pen           Stationery         20.00   200
306   Monitor       Electronics     12000.00    15


TASK 3: SEARCH PRODUCT BY NAME USING LIKE
=========================================

INPUT
-----
Enter your choice: 3
Enter product name to search: o

OUTPUT
------
Matching products:

ID    Product       Category       Price       Quantity
------------------------------------------------------------
301   Laptop        Electronics     55000.00    10
302   Mouse         Electronics       800.00    50
304   Notebook      Stationery        100.00   100
306   Monitor       Electronics     12000.00    15

NOTE
----
Use:
WHERE pname LIKE %s

Pass:
'%' + search_name + '%'


TASK 4: UPDATE PRODUCT PRICE
============================

INPUT
-----
Enter your choice: 4
Enter Product ID: 302
Enter New Price: 900

OUTPUT
------
Product price updated successfully.


TASK 5: DELETE PRODUCT
======================

INPUT
-----
Enter your choice: 5
Enter Product ID: 305

OUTPUT
------
Product deleted successfully.


TASK 6: EXIT
============

INPUT
-----
Enter your choice: 6

OUTPUT
------
Thank you for using Product Inventory System.


add these scenarios also:--

1. Display all products from Electronics category.
2. Display all products from Stationery category.
3. Search products whose names contain 'oo'.
4. Search products whose names start with 'M'.
5. Search products whose names end with 'e'.
6. Display products whose price is greater than 1000.
7. Display products whose quantity is less than 20.
8. Update product quantity.
9. Update product category.
10. Delete a product by ID.
11. Display products whose category contains 'tron'.
12. Search products by a user-provided price range.



SUGGESTED SUCCESS MESSAGES
==========================

INSERT:
Record inserted successfully.

SELECT:
Records displayed successfully.

UPDATE:
Record updated successfully.

DELETE:
Record deleted successfully.

NOT FOUND:
No record found for the given ID.

INVALID CHOICE:
Invalid choice. Please try again.

EXIT:
Thank you for using the system.

"""


"""
mysql> CREATE TABLE product_pdbc (
    ->     pid INT PRIMARY KEY,
    ->     pname VARCHAR(60),
    ->     category VARCHAR(40),
    ->     price DECIMAL(10,2),
    ->     quantity INT
    -> );
Query OK, 0 rows affected (0.10 sec)

mysql> desc product_pdbc;
+----------+---------------+------+-----+---------+-------+
| Field    | Type          | Null | Key | Default | Extra |
+----------+---------------+------+-----+---------+-------+
| pid      | int           | NO   | PRI | NULL    |       |
| pname    | varchar(60)   | YES  |     | NULL    |       |
| category | varchar(40)   | YES  |     | NULL    |       |
| price    | decimal(10,2) | YES  |     | NULL    |       |
| quantity | int           | YES  |     | NULL    |       |
+----------+---------------+------+-----+---------+-------+
5 rows in set (0.04 sec)

mysql> INSERT INTO product_pdbc (pid, pname, category, price, quantity)
    -> VALUES
    -> (301, 'Laptop', 'Electronics', 55000.00, 10),
    -> (302, 'Mouse', 'Electronics', 800.00, 50),
    -> (303, 'Keyboard', 'Electronics', 1500.00, 30),
    -> (304, 'Notebook', 'Stationery', 100.00, 100),
    -> (305, 'Pen', 'Stationery', 20.00, 200);
Query OK, 5 rows affected (0.02 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select * from product_pdbc;
+-----+----------+-------------+----------+----------+
| pid | pname    | category    | price    | quantity |
+-----+----------+-------------+----------+----------+
| 301 | Laptop   | Electronics | 55000.00 |       10 |
| 302 | Mouse    | Electronics |   800.00 |       50 |
| 303 | Keyboard | Electronics |  1500.00 |       30 |
| 304 | Notebook | Stationery  |   100.00 |      100 |
| 305 | Pen      | Stationery  |    20.00 |      200 |
+-----+----------+-------------+----------+----------+

"""
"""
mysql> create table product_pdbc (pid int primary key, pname varchar(60), category varchar(40), price decimal(10,2), quantity int);
Query OK, 0 rows affected (0.43 sec)

mysql> insert into product_pdbc values(301,'laptop','electronics',50000, 10),(302,'Mouse','Electronics',800,50),(303,'keyboard','electronics',1500,30),(304,'Notebook','Stationary',100,100),(305,'pen','stationary',20,20);
Query OK, 5 rows affected (0.16 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select * from product_pdbc;
+-----+----------+-------------+----------+----------+
| pid | pname    | category    | price    | quantity |
+-----+----------+-------------+----------+----------+
| 301 | laptop   | electronics | 50000.00 |       10 |
| 302 | Mouse    | Electronics |   800.00 |       50 |
| 303 | keyboard | electronics |  1500.00 |       30 |
| 304 | Notebook | Stationary  |   100.00 |      100 |
| 305 | pen      | stationary  |    20.00 |       20 |
+-----+----------+-------------+----------+----------+
5 rows in set (0.05 sec)
"""
import mysql.connector
conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
cursor=conn.cursor()

while True:
    print("MENU")
    print("1. Add Product")
    print("2. Display all Products")
    print("3. Search Product by Name")
    print("4. Update Produst Price")
    print("5. Delete Product")
    print("6. Search by Category")
    print("7. Search name contains")
    print("8. Search name starts with")
    print("9. Search name ends with")
    print("10.Search price greater than")
    print("11. Search by Quantity greater than")
    print("12. Update Product Quantity")
    print("13. Update Product Category")
    print("14. Delete Product by ID")
    print("15. Search category contains")
    print("16. Search by User Inserted Price")
    print("17. Exit")

    choice = int(input("Enter your choice : "))
  
    match choice:
        case 1:
            pid = int(input("Enter Product id : "))
            pname = (input("Enter Product name : "))
            category = (input("Enter Product Category : "))
            price = float(input("Enter Product Price : "))
            quantity = int(input("Enter Quantity : "))
            query = "insert into product_pdbc values(%s,%s,%s,%s,%s)"
            cursor.execute(query,(pid,pname,category,price,quantity))
            conn.commit()
            print("Product Inserted Successfully")

        case 2:
            cursor.execute("Select * from product_pdbc")
            for rows in  cursor.fetchall():
                print(rows)

        case 3:
            name = input("Enter Product name")
            query = "select * from product_pdbc where pname like %s"
            cursor.execute(query,("%"+name+"%",))
            print("Matching Products")
            for rows in  cursor.fetchall():
                    print(rows)

        case 4:
            id = int(input("Enter id "))
            price = float(input("Enter price"))
            query = "update product_pdbc set price = %s where pid = %s"
            cursor.execute(query,(price,id))
            print("Product Price updated successfully")

        case 5:
            id = int(input("Enter id "))
            query = "delete from product_pdbc where pid =%s"
            cursor.execute(query,(id,))
            conn.commit()

        case 6:
            category = input("Enter Category : ")
            query = "select * from product_pdbc where category = %s"
            cursor.execute(query,(category,))
            for row in cursor.fetchall():
                print(row)

        case 7 :
            name = input("Enter letter : ")
            query = "select * from product_pdbc where pname like %s"
            cursor.execute(query,("%"+ name + "%",))
            for row in cursor.fetchall():
                print(row)
        case 8 : 
            name = input("Enter letter : ")
            query = "select * from product_pdbc where pname like %s"
            cursor.execute(query,(name + "%",))
            for row in cursor.fetchall():
                print(row)
        case 9: 
            name = input("Enter letter : ")
            query = "select * from product_pdbc where pname like %s"
            cursor.execute(query,("%"+ name,))
            for row in cursor.fetchall():
                print(row)

        case 10:
            price = int(input("Enter price : "))
            query = "select * from product_pdbc where price > %s"
            cursor.execute(query,(price,))
            for row in cursor.fetchall():
                print(row)

        case 11:
            quantity = int(input("Enter quantity : "))
            query = "select * from product_pdbc where quantity < %s"
            cursor.execute(query,(quantity,))
            for row in cursor.fetchall():
                print(row)

        case 12:
            quantity = int(input("Enter Quantity : "))
            pid = int(input("Enter ID : "))
            query = "update product_pdbc set quantity = %s where pid = %s"
            cursor.execute(query,(quantity,pid))
            conn.commit()
        
        case 13:
            category = input("Enter Quantity : ")
            pid = int(input("Enter ID : "))
            query = "update product_pdbc set category = %s where pid = %s"
            cursor.execute(query,(category,pid))
            conn.commit()     

        case 14:
            pid = int(input("Enter ID : "))
            query = "delete from product_pdbc where pid = %s"
            cursor.execute(query,(pid,))
            conn.commit()

        case 15:
            name = input("Enter letter : ")
            query = "select * from product_pdbc where category like %s"
            cursor.execute(query,("%"+ name + "%",))
            for row in cursor.fetchall():
                print(row)

        case 16:
            price = int(input("Enter price : "))
            query = "select * from product_pdbc where price <= %s"
            cursor.execute(query,(price,))
            for r in cursor.fetchall():
                print(r)

        case 17:
            print("Thank you for using Product Management System.")
            break

