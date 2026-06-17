"""
=====================================================================
QUESTION 1: EMPLOYEE SALARY ANALYSIS
====================================

A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

---

2. Display all employee details.

---

3. Find and display the employee with the highest salary.

---

4. Find and display the employee with the lowest salary.

---

5. Calculate and display the average salary of all employees.

---

6. Accept a department name from the user and display all employees belonging to that department.

---

Test Case:

Input:
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000
"""
"""
from collections import namedtuple
employee=namedtuple("employee",["emp_id","emp_name","department","salary"])
n=int(input("enter n: "))
emp=[]
for i in range(n):
    id=int(input("enter your id"))
    name=input("enter name")
    d=input("enter department ")
    s=int(input("enter salary"))
    emp.append(employee(id,name,d,s))

for i in emp:
    for j in i:
        print(j,end=" ")
    print()


#highets

print()
print("highest salary employee")
hs=0
hse=0
for i in range(len(emp)):
    if emp[i][3]>hs:
        hs=emp[i][3]
        hse=i
for j in range(len(emp[hse])):
    print(emp[hse][j],end=" ")

#lowest 
print()
print("lowesr salary employee")
ls=emp[0][3]
ise=0
for i in range(len(emp)): 
    if emp[i][3]<ls:
        ls=emp[i][j]
        ise=i
for j in range(len(emp[ise])):
    print(emp[ise][j],end=" ")
print()
print()
#avarage
sum=0
print()
for i in range(len(emp)):
    a=emp[i][3]
    sum=sum+a
print("avarage salary")
print("avarage",sum//len(emp))    

#department
d=input("enter your department: ")
print("employee in ",d,"department")
c=0
for i in range(len(emp)):
    a=emp[i][2]
    if a==d:
        for j in range(len(emp[i])):
            print(emp[i][j],end=" ")
        print()

"""
"""
QUESTION 2: STUDENT RESULT PROCESSING
=====================================

A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

---

2. Display all student details.

---

3. Find and display the topper of the class.

---

4. Count and display the number of students scoring above 80 marks.

---

5. Calculate and display the average marks.

---

6. Accept a course name from the user and display all students enrolled in that course.

---

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92
"""
"""
from collections import namedtuple
student=namedtuple("student",["roll_no","name","course","marks"])
n=int(input("enter no of stu"))

stu=[]
for i in range(n):
    rno=int(input("enter your roll no: "))
    n=input("enter your name ")
    c=input("enter your course name: ")
    m=float(input("enter your marks: "))
    stu.append(student(rno,n,c,m))

#display all rows
for i in stu:
    for j in i:
        print(j,end=" ")
    print()

#highest
print()
print("topper: ")
hs=0
hsi=0
for i in range(len(stu)):
    a=stu[i][3]
    if a>hs:
        hs=a
        hsi=i
for j in range(len(stu[hsi])):
    print(stu[hsi][j],end=" ")
print()
#above 80
c=0
for i in range(len(stu)):
    a=stu[i][3]
    if a>80:
        c=c+1
print("count above 80",c)

#avarage
sum=0
for i in range(len(stu)):
    a=stu[i][3]
    sum=sum+a
print("avarage marks",sum//len(stu))

#in same course
ec=input("enter course")
for i in range(len(stu)):
    a=stu[i][2]
    if a==ec:
        for j in range(len(stu[i])):
            print(stu[i][j],end=" ")
        print()

"""
"""
QUESTION 3: HOSPITAL PATIENT TRACKER
====================================

A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:

1. Read N patient records from the user and store them in a list of NamedTuples.

---

2. Display all patient details.

---

3. Display patients whose age is above 60 years.

---

4. Search for a patient using Patient ID.

---

5. Count the number of patients suffering from a particular disease.

---

Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2
"""
"""
from collections import namedtuple
n=int(input("enter patient count= "))
pat=namedtuple("patients",["patient_id","patients_name","age","disease"])
p=[]
for i in range(n):
    pid=int(input("enter patient id: "))
    name=input("enter patient name: ")
    age=int(input("enter patient age: "))
    dise=input("enter patient disease: ")
    p.append(pat(pid,name,age,dise))
for i in p:
    for j in i:
        print(j,end=" ")
    print()

#find patient 
f=int(input("enter finding id: "))
for i in range(len(p)):
    a=p[i][0]
    if f==a:
        for j in range(len(p[i])):
            print(p[i][j],end=" ")
        print()
#patient above 60
print("patient above age=60")
for i in range(len(p)):
    a=p[i][2]
    if a>=60:
        for j in range(len(p[i])):
            print(p[i][j], end=" ")
        
        print()
    
#with same disease
d=input("enter your disease")
for i in range(len(p)):
    a=p[i][3]
    if d==a:
        
    
        for j in range(len(p[i])):
            print(p[i][j],end=" ")

            
        print()
"""
"""
=====================================================================
QUESTION 4: ONLINE SHOPPING ORDERS
==================================

An online shopping company stores customer orders using NamedTuple.

Fields:
order_id, customer_name, product_name, amount

Requirements:

1. Read N order records from the user and store them in a list of NamedTuples.

---

2. Display all order details.

---

3. Find and display the order having the highest amount.

---

4. Calculate and display total sales.

---

5. Count the number of orders whose amount is greater than ₹10,000.

---

Test Case:

Input:
Enter number of orders: 5

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3
"""
"""
from collections import namedtuple
n=int(input("enter user "))
user=namedtuple("user",["order_id","customer_name","product_name","amount"])
sales=[]
for i in range(n):
    oid=int(input("Enter usre id "))
    n=input("Enter usre name ")
    p=input("Enter product name ")
    am=int(input("Enter mount "))
    sales.append(user(oid,n,p,am))
#display
for i in sales:
    for j in i:
        print(j,end=" ")
    print()
#highest
max=0
h=i
for i in range(len(sales)):
    a=sales[i][3]
    if max<a:
        max=a
        h=i
print("highest order value")
for j in range(len(sales[h])):
    print(sales[h][j],end=" ")
print()

#order above than 10000
print("order above 10000")
c=0
for i in range(len(sales)):
    a=sales[i][3]
    if a>10000:
        c=c+1
print(c)
"""
"""
=====================================================================
QUESTION 5: LIBRARY BOOK RECORDS
================================

A library maintains book information using NamedTuple.

Fields:
book_id, title, author, price

Requirements:

1. Read N book records from the user and store them in a list of NamedTuples.

---

2. Display all book details.

---

3. Find and display the most expensive book.

---

4. Search books by author name.

---

5. Calculate and display the average price of all books.

---

Test Case:

Input:
Enter number of books: 4

B101 Python Basics John 450
B102 Java Programming James 550
B103 Data Science John 700
B104 SQL Guide Smith 300

Enter Author Name: John

Expected Output:
Most Expensive Book:
B103 Data Science John 700

Average Book Price:
500.0

Books Written By John:
B101 Python Basics John 450
B103 Data Science John 70
"""
"""
from collections import namedtuple
n=int(input("enter no of book: "))
library=namedtuple("library",["book_id","title","author","price"])
book=[]
for i in range(n):
    bid=int(input("enter book id")) 
    bt=input("enter title")
    a=input("enput author ")
    p=int(input("enter price "))
    book.append(library(bid,bt,a,p))
for i in book:
    for j in i:
        print(j,end=" ")
    print()

#most expensive book
print("most expensive book:")
max=0
h=0
for i in range(len(book)):
    a=book[i][3]
    if max<a:
        max=a
        h=i

for j in range(len(book[h])):
    print(book[h][j],end=" ")

#avarage
print()
av=0
sum=0
for i in range(len(book)):
    a=book[i][3]
    sum=sum+a
print("avarage book price")
print(sum//len(book))

#find book through auther
d=input("enter auther")
for i in range(len(book)):
    
    if book[i][2]==d:
        for j in range(len(book[i])):
            print(book[i][j],end=" ")
        print()
"""
"""
6.

NOTE: using tuple only
An electronics store wants to maintain product information. Since product details should not be modified accidentally,
 each product record is stored as a tuple.

Tuple Format:

(product_id, product_name, price)

Requirements:

Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.

Test Case:

Input:

Enter number of products: 4

P101 Laptop 65000
P102 Mobile 25000
P103 Television 80000
P104 Tablet 30000

Expected Output:

All Products:
('P101', 'Laptop', 65000)
('P102', 'Mobile', 25000)
('P103', 'Television', 80000)
('P104', 'Tablet', 30000)

Costliest Product:
('P103', 'Television', 80000)

Cheapest Product:
('P102', 'Mobile', 25000)

Average Price:
50000.0

Products Above ₹50,000:
('P101', 'Laptop', 65000)
('P103', 'Television', 80000
"""
"""
n=int(input("enter no of element "))
pro=[]
for i in range(n):
    pid=int(input("enter id: "))
    pname=input("enter product name")
    price=int(input("Enter price : "))
    pro.append((pid,pname,price))
for i in pro:
    print(i)
print()
#max price
print("highest price")
max=pro[0][2]
h=0
for i in range(len(pro)):
    a=pro[i][2]
    if max<a:
        max=a
        h=i
print(pro[h])
print()
print("chepest price")
min=pro[i][2]
h=0
for i in range(len(pro)):
    a=pro[i][2]
    if min>a:
        min=a
        h=i
print(pro[h])
print()


print("average price")
sum=0
for i in range(len(pro)):
    a=pro[i][2]
    sum=sum+a
print(sum//len(pro))
        

print()
print("price above 50000")
for i in range(len(pro)):
    a=pro[i][2]
    if a>50000:
        print(pro[i])
"""
"""
7.

A cricket academy wants to analyze player performance. Each player's information is stored as a tuple.

Tuple Format:

(player_id, player_name, runs_scored)

Requirements:

Read N player records from the user and store them as tuples in a list.
Display all player records.
Find and display the player who scored the highest runs.
Find and display the player who scored the lowest runs.
Calculate and display the total runs scored by all players.
Calculate and display the average runs scored.
Display players who scored more than 50 runs.

Test Case:

Input:

Enter number of players: 5

101 Virat 82
102 Rohit 45
103 Gill 120
104 Hardik 38
105 SKY 76

Expected Output:

All Players:
(101, 'Virat', 82)
(102, 'Rohit', 45)
(103, 'Gill', 120)
(104, 'Hardik', 38)
(105, 'SKY', 76)

Highest Scorer:
(103, 'Gill', 120)

Lowest Scorer:
(104, 'Hardik', 38)

Total Runs:
 361

 Average Runs:
72.2

Players Scoring More Than 50 Runs:
(101, 'Virat', 82)
 (103, 'Gill', 120)
 (105, 'SKY', 76)
 """
"""
n=int(input("enter no of player : "))
pla=[]
for i in range(n):
    id=int(input("enter id"))
    name=input("enter player name: ")
    runs=int(input("enter runs: "))
    pla.append((id,name,runs))
    print()
print("all player")
for i in pla:
    print(i)
print()
print("highest score")
max=pla[0][2]
h=0
for i in range(len(pla)):
    a=pla[i][2]
    if max<a:
        max=a
        h=i
print(pla[h])

print("lower score")
min=pla[0][2]
h=0
for i in range(len(pla)):
    a=pla[i][2]
    if min>a:
        min=a
        h=i
print(pla[h])

print()
print("avarage")
sum=0
for i in range(len(pla)):
    a=pla[i][2]
    sum=sum+a
print(sum//len(pla))

print("Players Scoring More Than 50 Runs:")
for i in range(len(pla)):
    a=pla[i][2]
    if a>50:
        print(pla[i])
        """