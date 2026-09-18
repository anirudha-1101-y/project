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
"""
import sqaure,cube
while True:
    print("1.square of a number")
    print("2.cube of a number")
    print("3.square and cube both")
    print("4.exit")
    ch=int(input("enter your choice: "))
    match ch:
        case 1:
            n=int(input("enter your number: "))
            sqaure.sq(n)
        case 2:
            n=int(input("enter your number: "))
            cube.cu(n)
        case 3:
            n=int(input("enter your number: "))
            sqaure.sq(n),cube.cu(n)
        case 4:
            print("exit")
            break
"""