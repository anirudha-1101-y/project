ASSIGNMENT 1 – STUDENT MANAGEMENT SYSTEM

Q1. Create a database named school_db and use the database.

Q2. Create a table named student with:
- student_id – INT, PRIMARY KEY, AUTO_INCREMENT
- student_name – VARCHAR(50)
- age – INT
- course – VARCHAR(50)
- city – VARCHAR(50)
- marks – INT

Q3. Insert the following 10 student records:

student_name | age | course | city | marks
Rahul Sharma | 21 | Python | Indore | 85
Priya Verma | 22 | Java | Bhopal | 78
Amit Singh | 20 | Python | Indore | 92
Neha Patel | 23 | Java | Pune | 81
Rohit Mehta | 21 | Python | Mumbai | 88
Sneha Jain | 22 | Java | Indore | 76
Karan Gupta | 20 | Python | Delhi | 95
Pooja Mishra | 23 | Java | Bhopal | 84
Ankit Tiwari | 21 | Python | Pune | 79
Riya Kapoor | 22 | Java | Mumbai | 91

Q4. Display the structure of the student table using DESC.

Q5. Display all records from the student table.
===============================================================================================
"""
mysql> use school_db;
Database changed
mysql> create table student(student_id int auto_increment primary key,student_name varchar(50),age int,course varchar(50),city varchar(50),marks int);
Query OK, 0 rows affected (0.03 sec)
# question ---1

mysql> desc student;
+--------------+-------------+------+-----+---------+----------------+
| Field        | Type        | Null | Key | Default | Extra          |
+--------------+-------------+------+-----+---------+----------------+
| student_id   | int         | NO   | PRI | NULL    | auto_increment |
| student_name | varchar(50) | YES  |     | NULL    |                |
| age          | int         | YES  |     | NULL    |                |
| course       | varchar(50) | YES  |     | NULL    |                |
| city         | varchar(50) | YES  |     | NULL    |                |
| marks        | int         | YES  |     | NULL    |                |
+--------------+-------------+------+-----+---------+----------------+
6 rows in set (0.01 sec)


question--2




mysql> insert into student(student_name,age,course,city,marks) values("rahul",21,"python","indore",85),("priya",22,"Java","Bhopal",78),("amit",20,"python","indore",92),("neha",23,"java","pune",81),("rohit",21,"pyhton","mumbai",88),("sneha",22,"java","indore",76),("karan",20,"python","delhi",95),("pooja",22,"java","bhopal",84),("ankit",21,"python","pune",79),("riya",22,"java","mumbai",91);
Query OK, 10 rows affected (0.01 sec)
Records: 10  Duplicates: 0  Warnings: 0

mysql> select * from student;
+------------+--------------+------+--------+--------+-------+
| student_id | student_name | age  | course | city   | marks |
+------------+--------------+------+--------+--------+-------+
|          1 | rahul        |   21 | python | indore |    85 |
|          2 | priya        |   22 | Java   | Bhopal |    78 |
|          3 | amit         |   20 | python | indore |    92 |
|          4 | neha         |   23 | java   | pune   |    81 |
|          5 | rohit        |   21 | pyhton | mumbai |    88 |
|          6 | sneha        |   22 | java   | indore |    76 |
|          7 | karan        |   20 | python | delhi  |    95 |
|          8 | pooja        |   22 | java   | bhopal |    84 |
|          9 | ankit        |   21 | python | pune   |    79 |
|         10 | riya         |   22 | java   | mumbai |    91 |
+------------+--------------+------+--------+--------+-------+
10 rows in set (0.00 sec)

mysql>


===============================================================================================
ASSIGNMENT 2 – EMPLOYEE MANAGEMENT SYSTEM

Q1. Create a database named company_db and use the database.

Q2. Create a table named employee with:
- employee_id – INT, PRIMARY KEY, AUTO_INCREMENT
- employee_name – VARCHAR(50)
- age – INT
- department – VARCHAR(50)
- designation – VARCHAR(50)
- salary – INT

Q3. Insert the following 10 employee records:

employee_name | age | department | designation | salary
Rahul Sharma | 28 | IT | Developer | 55000
Priya Verma | 26 | HR | Executive | 42000
Amit Singh | 30 | IT | Team Lead | 75000
Neha Patel | 27 | Finance | Accountant | 48000
Rohit Mehta | 32 | IT | Manager | 90000
Sneha Jain | 25 | Marketing | Executive | 40000
Karan Gupta | 29 | IT | Developer | 60000
Pooja Mishra | 31 | HR | Manager | 80000
Ankit Tiwari | 28 | Finance | Analyst | 65000
Riya Kapoor | 27 | Marketing | Manager | 70000

Q4. Display the structure of the employee table using DESC.

Q5. Display all records from the employee table.

===========================================================================================

mysql> create database company_db;
Query OK, 1 row affected (0.01 sec)

mysql> use company_db;
Database changed
mysql> create table employee(employee_id int primary key auto_increment,employee_name varchar(50),age int,department varchar(50),designation varchar(50),salary int);
Query OK, 0 rows affected (0.03 sec)

mysql> desc employee;
+---------------+-------------+------+-----+---------+----------------+
| Field         | Type        | Null | Key | Default | Extra          |
+---------------+-------------+------+-----+---------+----------------+
| employee_id   | int         | NO   | PRI | NULL    | auto_increment |
| employee_name | varchar(50) | YES  |     | NULL    |                |
| age           | int         | YES  |     | NULL    |                |
| department    | varchar(50) | YES  |     | NULL    |                |
| designation   | varchar(50) | YES  |     | NULL    |                |
| salary        | int         | YES  |     | NULL    |                |
+---------------+-------------+------+-----+---------+----------------+
6 rows in set (0.01 sec)

mysql> insert into employee(employee_name,age,department,designation,salary) values ("rahul",28,"it","developer",55000),("priya",26,"hr","executive",42000),("amit",30,"it","team lead",75000),("neha",27,"finanace","account",48000),("rohit",32,"it","manager",9000),("sneha",25,"marketing","executive",40000),("karan",29,"it","developer",60000),("pooja",31,"hr","manager",80000),("ankit",28,"finanace","analyst",65000),("riya",27,"marketing","manager",70000);
Query OK, 10 rows affected (0.01 sec)
Records: 10  Duplicates: 0  Warnings: 0

mysql> desc employee;
+---------------+-------------+------+-----+---------+----------------+
| Field         | Type        | Null | Key | Default | Extra          |
+---------------+-------------+------+-----+---------+----------------+
| employee_id   | int         | NO   | PRI | NULL    | auto_increment |
| employee_name | varchar(50) | YES  |     | NULL    |                |
| age           | int         | YES  |     | NULL    |                |
| department    | varchar(50) | YES  |     | NULL    |                |
| designation   | varchar(50) | YES  |     | NULL    |                |
| salary        | int         | YES  |     | NULL    |                |
+---------------+-------------+------+-----+---------+----------------+
6 rows in set (0.00 sec)

mysql> select * from employee;
+-------------+---------------+------+------------+-------------+--------+
| employee_id | employee_name | age  | department | designation | salary |
+-------------+---------------+------+------------+-------------+--------+
|           1 | rahul         |   28 | it         | developer   |  55000 |
|           2 | priya         |   26 | hr         | executive   |  42000 |
|           3 | amit          |   30 | it         | team lead   |  75000 |
|           4 | neha          |   27 | finanace   | account     |  48000 |
|           5 | rohit         |   32 | it         | manager     |   9000 |
|           6 | sneha         |   25 | marketing  | executive   |  40000 |
|           7 | karan         |   29 | it         | developer   |  60000 |
|           8 | pooja         |   31 | hr         | manager     |  80000 |
|           9 | ankit         |   28 | finanace   | analyst     |  65000 |
|          10 | riya          |   27 | marketing  | manager     |  70000 |
+-------------+---------------+------+------------+-------------+--------+
10 rows in set (0.00 sec)




================================================================================
ASSIGNMENT 3 – PRODUCT MANAGEMENT SYSTEM

Q1. Create a database named shop_db and use the database.

Q2. Create a table named product with:
- product_id – INT, PRIMARY KEY, AUTO_INCREMENT
- product_name – VARCHAR(50)
- category – VARCHAR(50)
- brand – VARCHAR(50)
- price – INT
- quantity – INT

Q3. Insert the following 10 product records:

product_name | category | brand | price | quantity
Laptop | Electronics | Dell | 55000 | 10
Smartphone | Electronics | Samsung | 25000 | 15
Keyboard | Accessories | Logitech | 1500 | 25
Mouse | Accessories | HP | 800 | 30
Monitor | Electronics | LG | 18000 | 12
Headphones | Accessories | Sony | 3000 | 20
Printer | Electronics | Canon | 12000 | 8
Tablet | Electronics | Lenovo | 22000 | 14
Webcam | Accessories | Logitech | 2500 | 18
Speaker | Accessories | JBL | 4500 | 16

Q4. Display the structure of the product table using DESC.

Q5. Display all records from the product table.
--------------------------------------------------------------------------------
mysql> create database shop_db;
Query OK, 1 row affected (0.01 sec)



mysql> use shop_db;
Database changed
mysql> create table product(product_id int primary key auto_increment,product_name varchar(50),category varchar(50),brand varchar(50),price int,quantity int);


mysql> insert into product(product_name,category,brand,price,quantity) values ("laptop","electronic","dell",55000,10),("smartphone","electronic","samung",25000,15),("keyboard","accessories","hp",800,30),("mouse","accessories","logitech",800,30),("monitor","electronic","lg",18000,12),("printer","electronic","lg",12000,8),("tablet","electronic","lenevo",22000,14),("webcam","accessories","logitech",2500,18),("speaker","accessories","jbl",4500,16);
Query OK, 9 rows affected (0.01 sec)
Records: 9  Duplicates: 0  Warnings: 0

mysql> desc product;
+--------------+-------------+------+-----+---------+----------------+
| Field        | Type        | Null | Key | Default | Extra          |
+--------------+-------------+------+-----+---------+----------------+
| product_id   | int         | NO   | PRI | NULL    | auto_increment |
| product_name | varchar(50) | YES  |     | NULL    |                |
| category     | varchar(50) | YES  |     | NULL    |                |
| brand        | varchar(50) | YES  |     | NULL    |                |
| price        | int         | YES  |     | NULL    |                |
| quantity     | int         | YES  |     | NULL    |                |
+--------------+-------------+------+-----+---------+----------------+
6 rows in set (0.00 sec)

mysql> select * from product;
+------------+--------------+-------------+----------+-------+----------+
| product_id | product_name | category    | brand    | price | quantity |
+------------+--------------+-------------+----------+-------+----------+
|          1 | laptop       | electronic  | dell     | 55000 |       10 |
|          2 | smartphone   | electronic  | samung   | 25000 |       15 |
|          3 | keyboard     | accessories | hp       |   800 |       30 |
|          4 | mouse        | accessories | logitech |   800 |       30 |
|          5 | monitor      | electronic  | lg       | 18000 |       12 |
|          6 | printer      | electronic  | lg       | 12000 |        8 |
|          7 | tablet       | electronic  | lenevo   | 22000 |       14 |
|          8 | webcam       | accessories | logitech |  2500 |       18 |
|          9 | speaker      | accessories | jbl      |  4500 |       16 |
+------------+--------------+-------------+----------+-------+----------+
9 rows in set (0.00 sec)

=================================================================================

#
You are developing a Student Management System for your coaching institute.

Write SQL commands to perform the following complete task:

Create a database named coaching.
Select the database.
Create a table named student.
The table must contain columns for student ID, name, age, mobile number, date of birth, city, and email.
Insert 3 student records in a single command.
Insert another student using INSERT IGNORE.
Add a salary column to the table.
Change the size of the name column.
Change the name of the mobile number column.
Rename the email column.
Remove the salary column.
Insert one more student with a date of birth.
Make the student ID automatically generate values.
Display the structure of the table.
Display all records from the table.

Write all the SQL commands yourself in the correct order.



mysql> create table student(id int,name varchar(20),age int,mobile_no varchar(15),DOB date,city varchar(20),email varchar(20));
Query OK, 0 rows affected (0.03 sec)

mysql> insert into student(id,name,age,mobile_no,email) values(101,"anirudha",21,9516401101,"anirudha@"),(102,"dhruv",22,8839216943,"dhruv@"),(103,"devendra",23,8839216943,"dev@");
Query OK, 3 rows affected (0.01 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> desc student;
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| id        | int         | YES  |     | NULL    |       |
| name      | varchar(20) | YES  |     | NULL    |       |
| age       | int         | YES  |     | NULL    |       |
| mobile_no | varchar(15) | YES  |     | NULL    |       |
| DOB       | date        | YES  |     | NULL    |       |
| city      | varchar(20) | YES  |     | NULL    |       |
| email     | varchar(20) | YES  |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
7 rows in set (0.00 sec)

mysql> select * from student;
+------+----------+------+------------+------+------+-----------+
| id   | name     | age  | mobile_no  | DOB  | city | email     |
+------+----------+------+------------+------+------+-----------+
|  101 | anirudha |   21 | 9516401101 | NULL | NULL | anirudha@ |
|  102 | dhruv    |   22 | 8839216943 | NULL | NULL | dhruv@    |
|  103 | devendra |   23 | 8839216943 | NULL | NULL | dev@      |
+------+----------+------+------------+------+------+-----------+
3 rows in set (0.00 sec)

mysql> alter table modify column id int primary key auto_increment;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'column id int primary key auto_increment' at line 1
mysql> alter table student modify column id int primary key auto_increment;
Query OK, 3 rows affected (0.07 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> desc student;
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| id        | int         | NO   | PRI | NULL    | auto_increment |
| name      | varchar(20) | YES  |     | NULL    |                |
| age       | int         | YES  |     | NULL    |                |
| mobile_no | varchar(15) | YES  |     | NULL    |                |
| DOB       | date        | YES  |     | NULL    |                |
| city      | varchar(20) | YES  |     | NULL    |                |
| email     | varchar(20) | YES  |     | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
7 rows in set (0.00 sec)

mysql> insert ignore into student(id,name,age) values(102,"virat",23);
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> select * from student;
+-----+----------+------+------------+------+------+-----------+
| id  | name     | age  | mobile_no  | DOB  | city | email     |
+-----+----------+------+------------+------+------+-----------+
| 101 | anirudha |   21 | 9516401101 | NULL | NULL | anirudha@ |
| 102 | dhruv    |   22 | 8839216943 | NULL | NULL | dhruv@    |
| 103 | devendra |   23 | 8839216943 | NULL | NULL | dev@      |
+-----+----------+------+------------+------+------+-----------+
3 rows in set (0.00 sec)

mysql> alter table student add column salary decimal(10,2);
Query OK, 0 rows affected (0.03 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc student;
+-----------+---------------+------+-----+---------+----------------+
| Field     | Type          | Null | Key | Default | Extra          |
+-----------+---------------+------+-----+---------+----------------+
| id        | int           | NO   | PRI | NULL    | auto_increment |
| name      | varchar(20)   | YES  |     | NULL    |                |
| age       | int           | YES  |     | NULL    |                |
| mobile_no | varchar(15)   | YES  |     | NULL    |                |
| DOB       | date          | YES  |     | NULL    |                |
| city      | varchar(20)   | YES  |     | NULL    |                |
| email     | varchar(20)   | YES  |     | NULL    |                |
| salary    | decimal(10,2) | YES  |     | NULL    |                |
+-----------+---------------+------+-----+---------+----------------+
8 rows in set (0.00 sec)

mysql> alter table student modify column name varchar(50);
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc student;
+-----------+---------------+------+-----+---------+----------------+
| Field     | Type          | Null | Key | Default | Extra          |
+-----------+---------------+------+-----+---------+----------------+
| id        | int           | NO   | PRI | NULL    | auto_increment |
| name      | varchar(50)   | YES  |     | NULL    |                |
| age       | int           | YES  |     | NULL    |                |
| mobile_no | varchar(15)   | YES  |     | NULL    |                |
| DOB       | date          | YES  |     | NULL    |                |
| city      | varchar(20)   | YES  |     | NULL    |                |
| email     | varchar(20)   | YES  |     | NULL    |                |
| salary    | decimal(10,2) | YES  |     | NULL    |                |
+-----------+---------------+------+-----+---------+----------------+
8 rows in set (0.00 sec)

mysql> alter table student change mobile_no mobile;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
mysql> alter table student change mobile_no mobile varchar(20);
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc student;
+--------+---------------+------+-----+---------+----------------+
| Field  | Type          | Null | Key | Default | Extra          |
+--------+---------------+------+-----+---------+----------------+
| id     | int           | NO   | PRI | NULL    | auto_increment |
| name   | varchar(50)   | YES  |     | NULL    |                |
| age    | int           | YES  |     | NULL    |                |
| mobile | varchar(20)   | YES  |     | NULL    |                |
| DOB    | date          | YES  |     | NULL    |                |
| city   | varchar(20)   | YES  |     | NULL    |                |
| email  | varchar(20)   | YES  |     | NULL    |                |
| salary | decimal(10,2) | YES  |     | NULL    |                |
+--------+---------------+------+-----+---------+----------------+
8 rows in set (0.01 sec)

mysql> alter table student rename column email to emaill;
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc student;
+--------+---------------+------+-----+---------+----------------+
| Field  | Type          | Null | Key | Default | Extra          |
+--------+---------------+------+-----+---------+----------------+
| id     | int           | NO   | PRI | NULL    | auto_increment |
| name   | varchar(50)   | YES  |     | NULL    |                |
| age    | int           | YES  |     | NULL    |                |
| mobile | varchar(20)   | YES  |     | NULL    |                |
| DOB    | date          | YES  |     | NULL    |                |
| city   | varchar(20)   | YES  |     | NULL    |                |
| emaill | varchar(20)   | YES  |     | NULL    |                |
| salary | decimal(10,2) | YES  |     | NULL    |                |
+--------+---------------+------+-----+---------+----------------+
8 rows in set (0.00 sec)

mysql> alter table student drop column salary;
Query OK, 0 rows affected (0.03 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc student;
+--------+-------------+------+-----+---------+----------------+
| Field  | Type        | Null | Key | Default | Extra          |
+--------+-------------+------+-----+---------+----------------+
| id     | int         | NO   | PRI | NULL    | auto_increment |
| name   | varchar(50) | YES  |     | NULL    |                |
| age    | int         | YES  |     | NULL    |                |
| mobile | varchar(20) | YES  |     | NULL    |                |
| DOB    | date        | YES  |     | NULL    |                |
| city   | varchar(20) | YES  |     | NULL    |                |
| emaill | varchar(20) | YES  |     | NULL    |                |
+--------+-------------+------+-----+---------+----------------+
7 rows in set (0.00 sec)

mysql> insert into student(name,DOB) values("mayank",1999-01-25);
ERROR 1292 (22007): Incorrect date value: '1973' for column 'DOB' at row 1
mysql> insert into student(name,DOB) values("mayank","1999-01-25");
Query OK, 1 row affected (0.01 sec)

mysql> desc student;
+--------+-------------+------+-----+---------+----------------+
| Field  | Type        | Null | Key | Default | Extra          |
+--------+-------------+------+-----+---------+----------------+
| id     | int         | NO   | PRI | NULL    | auto_increment |
| name   | varchar(50) | YES  |     | NULL    |                |
| age    | int         | YES  |     | NULL    |                |
| mobile | varchar(20) | YES  |     | NULL    |                |
| DOB    | date        | YES  |     | NULL    |                |
| city   | varchar(20) | YES  |     | NULL    |                |
| emaill | varchar(20) | YES  |     | NULL    |                |
+--------+-------------+------+-----+---------+----------------+
7 rows in set (0.00 sec)

mysql> select * from student;
+-----+----------+------+------------+------------+------+-----------+
| id  | name     | age  | mobile     | DOB        | city | emaill    |
+-----+----------+------+------------+------------+------+-----------+
| 101 | anirudha |   21 | 9516401101 | NULL       | NULL | anirudha@ |
| 102 | dhruv    |   22 | 8839216943 | NULL       | NULL | dhruv@    |
| 103 | devendra |   23 | 8839216943 | NULL       | NULL | dev@      |
| 104 | mayank   | NULL | NULL       | 1999-01-25 | NULL | NULL      |
+-----+----------+------+------------+------------+------+-----------+
4 rows in set (0.00 sec)

mysql> desc student;
+--------+-------------+------+-----+---------+----------------+
| Field  | Type        | Null | Key | Default | Extra          |
+--------+-------------+------+-----+---------+----------------+
| id     | int         | NO   | PRI | NULL    | auto_increment |
| name   | varchar(50) | YES  |     | NULL    |                |
| age    | int         | YES  |     | NULL    |                |
| mobile | varchar(20) | YES  |     | NULL    |                |
| DOB    | date        | YES  |     | NULL    |                |
| city   | varchar(20) | YES  |     | NULL    |                |
| emaill | varchar(20) | YES  |     | NULL    |                |
+--------+-------------+------+-----+---------+----------------+
7 rows in set (0.00 sec)

mysql> select * from student;
+-----+----------+------+------------+------------+------+-----------+
| id  | name     | age  | mobile     | DOB        | city | emaill    |
+-----+----------+------+------------+------------+------+-----------+
| 101 | anirudha |   21 | 9516401101 | NULL       | NULL | anirudha@ |
| 102 | dhruv    |   22 | 8839216943 | NULL       | NULL | dhruv@    |
| 103 | devendra |   23 | 8839216943 | NULL       | NULL | dev@      |
| 104 | mayank   | NULL | NULL       | 1999-01-25 | NULL | NULL      |
+-----+----------+------+------------+------------+------+-----------+
==================================================================================
practice question==

You are creating a College Student Management System. Complete the following task step-by-step using SQL commands.

Scenario

Create a database named college_db and create a table named student with these requirements:

The table should initially contain:
id
name
age
mobile
DOB
city
Insert 5 students in a single INSERT command.
One of the students should have a NULL value for city.
Add an email column using ALTER TABLE and place it after name.
Add a salary column using ALTER TABLE and place it after city.
Change the name column so that it can store up to 100 characters.
Rename mobile to mobile_no using CHANGE.
Rename DOB to date_of_birth using RENAME COLUMN.
Make id a Primary Key.
Make id AUTO_INCREMENT using ALTER TABLE.
Insert 2 more students without specifying id.
Try inserting a student with an already existing id using INSERT IGNORE.
Remove the salary column.
Rename the table from student to college_student.
Insert one more student into the renamed table with a valid date.
Display:
Table structure
All records
Finally, rename email to student_email.