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
#solution of question one

import clac
while True:
    print("1. add two number")
    print("2.sub two number")

    ch=int(input("enter your choice: "))
    
    match ch:
        case 1:
            a=int(input("enter first number: "))
            b=int(input("enter second number: "))
            print("addtion=",clac.add(a,b))
        case 2:
            a=int(input("enter first number: "))
            b=int(input("enter second number: "))
            print("subtraction=",clac.sub(a,b))
        case 3:
            print("exit")
            break





