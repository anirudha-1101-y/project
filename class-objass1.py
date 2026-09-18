"""
Question 1: Employee Salary Management System
Scenario

A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.

Requirements

Create a class named Employee with the following attributes:

employee_id
employee_name
basic_salary

Initialize the values using a constructor.

Calculations
HRA = 20% of Basic Salary
DA = 15% of Basic Salary
Gross Salary = Basic Salary + HRA + DA
Sample Input
Enter Employee ID : E101
Enter Employee Name : Rahul Sharma
Enter Basic Salary : 50000
Sample Output
------ Employee Salary Details ------
Employee ID      : E101
Employee Name    : Rahul Sharma
Basic Salary     : 50000.0
HRA              : 10000.0
DA               : 7500.0
Gross Salary     : 67500.0
"""
"""
class Employee:
    def __init__(self,id,name,bs):
        self.id=i
        self.name=n
        self.bs=b
    def salary(self):
        self.hra=self.bs*0.20
        self.da=self.bs*0.15
    def detail(self):
        print("-----------employee salary detail----------")
        print("employee id: ",self.id)
        print("employee name: ",self.name)
        print("basic salary: ",self.bs)
        print("HRA: ",self.hra)
        print("DA: ",self.da)
        self.total=self.bs+self.hra+self.da
        print("gross salary: ",self.total)
i=int(input("enter your id"))
n=input("enter your name")
b=int(input("enter your salary"))
e1=Employee(i,n,b)

e1.salary()
e1.detail()
    
"""
"""
Question 2: Electricity Bill Calculator
Scenario


An electricity company wants to generate monthly bills for its customers.

Requirements

Create a class named Customer with:

customer_id
customer_name
units_consumed

Initialize the values using a constructor.

Calculations
Cost per Unit = ₹8
Fixed Charge = ₹150
Total Bill = (Units × 8) + 150
Sample Input
Enter Customer ID : C101
Enter Customer Name : Amit Verma
Enter Units Consumed : 350
Sample Output
------ Electricity Bill ------
Customer ID       : C101
Customer Name     : Amit Verma
Units Consumed    : 350
Total Bill Amount : ₹2950.0

"""
"""
class Customer:
    def __init__(self,customer_id,customer_name,units_consumed):
        self.custid=customer_id
        self.cusn=customer_name
        self.units=units_consumed
    def display(self):
        self.fix=(self.units*8)+150
    def bill(self):
        print("----------total bill------------")
        print("customer_id: ",self.custid)
        print("customer_name: ",self.cusn)
        print("units_consumed: ",self.units)
        print("TOTAL BILL: ",self.fix)
id=input("enter your id")
name=input("enter customer name")
unit=int(input("enter unit consumed"))
c1=Customer(id,name,unit)
c1.display()
c1.bill()

"""
"""
Question 3: Online Shopping System
Scenario

An e-commerce company wants to calculate the final amount payable by customers after applying discounts.

Requirements

Create a class named Product with:

product_id
product_name
quantity
price_per_item

Initialize the values using a constructor.

Calculations
Total Amount = Quantity × Price Per Item
If Total Amount > ₹5000, Discount = 10%
Otherwise, Discount = 5%
Final Amount = Total Amount − Discount
Sample Input
Enter Product ID : P101
Enter Product Name : Laptop
Enter Quantity : 2
Enter Price Per Item : 35000
Sample Output
------ Shopping Bill ------
Product ID        : P101
Product Name      : Laptop
Quantity          : 2
Price Per Item    : 35000.0
Total Amount      : ₹70000.0
Discount          : ₹7000.0
Final Amount      : ₹63000.0
"""
"""
class Product:
    def __init__(self,id,name,price,quan):
        self.id=id
        self.name=name
        self.quantity=quan
        self.price=price
    def display(self):
        print("---------------------final bill---------------------------")
        self.total=self.price*self.quantity
        if self.total>=5000:
            self.dis=self.total*0.10
        else:
            self.dis=self.total*0.05
        self.final=self.total-self.dis
        print("Product ID :",self.id)
        print("Product Name: ",self.name)    
        print("Quantity :",self.quantity)
        print("Price Per Item :",self.price)
        print("Total Amount :",self.total)
    
        print("Discount :",self.dis)
        print("Final Amount",self.final)
id=input("enter your id: ")
name=input("enter your name: ")

price=int(input("enter price: "))
qua=int(input("enter quantity: "))

p1=Product(id,name,price,qua)
p1.display()
"""
"""
Question 4: Student Result Processing System
Scenario

A college wants to automate result generation by calculating total marks, percentage, and grade.

Requirements

Create a class named Student with:

roll_number
student_name
marks1
marks2
marks3

Initialize the values using a constructor.

Calculations
Total = Marks1 + Marks2 + Marks3
Percentage = Total / 3
Grade Criteria
Percentage	Grade
90 and above	A
75 to 89	B
60 to 74	C
Below 60	D
Sample Input
Enter Roll Number : 101
Enter Student Name : Priya Sharma
Enter Marks in Subject 1 : 85
Enter Marks in Subject 2 : 90
Enter Marks in Subject 3 : 88
Sample Output
------ Student Result ------
Roll Number      : 101
Student Name     : Priya Sharma
Total Marks      : 263
Percentage       : 87.67
Grade            : B
"""
"""
class Student:
    def __init__(self,rn,name,a,b,c):
        self.roll_no=rn
        self.name=name
        self.marks1=a
        self.marks2=b
        self.marks3=c
        self.total=self.marks1+self.marks2+self.marks3
    def final(self):
        self.percent=self.total/3
        if self.percent>=90:
            self.grade="A"
        elif 89>=self.percent>=75:
            self.grade="B"
        elif 74>=self.percent>=60:
            self.grade="C"
        else:
            self.percent="D"
    def display(self):
        print("------ Student Result ------")
        print("Roll Number :",self.roll_no)
        print("Student Name :",self.name)
        print("Total Marks :",self.total)
        print("Percentage :",self.percent) 
        print("Grade :",self.grade)
ro=int(input("enter roll no: "))
n=input("enter student name: ")
a=int(input("Enter Marks in Subject 1: "))    
b=int(input("Enter Marks in Subject 2: "))        
c=int(input("Enter Marks in Subject 3: "))
s1=Student(ro,n,a,b,c)
s1.final()
s1.display()

"""
"""
Question 5: Hotel Room Booking System
Scenario

A hotel wants to generate the final bill of guests based on the duration of their stay.

Requirements

Create a class named Guest with:

guest_id
guest_name
number_of_days
room_charge_per_day

Initialize the values using a constructor.

Calculations
Room Bill = Number of Days × Room Charge Per Day
GST = 12% of Room Bill
Final Bill = Room Bill + GST
Sample Input
Enter Guest ID : G101
Enter Guest Name : Rohan Mehta
Enter Number of Days : 4
Enter Room Charge Per Day : 2500
Sample Output
------ Hotel Bill ------
Guest ID              : G101
Guest Name            : Rohan Mehta
Number of Days        : 4
Room Charge Per Day   : ₹2500.0
Room Bill             : ₹10000.0
GST (12%)             : ₹1200.0
Final Bill            : ₹11200.0

"""
#solution
"""
class Guest:
    def __init__(self,id,name,day,e):
        self.id=id
        self.name=name
        self.day=day
        self.charge=e
    def room_b(self):
        self.bill=self.day*self.charge
        self.gst=self.bill*0.12
    def final(self):
        self.finalbill=self.bill+self.gst
    def display(self):
        print("------ Hotel Bill ------")
        print("Guest ID :",self.id)
        print("Guest Name :",self.name)
        print("Number of Days :",self.day)
        print("Room Charge Per Day :",self.charge)
        print("Room Bill :",self.bill)
        print("GST (12%) :",self.gst)
        print("Final Bill :",self.finalbill)






id=int(input("enter guest id: "))
name=input("enter guest name")
day=int(input("enter number of days: "))
e=int(input("Enter Room Charge Per Day"))

g=Guest(id,name,day,e)
g.room_b()

g.final()
g.display()
"""
"""
Question 6: Library Book Management System


A library wants to maintain information about books. The librarian should be able to:

View book details.
Issue the book to a student.
Return the book.
Requirements

Create a class named Book with the following attributes:

book_id
title
author
status (Initially "Available")

Initialize the values using a constructor.

Create the following methods:
display_details() → Displays all book information.
issue_book() → Changes the status to "Issued".
return_book() → Changes the status to "Available".
Sample Input
Enter Book ID : B101
Enter Book Title : Python Programming
Enter Author Name : John Smith
Sample Output
------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Available

Book issued successfully.

------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Issued

Book returned successfully.

------ Book Details ------
Book ID     : B101
Title       : Python Programming
Author      : John Smith
Status      : Available
"""
"""
class Book:
    a="available"
    def __init__(self,id,title,author):
        self.id=id
        self.title=title
        self.author=author
        self.d={
            "book":id,"title":title,"author":author,"status":Book.a}
    def display(self):
        print("============book detail==========")
        for i,j in self.d.items():
            print(i,":",j)
    def issue(self):
        print("Book issued successfully.")
        self.d["status"]="issued"
    def return_book(self):
        print("Book returned successfully.")
        self.d["status"]="available"

b1=Book(101,"mahabharat","vedvyas",)
b1.display()
b1.issue()
b1.display()
b1.return_book()
b1.display()

"""
