"""

ASSIGNMENT 5: School ERP System (Hierarchical Inheritance)
Scenario
A school is developing an ERP system.
Every person has common information.
Base Class
Person
Name
Age
Address
Derived Classes
Student
Roll Number
Course
Marks
Teacher
Employee ID
Subject
Salary
Principal
Office Number
Experience
Qualification
Functional Requirements
========== School ERP ==========
1. Add Student
2. Add Teacher
3. Add Principal
4. Display Student
5. Display Teacher
6. Display Principal
7. Exit
Sample Input
Choice : 1

Roll Number : 102
Name : Riya Sharma
Age : 20
Address : Indore

Course : Python Full Stack
Marks : 89
Sample Output
----------- Student Details -----------

Roll Number : 102
Name : Riya Sharma
Age : 20
Address : Indore

Course : Python Full Stack
Marks : 89
"""
class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

class Student(Person):
        def __init__(self,name,age,address,roll,course,marks):
             super().__init__(name,age,address)
             self.roll=roll
             self.course=course
             self.marks=marks
        def display(self):
            print("============Student detail===========")
            print("Student name               :",self.name)
            print("Student age                :",self.age)
            print("Student address            :",self.address)
            print("Student roll no            :",self.roll)
            print("Student course             :",self.course)
            print("Student marks              :",self.marks)



class Teacher(Person):
    def __init__(self,name,age,address,id,subject,salary):
         super().__init__(name,age,address)
         self.id=id
         self.subject=subject
         self.salary=salary
    def display(self):
            print("============Teacher detail===========")
            print("Teacher name               :",self.name)
            print("Teacher age                :",self.age)
            print("Teacher address            :",self.address)
            print("Employee id                :",self.id)
            print("Techer subject             :",self.subject)
            print("Teacher salary             :",self.salary)

class Principal(Person):
    def __init__(self,name,age,address,office_no,exp,qualification):
         super().__init__(name,age,address)
         self.office_no=office_no
         self.exp=exp
         self.qualification=qualification
    def display(self):
            print("===========Principal detail===========")
            print("Principal name                :",self.name)
            print("Principal age                 :",self.age)
            print("Principal address             :",self.address)
            print("Principal office no           :",self.office_no)
            print("Principal Experience          :",self.exp)
            print("Principal qualification       :",self.qualification)

student=None
teacher=None
principal=None

while True:
     print("========== School ERP ==========")
     print("1. Add Student")
     print("2. Add Teacher")
     print("3. Add Principal")
     print("4. Display Student")
     print("5. Display Teacher")
     print("6. Display Principal")
     print("7. Exit")


     ch=int(input("enter your choice : "))

     match ch:
        case 1:
               print("============add detail...........")
               name=input("enter your name :")
               age=int(input("enter your age :"))
               address=input("enter your address :")
               roll=int(input("enter student roll no : "))
               course=input("enter your course : ")
               marks=int(input("enter your marks : "))

               student=Student(name,age,address,roll,course,marks)
               print("detail added successfully ...............")

        case 2:
               print("============add detail...........")
               name=input("enter your name :")
               age=int(input("enter your age :"))
               address=input("enter your address :")
               id=int(input("enter your id : "))
               subject=input("enter your subject : ")
               salary=int(input("enter your salary :"))

               teacher=Teacher(name,age,address,id,subject,salary)
               print("detail added successfully ...............")

        case 3:
               print("============add detail...........")
               name=input("enter your name :")
               age=int(input("enter your age :"))
               address=input("enter your address :")
               office_no=int(input("enetr office number :"))
               exp=int(input("enter your experiance :"))
               qualification=input("enter your qualification :")

               principal=Principal(name,age,address,office_no,exp,qualification)
               print("detail added successfully ...............")
        case 4:
                 if student:
                       student.display()
                 else:
                       print("student not find .........")
        case 5:
                 if teacher:
                       teacher.display()
                 else:
                       print("teacher not find ................")

        case 6:
                 if principal:
                       principal.display()
                 else:
                       print("prinvipal not find ............")
        case 7:
                 print("EXIT")
                 break

               

               
     
               


    

         
     
