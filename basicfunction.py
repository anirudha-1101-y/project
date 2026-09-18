#function--
"""
def sum(a,b):
    c=a+b
    print(c)
sum(5,10)
"""
"""
def sum(a,b):
    c=a+b
    print("sum is",c)
a=int(input("enter fist no"))
b=int(input("enter second no:"))
sum(a,b)
"""
"""
def welcome():
    print("welcome guys")
def hello():
    welcome()
    print("guys how are you")
def name():
    n=input("enter your name")
    print("name is ",n)
    hello()
name()
"""
#positional argument---
"""
def hello(name,age):
    print("name is",name,"age =",age)
hello("deeika",45)
"""
"""
#return argument====
def hello():
    print("hello")
    return
   
def main():
    print("welcome")
    hello()
    print("done")
main()
"""
"""
def even(n):
    e=[]
    for i in range(1,n+1):
        if i%2==0:
            e.append(i)
    return  e
print(even(10))
"""
"""
def hello(name,age):
    print("aname is",name)
    print("age is",age)
hello(age=95,name="ani")
"""
"""
def hello(name,age,salary):
    print(name,age,salary)
hello("ani",age=90,salary=7500)
"""
#default parameter 
"""
def hello(n,a,age="indore",salary=4500):
    print("name id",n)
    print("name id",a)
    print("name id",age)
    print("name id",salary)
hello(n="depika",a=45,age="hyb")
"""
#variable length argument--
#def function(*args)
"""
def d(*ani):
    print(ani)
d(1,2,3,4,5)
"""
"""
def sum(*args):
    t=0
    for i in args:
        t=t+i
    print(t)
sum(10,20,30)
"""
"""
def hello(name,*marks):
    print("name is",name)
    print("marks is",marks)
    print("marks is ",*marks)
hello("depika",10,20,30)

"""
"""
def average(*n):
    return sum(n)//len(n)
print(average(10,20,30,40))
"""
"""
l1=[1,2,3,4,5,6]
def add(*l1):
    return sum(l1)
print(add(*l1))
"""
"""
l1=[1,2,3,4,6]
def add(a,b,c,d,e):
    sum=a+b+c+d+e
    print(sum)
add(*l1)
"""
"""
def add(*l1):
    s=0
    for i in l1:
        s=s+i
    return s
print(add(10,20,30,40,50))
"""
#keyword variable length argument
"""
def dis(**kwargs):
    print(kwargs)
dis(name="ani",age=18,salary=15000)

def dis(**kwargs):
    

    for k,v in kwargs.items():
        print(k,v)
    print(kwargs["name"])
dis(name="ani",age=18,salary=15000)
"""
"""
def profile(**info):
    if "name" in info:
        print("name",info["name"])
    if "age" in info:
        print("age",info["age"])


profile(name="ani",age=18,salary=4500)
"""
#positional only argument-(/):
"""
def dis(name,age,salary,/):
    print("name is",name)
    print("age is",age)
    print("salary is",salary)
dis("deepika",15,8)
"""
"""
def dis(name,/,age,salary):
    print("name ",name,age,salary)
dis("ani",age=18,salary=1999)
"""
"""
def add(*args):
    print(sum(args))
add(10,20,30,40)
"""

"""
def add(a,b):
    return (a+b)


print(add(a=10,b=30))
"""
"""
#keyword only parameter ---(*)
def show(name,/,*,age,add):
    print(name,age,add)
show("ani",age=82,add="indore")
"""



#note==when we use positional only argument we use(/) and before slash all value are consider as positional and we talk bout keyword only argumnet (*)
#after that all value must consider as keyword parameter


#lambda function==
#lambda agrgument : expression argument mean input parameter and expression mean statement
"""
fun=lambda a,b:a*b
print(fun(5,10))
"""
"""
fun=lambda *a:[i**2 for i in a]
print(fun(5,10,20))
"""
"""
max=lambda a,b: a if a>b else b
print(max(10,20))
"""
"""
def sq(x):
    return x*x
l1=[10,20,30,40,50]
print(list(map(sq,l1)))
"""
"""
1.
STUDENT RESULT MANAGEMENT SYSTEM

Scenario:

A college examination department wants to automate the process of generating student results. The staff should be able to enter student details, calculate marks, determine grades, and display a complete report card using a menu-driven application.

Develop a Python program using multiple user-defined functions and a menu-driven approach to perform the following operations.

MENU

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit

Functional Requirements

1. Add Student Details

   * Student Name
   * Roll Number
   * Marks of 5 Subjects

2. Calculate Total Marks

3. Calculate Percentage

4. Find Grade

5. Display Complete Result

6. Find Highest Subject Mark

7. Find Lowest Subject Mark

8. Exit

Grade Criteria

Percentage        Grade

90 - 100          A+
80 - 89           A
70 - 79           B
60 - 69           C
50 - 59           D
Below 50          Fail

Constraints

* Marks should be between 0 and 100.
* Display an appropriate message for invalid marks.
* The program should continue until the user chooses Exit.

Sample Input / Output

*** STUDENT RESULT MANAGEMENT ***

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Result
6. Find Highest Mark
7. Find Lowest Mark
8. Exit

Enter Choice : 1

Enter Student Name : Ajay
Enter Roll Number : 101

Enter Mark 1 : 78
Enter Mark 2 : 85
Enter Mark 3 : 92
Enter Mark 4 : 88
Enter Mark 5 : 77

Student details added successfully.

Enter Choice : 2

Total Marks = 420

Enter Choice : 3

Percentage = 84.0

Enter Choice : 4

Grade = A

Enter Choice : 6

Highest Mark = 92

Enter Choice : 7

Lowest Mark = 77

Enter Choice : 5

----------- RESULT CARD -----------

Name        : Ajay
Roll Number : 101

Marks
Subject 1 : 78
Subject 2 : 85
Subject 3 : 92
Subject 4 : 88
Subject 5 : 77

Total Marks : 420
Percentage  : 84.0
Grade       : A
Highest Mark: 92
Lowest Mark : 77

Enter Choice : 8

Thank You. Program Terminated.

Important Instructions

1. The solution must be developed using multiple user-defined functions.
2. Use appropriate parameters wherever data needs to be passed between functions.
3. Use return statements wherever a function needs to send a result back to the caller.
4. Avoid using unnecessary global variables.
5. Implement the application using a menu-driven approach.
6. Perform proper input validation.
7. Write meaningful function names and maintain proper code readability
"""
"""

def profile(name,id,marks):
    print("name is ",name)
    print("id is",id)
    for i in range(len(m)):
        print("subject",i+1,m[i])

def total(m):
    return sum(m)
def percent(m):
    return sum(m)/5
def grade(m):
    x=sum(m)/5
    return "a+" if x>=90 else "a" if 80<=x<=89 else "B" if 70<=x<=79 else "c" if 60<=x<=69 else "d" if 50<=x<=59 else "fail"
def ma(m):
    return max(m)
def mi(m):
    return min(m)

m=[]
while True:
    print("1. Add Student Details")
    print("2. Calculate Total Marks")
    print("3. Calculate Percentage")
    print("4. Find Grade")
    print("5. Display Result")
    print("6. Find Highest Mark")
    print("7. Find Lowest Mark")
    print("8. Exit")
    ch=int(input("enter your choice: "))
    match ch:
        case 1:
            n=input("entre your name")
            id=int(input("enter id"))
            
            for i in range(5):
                x=int(input("enter marks: "))
                m.append(x)
            profile(n,id,m)
        case 2:
            print("total marks",total(m))
        case 3:
            print("total percent",percent(m))
        case 4:
            print("grade",grade(m))
        case 5:
            profile(n,id,m)
            print("total marks",total(m))
            print("total percent",percent(m))
            print("grade",grade(m))
            print("maiximum marks",ma(m))
            print("minimum marks",mi(m))
            

        case 6:
            print("maiximum marks",ma(m))
        case 7:
            print("minimum marks",mi(m))
        case 8:
            print("exit")
            break


"""

#lambda function---
"""
l=[1,2,3,4,5]
r=map(lambda x:x*x ,l)
print(list(r))
"""
"""
l=["ani","anirudha","yadav","aaradhya","seema"]
r=filter(lambda x:len(x)>=5 ,l)
print(list(r))
"""
"""
l=["ani","anirudha","yadav","aaradhya","seema"]
def cap(x):
    return x.capitalize()
print(list(map(cap,l)))
"""
"""
l=["ani","anirudha","yadav","aaradhya","seema"]
r=map(lambda x:x.capitalize(),l)
print(list(r))
"""
"""
l=["ani","anirudha","yadav","aaradhya","seema"]
r=map(lambda x:len(x),l)
print(list(r))
"""
"""
l1=[10,20,30,40]
l2=[40,30,20,10]
r=map(lambda a,b:a+b,l1,l2)
print(list(r))
"""
"""
l1=[10,20,30,40]
l2=[40,30,20,10]
def add(a,b):
    return a+b
print(list(map(add,l1,l2)))
"""
"""
l1=[10,12,15,17,19,20]
r=map(lambda x:"even" if x%2==0 else "odd",l1)
print(list(r))
"""
"""
l1=[10,12,15,17,19,20]
def eo(x):
    return "even" if x%2==0 else "odd"
print(list(map(eo,l1)))
"""
#filter function -----------
"""
this function is only those element are come whose condition is true thatwhy is called filter function it filter out items from an iterable"""
"""
l1=[10,12,15,17,19,20]
r=filter(lambda x:x%2==0 ,l1)
print(list(r))
"""
"""
l=["ani","aaradhya","aman","yadav","anu"]
r=filter(lambda x:x.startswith("a"),l)
print(list(r))
"""
"""
l=["ani","aaradhya","aman","yadav","anu"]
r=filter(lambda x:len(x)>=5,l)
print(list(r))
"""
"""
l1=[10,12,15,17,19,20]
r=map(lambda x:str(x),l1)
print(list(r))
"""
"""
l=["ani","aaradhya","aman","yadav","anu",""]
r=filter(lambda x:len(x)>0,l)
#r=filter(lambda x:x,l)
print(list(r))
"""
"""
l=[1,2,3,4,5,6]
r=filter(lambda x:x%2!=0,(map(lambda x:x*x,l)))
print(list(r))
r=map(lambda x:x*x,(filter(lambda x:x%2==0,l)))
print(list(r))
"""
"""
l=["ani","aaradhya","aman","yadav","anu"]
r=map(lambda x:x[::-1],l)
print(list(r))
"""
"""
l1=[10,12,15,17,19,20]
r=map(lambda x:x+10,l1)
print(list(r))
"""
"""
l1=[10,12,15,17,19,20]
r=map(lambda x:x*2,(filter(lambda x:x>15,l1)))

print(list(r))
"""
"""
2.
NUMBER ANALYSIS SYSTEM

Scenario:

A software company wants to develop a Number Analysis System. The application should be menu-driven and perform different mathematical operations on a given number.

MENU

1. Check Perfect Number
2. Check Prime Number
3. Find Reverse of a Number
4. Calculate Factorial
5. Display Factors of a Number
6. Exit

Requirements

Choice 1 – Check Perfect Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return True if the number is Perfect, otherwise False.
* Display an appropriate message based on the returned value.

Choice 2 – Check Prime Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return a message such as "Prime Number" or "Not a Prime Number".
* Display the returned message.

Choice 3 – Find Reverse of a Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return the reversed number.
* Display the returned value.

Choice 4 – Calculate Factorial

* Accept a number from the user.
* Pass the number to a function.
* The function should return the factorial value.
* Display the returned value.

Choice 5 – Display Factors of a Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return all factors of the given number.
* Display the returned factors.

Choice 6 – Exit

Sample Output

Enter Choice : 1

Enter Number : 28

28 is a Perfect Number

---

Enter Choice : 2

Enter Number : 17

Prime Number

---

Enter Choice : 3

Enter Number : 1234

Reverse Number : 4321

---

Enter Choice : 4

Enter Number : 5

Factorial : 120

---

Enter Choice : 5

Enter Number : 12

Factors : 1 2 3 4 6 12

---

Important Instructions

1. Create separate functions for each operation.
2. Use parameters to pass values to functions.
3. Use return statements appropriately.
4. Different functions should return different types of values such as Boolean, String, Integer, and Collection/List.
5. Avoid using global variables.
6. Implement the solution using a menu-driven approach.
7. Write meaningful function names and maintain proper code readability.
"""
"""
def pn(n):
    sum=0
    for i in range(1,n//2+1):
        if n%i==0:
            sum=sum+i
    if sum==n:
        print(n,"is a perfect number")
    else:
        print("not a perfect no")
def prino(n):
    if n>1:
        x=0
        for i in range(2,n//2+1):
            if n%i==0:
                x=1
                break
        if x==0:
            print("prime no")
        else:
            print("not a prime no")
    else:
        print("not a prime number")
def rev(n):
    re=0
    while n>0:
        rem=n%10
        re=re*10+rem
        n=n//10
    print("reverse no",re)

def fac(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print("fatorial :",f)


def factor(n):
    for i in range(1,n):
        if n%i==0:
            print(i,end=" ")


print()



print()
while True:
    print("=========MENU============")

    print("1. Check Perfect Number")
    print("2. Check Prime Number")
    print("3. Find Reverse of a Number")
    print("4. Calculate Factorial")
    print("5. Display Factors of a Number")
    print("6. Exit")
    ch=int(input("enter your choice"))
    match ch:
        case 1:
            n=int(input("enter perfect no"))
            pn(n)
        case 2:
            n=int(input("enter prime no"))
            prino(n)
        case 3:
            n=int(input("enter number: "))
            rev(n)
        case 4:
            n=int(input("enter factorial no"))
            fac(n)
        case 5:
            n=int(input("enter factor"))
            factor(n)
            print()
        case 6:
            print("exit")
            break
            
"""
#lambda function--
"""
l=[1,2,35,85,5,65]
b=sorted(map(lambda x:x+10,filter(lambda x:x>10 ,l)),reverse=True)
print(b)
"""
"""
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
def main():
    x=fact(5)
    print(x)
main()
"""
"""
def pow(b,p):
    if p==0:
        return 1
    return b*pow(b,p-1)
def main():
    x=pow(2,5)
    print(x)
main()
"""
#nested function--
"""
def hello(name):
    def message():
        return "hey guys how are you"
    print("hello",name)
    print(message())
hello("ani")
"""
"""
def outer():
    x=10
    
    def inner():
        x=100
        print("inner of x",x)
    print("outer value",x)
    inner()
outer()
"""
#inner funtion can access outer function but outer function can't
"""
def outer():
    x=10
    
    def inner():
        x=100
        print("inner of x",x)
    
    inner()
    print("outer value",x)
outer()
"""
#pthon follow legb=local enclosing global builtin
"""
def outer():
    x=10
    def inner():
        nonlocal x
        x=100
        print("iinner value",x)
    inner()
    print("outer value",x)
outer()
"""
#enclosing mean nearest outer
"""
x=100
def test():
    x=10
    print("inside funt",x)
test()
print("value is",x)
"""
"""
x=100
def test():
    x=90
    def inner():
        print("value is",x)
    inner()
test()
"""
#higher order function 
"""
def hello(fun):
    return fun("hey guys")
def uppercase(x):
    return x.upper()
print(hello(uppercase))
"""
#closure 
"""
def hello(name):
    message=f"hello  {name}"
    def display():
        print(message)
    return display
#closure
h=hello("ani")
h()
"""
"""
def counter():
    c=0
    def increament():
        nonlocal c
        c=c+1
        return c
    return increament
c=counter()
print(c())
print(c())
"""
"""
def codemaker(greet,name):
    def card():
        return greet,name
    return card
first=codemaker("hello","ani")
seco=codemaker("hii","yadav")

print(first())
print(seco())
"""
"""
Question 1: Module (Easy)

Create a module named calc.py containing the following functions:

add(a, b) – returns the sum
sub(a, b) – returns the difference

Now create another Python file main.py that:

Imports the calc module.
Takes two numbers as input.
Displays the addition and subtraction using the module functions.

Example:

Enter first number: 20
Enter second number: 5

Addition = 25
Subtraction = 15
"""












































"""
Question 2: Package (Easy)

Create a package named mathpack with the following structure:

mathpack/
│── _init_.py
│── square.py
│── cube.py
square.py should contain a function square(n) that returns the square of a number.
cube.py should contain a function cube(n) that returns the cube of a number.

Create main.py that:

Imports both functions from the package.
Takes a number as input.
Prints its square and cube.

Example:

Enter a number: 4

Square = 16
Cube = 64
"""