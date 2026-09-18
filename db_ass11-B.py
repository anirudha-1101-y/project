"""
=========================================================
ASSIGNMENT 2: EMPLOYEE MANAGEMENT SYSTEM
=========================================================

--------
A company wants to maintain employee details, departments,
salaries, and cities using Python PDBC.

TABLE STRUCTURE
===============

Table Name: employee_pdbc

Column       Data Type
--------------------------------
eid          INT PRIMARY KEY
ename        VARCHAR(50)
department   VARCHAR(40)
salary       DECIMAL(10,2)
city         VARCHAR(30)


SAMPLE DATA
===========

eid   ename    department    salary      city
----------------------------------------------------
201   Amit     IT            45000.00    Indore
202   Priya    HR            40000.00    Bhopal
203   Rahul    IT            55000.00    Indore
204   Neha     Finance       50000.00    Ujjain
205   Karan    IT            60000.00    Indore


MENU
====

===== EMPLOYEE MANAGEMENT SYSTEM =====
1. Add Employee
2. Display All Employees
3. Search Employee by Name
4. Update Employee Salary
5. Delete Employee
6. Exit

Enter your choice:


TASK 1: ADD EMPLOYEE
====================

INPUT
-----
Enter your choice: 1
Enter Employee ID: 206
Enter Employee Name: Anjali
Enter Department: HR
Enter Salary: 42000
Enter City: Dewas

OUTPUT
------
Employee inserted successfully.


TASK 2: DISPLAY ALL EMPLOYEES
=============================

INPUT
-----
Enter your choice: 2

OUTPUT
------
ID    Name      Department    Salary      City
----------------------------------------------------
201   Amit      IT            45000.00    Indore
202   Priya     HR            40000.00    Bhopal
203   Rahul     IT            55000.00    Indore
204   Neha      Finance       50000.00    Ujjain
205   Karan     IT            60000.00    Indore
206   Anjali    HR            42000.00    Dewas


TASK 3: SEARCH EMPLOYEE BY NAME USING LIKE
==========================================

INPUT
-----
Enter your choice: 3
Enter name to search: ra

OUTPUT
------
Matching employees:

ID    Name      Department    Salary      City
----------------------------------------------------
203   Rahul     IT            55000.00    Indore
205   Karan     IT            60000.00    Indore

NOTE
----
Use:
WHERE ename LIKE %s

Pass:
'%' + search_name + '%'


TASK 4: UPDATE EMPLOYEE SALARY
=============================

INPUT
-----
Enter your choice: 4
Enter Employee ID: 201
Enter New Salary: 48000

OUTPUT
------
Employee salary updated successfully.


TASK 5: DELETE EMPLOYEE
=======================

INPUT
-----
Enter your choice: 5
Enter Employee ID: 202

OUTPUT
------
Employee deleted successfully.


TASK 6: EXIT
============

INPUT
-----
Enter your choice: 6

OUTPUT
------
Thank you for using Employee Management System.

"""

"""
mysql> create table employee_pdbc(eid int primary key,ename varchar(50),department varchar(40),salary decimal(10,2),city varchar(30));
Query OK, 0 rows affected (0.06 sec)

mysql> desc employee_pdbc;
+------------+---------------+------+-----+---------+-------+
| Field      | Type          | Null | Key | Default | Extra |
+------------+---------------+------+-----+---------+-------+
| eid        | int           | NO   | PRI | NULL    |       |
| ename      | varchar(50)   | YES  |     | NULL    |       |
| department | varchar(40)   | YES  |     | NULL    |       |
| salary     | decimal(10,2) | YES  |     | NULL    |       |
| city       | varchar(30)   | YES  |     | NULL    |       |
+------------+---------------+------+-----+---------+-------+
5 rows in set (0.01 sec)

mysql> INSERT INTO employee_pdbc (eid, ename, department, salary, city)
    -> VALUES
    -> (201, 'Amit', 'IT', 45000.00, 'Indore'),
    -> (202, 'Priya', 'HR', 40000.00, 'Bhopal'),
    -> (203, 'Rahul', 'IT', 55000.00, 'Indore'),
    -> (204, 'Neha', 'Finance', 50000.00, 'Ujjain'),
    -> (205, 'Karan', 'IT', 60000.00, 'Indore');
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select * from employee_pdbc;
+-----+-------+------------+----------+--------+
| eid | ename | department | salary   | city   |
+-----+-------+------------+----------+--------+
| 201 | Amit  | IT         | 45000.00 | Indore |
| 202 | Priya | HR         | 40000.00 | Bhopal |
| 203 | Rahul | IT         | 55000.00 | Indore |
| 204 | Neha  | Finance    | 50000.00 | Ujjain |
| 205 | Karan | IT         | 60000.00 | Indore |
+-----+-------+------------+----------+--------+

"""



import mysql.connector
conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
cursor=conn.cursor()

while True:
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Search Employee by Name")
    print("4. Update Employee Salary")
    print("5. Delete Employee")
    print("6. Exit")

    print()
    ch=int(input("enter your choice.."))
    match ch:
        case  1:
            eid=int(input("enter id :"))
            ename=input("enter employee name :")
            department=input("enter employee department :")
            salary=float(input("enter your salary :"))
            city=input("enter city :")

            query="insert into employee_pdbc values(%s,%s,%s,%s,%s)"
            cursor.execute(query ,(eid,ename,department,salary,city,))
            conn.commit()
            print("employee inserted ...")
            conn.close()
        case 2:
            query="select * from employee_pdbc"
            cursor.execute(query)
            for row in cursor.fetchall():
                print(row)
            conn.close()
        case 3:
            name=input("enter your name ")
            query="select * from employee_pdbc where ename like %s" 
            cursor.execute(query,("%"+name+"%",))
            for row in cursor.fetchall():
                print(row)
            conn.close()
        case 4:
            eid=int(input("enter employee id :"))
            salary=float(input("enter new salary :"))
            query="update employee_pdbc set salary=%s where eid=%s"
            cursor.execute(query, (salary,eid))
            conn.commit()
            print("updated employee successfull..")
            conn.close()
        case 5:
            eid=int(input("enter your id :"))
            query="delete from employee_pdbc where eid=%s"
            cursor.execute(query, (eid,))
            conn.commit()
            print("deleted successfully ..")
            conn.close()
        case 6:
            print("Thank you for using Employee Management System.")
            break
