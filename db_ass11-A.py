"""
ASSIGNMENT 1: STUDENT MANAGEMENT SYSTEM
=======================================

-------
A coaching institute wants to manage student records using
Python Database Connectivity (PDBC).

TABLE STRUCTURE
===============

Table Name: student_pdbc

Column       Data Type
--------------------------------
sid          INT PRIMARY KEY
sname        VARCHAR(50)
course       VARCHAR(50)
fees         DECIMAL(10,2)
city         VARCHAR(30)


SAMPLE DATA
===========

sid   sname    course    fees       city
------------------------------------------------
101   Amit     Python    15000.00   Indore
102   Priya    Java      18000.00   Bhopal
103   Rahul    Python    15000.00   Indore
104   Neha     Java      18000.00   Ujjain
105   Karan    MERN      20000.00   Indore


MENU
====

===== STUDENT MANAGEMENT SYSTEM =====
1. Add Student
2. Display All Students
3. Search Student by Name
4. Update Student Fees
5. Delete Student
6. Exit

Enter your choice:


TASK 1: ADD STUDENT
===================

INPUT
-----
Enter your choice: 1
Enter Student ID: 106
Enter Student Name: Anjali
Enter Course: Python
Enter Fees: 15000
Enter City: Dewas

OUTPUT
------
Student inserted successfully.


TASK 2: DISPLAY ALL STUDENTS
============================

INPUT
-----
Enter your choice: 2

OUTPUT
------
ID    Name      Course    Fees       City
------------------------------------------------
101   Amit      Python    15000.00   Indore
102   Priya     Java      18000.00   Bhopal
103   Rahul     Python    15000.00   Indore
104   Neha      Java      18000.00   Ujjain
105   Karan     MERN      20000.00   Indore
106   Anjali    Python    15000.00   Dewas


TASK 3: SEARCH STUDENT BY NAME USING LIKE
=========================================

INPUT
-----
Enter your choice: 3
Enter name to search: an

OUTPUT
------
Matching students:

ID    Name      Course    Fees       City
------------------------------------------------
105   Karan     MERN      20000.00   Indore
106   Anjali    Python    15000.00   Dewas

NOTE
----
Use a parameterized query with:
WHERE sname LIKE %s

Pass the search pattern:
'%' + search_name + '%'


TASK 4: UPDATE STUDENT FEES
===========================

INPUT
-----
Enter your choice: 4
Enter Student ID: 101
Enter New Fees: 17000

OUTPUT
------
Student fees updated successfully.


TASK 5: DELETE STUDENT
======================

INPUT
-----
Enter your choice: 5
Enter Student ID: 104

OUTPUT
------
Student deleted successfully.


TASK 6: EXIT
============

INPUT
-----
Enter your choice: 6

OUTPUT
------
Thank you for using Student Management System.
"""
"""

mysql> create table student_pdbc(sid int primary key,sname varchar(50),course varchar(50),fees decimal(10,2),city varchar(30));
Query OK, 0 rows affected (0.15 sec)

mysql> desc student_pdbc;
+--------+---------------+------+-----+---------+-------+
| Field  | Type          | Null | Key | Default | Extra |
+--------+---------------+------+-----+---------+-------+
| sid    | int           | NO   | PRI | NULL    |       |
| sname  | varchar(50)   | YES  |     | NULL    |       |
| course | varchar(50)   | YES  |     | NULL    |       |
| fees   | decimal(10,2) | YES  |     | NULL    |       |
| city   | varchar(30)   | YES  |     | NULL    |       |
+--------+---------------+------+-----+---------+-------+
5 rows in set (0.06 sec)

mysql> insert into student_pdbc values(101,"amit","python",15000,"indore")
    -> ,(102,"priya","java",18000,"bhopal"),
    -> (103,"rahul","python",15000,"indore"),
    -> (104,"neha","java",18000,"ujjain"),
    -> (105,"karan","mern",20000,"indore");
Query OK, 5 rows affected (0.02 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> select * from student_pdbc;
+-----+-------+--------+----------+--------+
| sid | sname | course | fees     | city   |
+-----+-------+--------+----------+--------+
| 101 | amit  | python | 15000.00 | indore |
| 102 | priya | java   | 18000.00 | bhopal |
| 103 | rahul | python | 15000.00 | indore |
| 104 | neha  | java   | 18000.00 | ujjain |
| 105 | karan | mern   | 20000.00 | indore |
+-----+-------+--------+----------+--------+
5 rows in set (0.01 sec)

"""

print(" welcome to student_pdbc")

import mysql.connector
conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
cursor=conn.cursor()



while True:
   print(" 1. Add Student")
   print("2. Display All Students")
   print("3. Search Student by Name")
   print("4. Update Student Fees")
   print("5. Delete Student")
   print("6. Exit")

   ch=int(input("enter your choice::"))
   match ch:
      case 1:
         sid=int(input("enter your id :"))
         sname=input("enter your name :")
         course=input("enter your course :")
         fees=float(input("enter your fees :"))
         city=input("enter your city :")

         query="insert into student_pdbc values(%s,%s,%s,%s,%s)"
         cursor.execute(query, (sid, sname, course, fees, city))
         conn.commit()
         print("data inserted successfully...")

         conn.close()
         print("==========================")
      case 2:
         query="select * from student_pdbc"
         cursor.execute(query)
         for row in cursor.fetchall():
            print(row)
         conn.close()
         print("============================")
      case 3:
         name=input("enter search name  :")
         query="select * from student_pdbc where sname like %s"
         cursor.execute(query, ("%"+name+"%",))
         for row in cursor.fetchall():
            print(row)
         conn.close()
      case 4:
         sid=int(input("enter student id :"))
         fees=float(input("enter new fees :"))
         query="update student_pdbc set fees=%s where sid=%s"
         cursor.execute(query, (fees,sid))
         conn.commit()
         print("updated successfully...")
         conn.close()
      case 5:
         sid=int(input("enter your id :"))
         query="delete from student_pdbc where sid=%s"
         cursor.execute(query,(sid,))
         conn.commit()
         print("deleted successfully...")
         conn.close()
      case 6:
         print("Thank you for using Student Management System.")
         break
         
         







         














