
# import connector

"""
import mysql.connector
print("hooo gya")
try:
   conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="********",database="batch18")
   print("hoooooooo gaye  reee")
   if conn.is_connected():
      print("connection established ")
except Exception as e:
   print("something went wrong ",e)     
finally:
   print("inside finally block")
   conn.close()
   print("connection closed successgully")

"""
# if we choose wrong database

"""
import mysql.connector
print("hooo gya")
try:
   connection=mysql.connector.connect(host="localhost",port=3306,user="root",password="********",database="batch8")
   print("hoooooooo gaye  reee")
   
except Exception as e:
   print("something went wrong ",e)     

output--

hooo gya
something went wrong  1049 (42000): Unknown database 'batch8'
"""

# table created using python
"""
import mysql.connector
print("hooo gya")
try:
   conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
   print("hoooooooo gaye  reee")
   if conn.is_connected():
      print("connection established ")
   cursor=conn.cursor()
   query="create table pdemployee1 (empid int primary key,empname varchar(50), salary decimal(10,2))"
   cursor.execute(query)
   print("areeee table also create ........")
   
except Exception as e:
   print("something went wrong ",e)     
finally:
   print("inside finally block")
   conn.close()
   print("connection closed successgully")

"""
# insert value in table 

"""
import mysql.connector
print("hooo gya")
try:
   conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
   print("hoooooooo gaye  reee")
   if conn.is_connected():
      print("connection established ")
   cursor=conn.cursor()
   query="insert into pdemployee1 values (1,"depuu",5000),(2,"rashmika",20000)"
             
   cursor.execute(query)
   print("insert data in our table  ........")
   conn.commit()
except Exception as e:
   print("something went wrong ",e)     
finally:
   print("inside finally block")
   conn.close()
   print("connection closed successgully")
   """

# exwecute many--

"""
import mysql.connector
print("hooo gya")
try:
   conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
   print("hoooooooo gaye  reee")
   if conn.is_connected():
      print("connection established ")
   cursor=conn.cursor()
   query="insert into pdemployee1(empid,empname,salary) values(%s,%s,%s)"
   data=[(101,"deepika",5000),(102,"rashmika",7000),(103,"virat",70551)]
   cursor.executemany(query,data)
   conn.commit()
   print("record insert successfully")


except Exception as e:
   print("something went wrong ",e)     
finally:
   print("inside finally block")
   conn.close()
   print("connection closed successgully")
   
"""
#@read data from user


"""
import mysql.connector
print("hooo gya")
try:
   conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
   print("hoooooooo gaye  reee")
   if conn.is_connected():
      print("connection established ")
 
   cursor=conn.cursor()
   query="insert into pdemployee1(empid,empname,salary) values(%s,%s,%s)"
   n=int(input("enter no of records "))
   data=[]
   for i in range(n):
         print("enter detail")
         empid=int(input("enter empid :"))
         empname=input("enter empname :")
         salary=float(input("enter salary: "))
         data.append((empid,empname,salary))
   cursor.executemany(query,data)
   conn.commit()
   print("record insert successfully")


except Exception as e:
   print("something went wrong ",e)     
finally:
   print("inside finally block")
   conn.close()
   print("connection closed successgully")
   
"""

#@# fetch data from database--
"""
import mysql.connector
print("hooo gya")
try:
   conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
   print("hoooooooo gaye  reee")
   if conn.is_connected():
      print("connection established ")
 
   cursor=conn.cursor()
   cursor.execute("select * from pdemployee1")
   print("using fetchone")
   print(cursor.fetchall())
  



except Exception as e:
   print("something went wrong ",e)     
finally:
   print("inside finally block")
   conn.close()
   print("connection closed successgully")
   """

"""
import mysql.connector
print("hooo gya")
try:
   conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
   print("hoooooooo gaye  reee")
   if conn.is_connected():
      print("connection established ")
 
   cursor=conn.cursor()
   cursor.execute("select * from pdemployee1")
   for row in cursor:
      print(row)



except Exception as e:
   print("something went wrong ",e)     
finally:
   print("inside finally block")
   conn.close()
   print("connection closed successgully")

   """

#@ acess column values
"""
import mysql.connector
print("hooo gya")
try:
   conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
   print("hoooooooo gaye  reee")
   if conn.is_connected():
      print("connection established ")
 
   cursor=conn.cursor()
   cursor.execute("select * from pdemployee1")
   for row in cursor:
      print(row[0])
      print(row[1])



except Exception as e:
   print("something went wrong ",e)     
finally:
   print("inside finally block")
   conn.close()
   print("connection closed successgully")
   """

# using dictionary cursor
"""
import mysql.connector
print("hooo gya")
try:
   conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
   print("hoooooooo gaye  reee")
   if conn.is_connected():
      print("connection established ")
 
   cursor=conn.cursor(dictionary=True)
   cursor.execute("select * from pdemployee1")
   row=cursor.fetchall()
   print(row)
   print(row["name"])



except Exception as e:
   print("something went wrong ",e)     
finally:
   print("inside finally block")
   conn.close()
   print("connection closed successgully")
"""


# waq to give employee whos salary is reater than 50000

"""
import mysql.connector
print("hooo gya")
try:
   conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
   print("hoooooooo gaye  reee")
   if conn.is_connected():
      print("connection established ")
 
   cursor=conn.cursor(dictionary=True)
   cursor.execute("select * from pdemployee1 where salary >50000")
   for row in cursor:
      print(row)


except Exception as e:
   print("something went wrong ",e)     
finally:
   print("inside finally block")
   conn.close()
   print("connection closed successgully")
   """

# waqto fetch and cound all records 
"""
import mysql.connector
print("hooo gya")
try:
   conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
   print("hoooooooo gaye  reee")
   if conn.is_connected():
      print("connection established ")
 
   cursor=conn.cursor(dictionary=True)
   cursor.execute("select * from pdemployee1 ")
   row=cursor.fetchall()
   print(len(row))
  


except Exception as e:
   print("something went wrong ",e)     
finally:
   print("inside finally block")
   conn.close()
   print("connection closed successgully")

# waq to display employee details whose name is taken from user
"""

"""
import mysql.connector
print("hooo gya")
try:
   conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
   print("hoooooooo gaye  reee")
   if conn.is_connected():
      print("connection established ")
   cursor=conn.cursor()
   name=int(input("enter name "))
   query="select * from pdemployee1 where name='"+name+"'"
   cursor.execute(query)
   row=cursor.fetchall()
   print(row)
   
 

except Exception as e:
   print("something went wrong ",e)     
finally:
   print("inside finally block")
   conn.close()
   print("connection closed successgully")


"""

"""
import mysql.connector
print("hooo gya")
try:
   conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
   print("hoooooooo gaye  reee")
   if conn.is_connected():
      print("connection established ")
   cursor=conn.cursor()
   name=input("enter name ")
   query="select * from pdemployee1 where empname=%s "
   cursor.execute(query,(name,))
   row=cursor.fetchall()
   print(row)
   
 

except Exception as e:
   print("something went wrong ",e)     
finally:
   print("inside finally block")
   conn.close()
   print("connection closed successgully")

   """

#write a query to read name and salary from user and fetch that record.
"""

import mysql.connector

conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
cursor=conn.cursor()
name=input("enter name")
salary=float(input("enter salary"))
query="select * from pdemployee1 where empname=%s and salary>%s"
cursor.execute(query,(empname,salary))

for row in cursor.fetchall():
    print(row)
conn.close()

"""

# dynamic insert-
"""

import mysql.connector

conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
cursor=conn.cursor()
empid=int(input("enter id"))
empname=input("enter name")
salary=float(input("enter salary"))
query="insert into pdemployee1(empid,empname,salary) values(%s,%s,%s)"
cursor.execute(query,(empid,empname,salary))
conn.commit()
print("data insert ")
conn.close()

"""

#waq to update salary of employee based on id 
"""
import mysql.connector

conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
cursor=conn.cursor()
empid=int(input("enter id"))

salary=float(input("enter salary"))
query="update pdemployee1 set salary=%s where empid=%s"
cursor.execute(query,(salary,empid))
conn.commit()
print("data updated ")
conn.close()

"""


#waq to delete an employee based on id

"""
import mysql.connector

conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
cursor=conn.cursor()
empid=int(input("enter id"))


query="delete from  pdemployee1 where empid=%s"
cursor.execute(query,(empid,))
conn.commit()
print("data deleted ")
conn.close()
"""

# dynamic qury with like 

"""
import mysql.connector

conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
cursor=conn.cursor()
name=input("enter name")


query="select * from  pdemployee1 where empname like %s"
cursor.execute(query,(name+"%",))
for row in cursor.fetchall():
    print(row)
conn.close()

"""
# --> find employee using last letter

"""
import mysql.connector

conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
cursor=conn.cursor()
name=input("enter name")


query="select * from  pdemployee1 where empname like %s"
cursor.execute(query,("%"+name,))
for row in cursor.fetchall():
    print(row)
conn.close()
"""
"""
import mysql.connector

conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
cursor=conn.cursor()
name=input("enter name")


query="select * from  pdemployee1 where empname like %s"
cursor.execute(query,("%"+name+"%",))
for row in cursor.fetchall():
    print(row)
conn.close()

"""
"""

import mysql.connector

conn=mysql.connector.connect(host="localhost",port=3306,user="root",password="password",database="batch18")
cursor=conn.cursor()
ids=[101,102,104]

query="select * from pdemployee1 where enpid in (%s,%s,%s)"
cursor.execute(query,tuple(ids))
for row in cursor.fetchall():
    print(row)
conn.close()
"""



