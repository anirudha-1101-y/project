"""
Question 1: Function + Local Variable

Create a function calculate_area(length, width) that:

Calculates the area of a rectangle.
Stores the result in a local variable named area.
Returns the area.
Call the function and print the result.

Sample Output

Area = 50
"""
"""
def a(l,w):
    area=l*w
    return area
l=int(input("enter length: "))
w=int(input("enter width: "))
r=a(l,w)
print(r)
#print("area",a(a,b))
"""
"""
Question 2: Class, Object, and Instance Variables

Create a class Student.

Requirements:

Instance variables:
name
age
marks
Create a method display() to print all details.
Create two objects with different data and display both.

Sample Output

Name : Dev
Age : 20
Marks : 92

Name : Rahul
Age : 21
Marks : 85
"""
"""
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age           #instance variable
        self.marks=marks
    def display(self):
        print("name :",self.name)
        print("age :",self.age)
        print("marks :",self.marks)
s1=Student("deepika",30,89)
s1.display()
print()
s2=Student("ranveer",35,90)
s2.display()
"""
"""
Question 3: Local Variable vs Instance Variable

Create a class Employee.

Requirements:

Instance variables:
name
salary
Create a method bonus() that:
Creates a local variable bonus = salary * 0.10
Prints both salary and bonus.
Create an object and call the method.

Concept Tested

Difference between instance variable and local variable.
"""
"""
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def sa(self):
        bonus=self.salary*0.10
        print("salary",self.salary)
        print("bonus",bonus)
e1=Employee("deepika",50000)
e1.sa()
"""
"""
Question 4: Function Inside a Class

Create a class Calculator.

Requirements:

Method add(a, b)
Method subtract(a, b)
Method multiply(a, b)
Create an object and call all three methods.

Sample Output

Addition = 30
Subtraction = 10
Multiplication = 200
"""
"""
class Calculator:
    
    def abc(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(abs(self.a-self.b))
    def mul(self):
        print(self.a*self.b)
c1=Calculator()
a=int(input("enter a"))
b=int(input("enter b"))
c1.abc(a,b)
c1.add()
c1.sub()
c1.mul()
"""
"""
Question 5: Mini Student Management System

Create a class Student.

Requirements:

Instance variables:
name
roll_no
python_marks
java_marks
Create methods:
total_marks()
average_marks()
display()
Create at least three objects.
Display:
Name
Roll Number
Total
Average

Bonus Challenge: Display Pass if average ≥ 40, otherwise Fail
"""
"""
class Student:
    def __init__(self,name,roll_no,python_marks,java_marks):
        self.roll_no=roll_no
        self.python_marks=python_marks
        self.java_marks=java_marks
        self.name=name
    def total_marks(self):
        return self.python_marks+self.java_marks
        return
    def average(self):
        return (self.python_marks+self.java_marks)/2
    def diaplay(self):
        print("name",self.name)
        print("id",self.roll_no)
        print("total",self.total_marks())
        print("average",self.average())
        if self.average()>=40:
            print("result","pass")
        else:
            print("result","fail")

s1=Student("ani",101,85,89)

s1.diaplay()
print()

s2=Student("mayank",102,31,29)

s2.diaplay()
print()

s3=Student("aaradhya",103,55,79)

s3.diaplay()
"""
#class work
"""
class Student:
    college="iit"
    def __init__(self,name):
        self.name=name
s1=Student("ani")
s2=Student("deepika")
print(s1.name)
print(s2.college)
Student.college="iiiiiiiiiit"       #change class variable using classname.variabke
print(s1.college)

"""
"""
class Student:
    college="nit"
    def __init__(self,name):
        self.name=name
    @classmethod
    def change_clg(cls,new):
        cls.college=new
s1=Student("ani")
print(s1.name)
print(s1.college)
Student.change_clg("iit")
print(s1.college)
print(s1.college)
"""
"""
class Calculator:
    @staticmethod
    def add(a,b):
        return a+b
c1=Calculator()
print(c1.add(10,20))
print(c1.__dict__)
print(Calculator.__dict__)
print(Calculator.add(10,20))
"""
#internal method call
"""
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_name(self):
        print("name",self.name)
    def display_marks(self):
        print("marks",self.marks)
    def displayall(self):
        self.display_name()
        self.display_marks()
s1=Student("ani",95)
s1.displayall()
"""
"""
#method chaining

class Student:
    def __init__(self,name):
        self.name=name
        self.marks=0
    def set_marks(self,marks):
        self.marks=marks
        return self
    def hello(self):
        print("heyy ",self.name)
        return self
    def display(self):
        print("marks is",self.marks)
        return self
s1=Student("ani")
s1.hello().set_marks(80).display()
"""
#ENCAPSULATION
#private specifier
"""
class Employee:
    def __init__(self,id,name,salary):
        self.__id=id
        self.__name=name
        self.__salary=salary
    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id=id

    def get_name(self):
        return self.__name
    def set_name(self,name):
      
        self.__name=name

    def get_salary(self):
        return self.__salary
    def set_salary(self,salary):
        if salary>=1000:
           self.__salary=salary
        else:
            print("not sufficient salary")
e1=Employee(101,"ani",50000)
print(e1.get_id())
print(e1.get_name())
print(e1.get_salary())
e1.set_salary(30000)
print(e1.get_salary())
"""
#10-06-2026
"""
1. Flatten a Matrix 

Convert a 2D list into a single list.

Input

matrix = [
    [1,2,3],
    [4,5],
    [6,7,8,9]
]

Output

[1,2,3,4,5,6,7,8,9]
"""
"""
r=int(input("enter no of rows"))
c=int(input("enter no of column"))
mat=[]
for i in range(r):
    rr=[]
    for j in range(c):
        x=int(input("enter no of element"))
        rr.append(x)
    mat.append(rr)
print(mat)
mat1=[]
for i in mat:
    for j in i:
        mat1.append(j)
print(mat1)
"""

"""
2. Count Even and Odd Numbers in a Matrix 

Count how many even and odd numbers are present.

Input

matrix = [
    [2,5,8],
    [1,4,7]
]

Output

Even = 3
Odd = 3
"""
"""
r=int(input("enter no of rows"))
c=int(input("enter no of column"))
mat=[]
for i in range(r):
    rr=[]
    for j in range(c):
        x=int(input("enter no of element"))
        rr.append(x)
    mat.append(rr)
print(mat)
e=0
o=0
for i in mat:
    for j in i:
        if j%2==0:
            e=e+1
        else:
            o=o+1
print("even",e)
print("odd",o)
"""
"""
3. Transpose of a Matrix 

Find the transpose of a matrix.

Input

matrix = [
    [1,2,3],
    [4,5,6]
]

Output

[
 [1,4],
 [2,5],
 [3,6]
]

"""
"""
r=int(input("enter no of rows"))
c=int(input("enter no of column"))
mat=[]
for i in range(r):
    rr=[]
    for j in range(c):
        x=int(input("enter no of element"))
        rr.append(x)
    mat.append(rr)
print(mat)
mat1=[]
for i in range(c):
    rr=[]
    for j in range(r):
        rr.append(mat[j][i])
    mat1.append(rr)
print(mat1)
"""
"""
4. Find the Row Having Maximum Sum 

Input

matrix = [
    [1,2,3],
    [10,20,30],
    [5,5,5]
]

Output

Row Index = 1
Row Sum = 60
""
"""
"""
r=int(input("enter no of rows"))
c=int(input("enter no of column"))
mat=[]
for i in range(r):
    rr=[]
    for j in range(c):
        x=int(input("enter no of element"))
        rr.append(x)
    mat.append(rr)
print(mat)

max=0

for i in range(r):
    sum=0
    for j in range(c):
        sum=sum+mat[i][j]
    if  sum>max:
        max=sum
        h=i
print(h)        
print(sum)
"""
"""
5. Find the Longest String in a List 

Input

words = ["apple","banana","kiwi","watermelon","grapes"]

Output

watermelon
"""
"""
l=list(map(str,input("enter your word :").split()))
m=""
for i in l:
    if len(i)>len(m):
        m=i
print(m)
"""
"""
6. Group Strings by Their First Letter 

Input

words = ["apple","ant","ball","bat","cat","car"]

Output

{
'a':['apple','ant'],
'b':['ball','bat'],
'c':['cat','car']
}
"""
"""
l=list(map(str,input("enter your word :").split()))
a=[]
b=[]
c=[]
for i in l:
    if i.startswith("a"):
        a.append(i)
    elif i.lower().startswith("b"):
        b.append(i)
    else:
         i.lower().startswith("c")
         c.append(i)
d={
    "a":a,
    "b":b,
    "c":c
}
print(d)
"""
"""
words=list(map(str,input("enter your word :").split()))
d = {}

for word in words:
    first = word[0]      # First letter

    if first not in d:
        d[first] = []

    d[first].append(word)

print(d)

"""


"""
7. Find Common Words Between Two Lists 

Input

list1 = ["python","java","c","sql"]
list2 = ["sql","python","html"]

Output

["python","sql"]
"""
"""
l=list(map(str,input("enter your word :").split()))
l1=list(map(str,input("enter your word :").split()))
same=[]
for i in l:
    for j in l1:
        if i==j:
            same.append(i)
print(same)
"""

"""
8. Rotate a Matrix by 90° Clockwise 

Input

matrix = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

Output

[
 [7,4,1],
 [8,5,2],
 [9,6,3]
]
"""
"""
r=int(input("enter no of rows"))
c=int(input("enter no of column"))
mat=[]
for i in range(r):
    rr=[]
    for j in range(c):
        x=int(input("enter no of element"))
        rr.append(x)
    mat.append(rr)
print(mat)
mat1=[]
for j in range(c):
    rr=[]
    for i in range(r-1,-1,-1):
        rr.append(mat[i][j])
    mat1.append(rr)
print(mat1)
"""
"""
9. Find Duplicate Words in a Sentence 

Input

sentence = "python java python c java sql python"

Output

python -> 3
java -> 
"""
"""
l= input("Enter sentence: ").split()

v = []

for word in l:
    if word not in v:
        if l.count(word) > 1:
            print(word, "->", l.count(word))
        v.append(word)


"""
"""
l = input("Enter sentence: ").split()

v = []

for i in range(len(l)):
    c = 1

    if l[i] not in v:
        for j in range(i + 1, len(l)):
            if l[i] == l[j]:
                c += 1

        if c > 1:
            print(l[i], "->", c)

        v.append(l[i])
        """

#inheritance 
#single inheritance
"""
class Parent:
    def func1(self):
        print("this is parent class function")
class Child(Parent):
    def func2(self):
        print("this is chile class ")
obj=Child()
obj.func1()
obj.func2()
obj.func1()
"""
"""
class Person:
    def __init__(self,name):
        self.name=name
class Emp(Person):
    def display(self):
        print(self.name,"is employee")
obj=Emp("depika")
obj.display()
"""
#multi-level inheritance
"""
class Grandp:
    def fun1(self):
        print("i am garnparent")
class Parent(Grandp):
    def fun2(self):
        print("i am parent")
class Child(Parent):
    def fun3(self):
        print("i am child")

obj=Child()
obj.fun1()
obj.fun2()
obj.fun3()
"""
"""
#super keyword
class Parent:
    def __init__(self):
        print("constuctoe is called")
class Emp(Parent):
    
    def __init__(self):
        super().__init__()
        print("employee constructer")
e=Emp()
"""
"""


class Person:
    def __init__(self,name):
        self.name=name
        print(self.name)
class Emp(Person):
    def __init__(self,name,slary):
        super().__init__(name)
        self.salary=slary
        print("employee contructor")
e=Emp("DEEPIKA",82000)
print(e.name)
print(e.salary)
"""
"""
class Person:
    def show(self,name):
        self.name=name
        print(self.name)
class Emp(Person):
    def __init__(self,name,slary):
        super().show(name)
        self.salary=slary
        print("employee contructor")
e=Emp("DEEPIKA",82000)
print(e.name)
print(e.salary)
"""
#multiple inheritance
#child class inherit from more than parent class
"""
class Dada:
    def house(self):
        print("dada i love you")
class Dadi:
    def all(self):
        print("i love you dadi")

class Ani(Dada,Dadi):
    def ani(self):
     
        print("nothing")
a=Ani()
a.ani()
a.all()
a.house()ani

"""
"""
try:
    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks (0-100): "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B+"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    print("\n------ RESULT ------")
    print("Student Name :", name)
    print("Marks        :", marks)
    print("Grade        :", grade)

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Something went wrong:", e)
    """
"""
class Student:
  def add(self):
    print("ybgbg7b")
s1 = Student()
s2 = Student()

print(s1 == s2)
print(s1 is s2)
"""
"""
ASSIGNMENT 7: Hotel Booking System (Method Overriding)
Scenario

A hotel has different room types. The room rent is calculated differently for each room.

Base Class

Room

Common Details

Room Number
Customer Name
Days Stayed
Derived Classes
StandardRoom
Rent Per Day
Total Rent = Rent × Days
DeluxeRoom
Rent Per Day
Luxury Charge
Total Rent = (Rent × Days) + Luxury Charge
SuiteRoom
Package Amount
Total Rent = Package Amoun
"""
class Room:
    def __init__(self,r_no,cust_name,day):
        self.room_no=r_no
        self.cust_name=cust_name
        self.day=day

class StandardRoom(Room):
    def __init__(self,r_no,cust_name,day,room_rent):
        super().__init__(r_no,cust_name,day)
        self.room_rent=room_rent

    def total(self):
        self.total=self.day*self.room_rent
    
    def display(self):
        print("Room no",self.room_no)
        print("Customer name ",self.cust_name)
        print("Day stayed ",self.day)
        print()
        print("Room rent",self.room_rent)
        print("Total bill ",self.total)


    
class DeluxeRoom(Room):
    def __init__(self,r_no,cust_name,day,room_rent,luxury_c):
        super().__init__(r_no,cust_name,day)
        self.room_rent=room_rent
        self.luxury_c=luxury_c
    def total(self):
        self.total=(self.day*self.room_rent)+self.luxury_c

    def display(self):
        print("Room no",self.room_no)
        print("Customer name ",self.cust_name)
        print("Day stayed ",self.day)
        print()
        print("luxury charge",self.luxury_c)
        print("Room rent",self.room_rent)
        print("Total bill ",self.total)

class SuiteRoom(Room):
    def __init__(self,r_no,cust_name,day,package_a):
        super().__init__(r_no,cust_name,day)
        self.package_a=package_a
    def total(self):
        self.total=self.package_a

    def display(self):
        print("Room no",self.room_no)
        print("Customer name ",self.cust_name)
        print("Day stayed ",self.day)
        print()
        print("Package amount",self.package_a)
        print("Total bill ",self.total)
    
suit=None
deluxe=None
standard=None

while True:
    print("========== Hotel Booking ==========")

    print("1. Add Standard Room")
    print("2. Add Deluxe Room")
    print("3. Add Suite Room")
    print("4. Display Standard Bill")
    print("5. Display Deluxe Bill")
    print("6. Display Suite Bill")
    print("7. Exit")

    ch=int(input("enter your choice : "))
    match ch:
        case 1:
            r_no=int(input("Enter your room no"))
            cust_name=input("enter your name")
            day=int(input("enter no of days :"))
            room_rent=int(input("enter room rent "))

            standard=StandardRoom(r_no,cust_name,day,room_rent)
            print("detail added successfully ................")

        case 2:
            r_no=int(input("Enter your room no"))
            cust_name=input("enter your name")
            day=int(input("enter no of days :"))
            room_rent=int(input("enter room rent "))
            luxury_c=int(input("enter luxury charge "))

            deluxe=DeluxeRoom(r_no,cust_name,day,room_rent,luxury_c)
            print("detail added successfully ................")

        case 3:
            r_no=int(input("Enter your room no"))
            cust_name=input("enter your name")
            day=int(input("enter no of days :"))
            package_a=int(input("enter package amount"))

            suit=SuiteRoom(r_no,cust_name,day,package_a)
            print("detail added successfully ................")

        case 4:
            if standard:
                standard.total()
                standard.display()
            else:
                print("not found .........")

        case 5:
            if deluxe:
                deluxe.total()
                deluxe.display()
            else:
                print("not found ...........")
        
        case 6:
            if suit:
                suit.total()
                suit.display()
            else:
                print("not found ..........")
        case 7:
            print("exit")
            break
            






