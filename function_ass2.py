#question==1
"""
1.
Employee Record Sorting (Lambda)


A company stores employee details as (Name, Salary). The HR department wants to sort the employees based on salary.

Task

Write a Python program to sort the employee records using a lambda expression.

Input
employees = [("Rahul",45000),("Amit",30000),("Neha",55000),("Priya",40000)]
Output
[('Amit', 30000), ('Priya', 40000), ('Rahul', 45000), ('Neha', 55000)
"""
#solution
"""
employees = [("Rahul",45000),("Amit",30000),("Neha",55000),("Priya",40000)]
b=sorted(employees,key=lambda x:x[1])
print(b)
"""
#orr
"""
m=[]
for i in range(3):
    n=input("enter name")
    i=int(input("enter salary"))
    m.append((n,i))
b=sorted(m,key=lambda x:x[1])
print(b)

"""

#question ==2
"""
2.
 Employee Bonus Calculation (Using filter() and map() with Lambda Expressions)


A software company wants to reward its high-performing employees with a 10% bonus. However, only employees earning ₹50,000 or more are eligible for
 the bonus.

As a software developer, your task is to:

Filter the salaries of eligible employees.
Calculate the updated salary after adding a 10% bonus.
Display the final salaries of the eligible employees.

Note: Use filter() to identify eligible employees and map() to calculate the updated salaries. Both operations must use lambda expressions.

Input Format
The first line contains an integer N, representing the number of employees.
The second line contains N space-separated salary values.
Output Format

Display the updated salaries of all eligible employees after adding a 10% bonus.

Sample Input
Enter the number of employees:
6

Enter the salaries:
35000 50000 62000 45000 70000 55000
Sample Output
Eligible Employees' Updated Salaries:
55000.0 68200.0 77000.0 60500.0
"""
#solution
"""
n=int(input("enter no of salary: "))
sa=[]
for i in range(n):
    x=int(input("enter amount: "))
    sa.append(x)
b=map(lambda x:x+x*0.1 ,filter(lambda x:x>=50000 ,sa))
print(list(b))

"""
# question ==3
"""
3.
 Online Shopping Discount (Using filter() and map() with Lambda Expressions)

An online shopping website is running a Festive Sale. Customers who purchase products worth ₹2,000 or more are eligible for a 20% discount.

As a software developer, your task is to:

Filter the prices of products that are ₹2,000 or more.
Calculate the discounted price by applying a 20% discount.
Display the final discounted prices.

Note: Use filter() to identify eligible products and map() to calculate the discounted prices. Both operations must use lambda expressions.

Input Format
The first line contains an integer N, representing the number of products.
The second line contains N space-separated product prices.
Output Format

Display the discounted prices of all eligible products.

Sample Input
Enter the number of products:
6

Enter the product prices:
1500 2500 1800 3000 4500 1200
Sample Output
Discounted Prices:
2000.0 2400.0 3600.0
"""
#solution
"""
n=int(input("enter no of product: "))
p=[]
for i in range(n):
    x=int(input("enter product prices"))
    p.append(x)
b=map(lambda x:x-x*0.20 ,filter(lambda x:x>2000 ,p))
a=list(b)
for i in a:
    print(i,end=" ")
    """
#question==4
"""
4.
Assignment: Scholarship Eligibility System (Using filter(), map(), and sorted() with Lambda Expressions)

A university is offering scholarships to students based on their academic performance.

The scholarship committee has decided on the following rules:

Only students who score 75 marks or above are eligible for the scholarship.
Eligible students will receive 5 bonus marks to reward their outstanding performance.
Finally, the updated marks should be displayed in descending order.

As a software developer, your task is to automate this process using Python.

Note: Use filter() to select eligible students, map() to add the bonus marks, and sorted() to display the final marks in descending order. All three operations must use lambda expressions.

Task

Write a Python program that:

Filters students who have scored 75 or above.
Adds 5 bonus marks to each eligible student.
Sorts the updated marks in descending order.
Displays the final list of scholarship marks.
Input Format
The first line contains an integer N, representing the number of students.
The second line contains N space-separated marks.
Output Format

Display the updated scholarship marks in descending order.

Sample Input
Enter the number of students:
8

Enter the marks:
65 80 92 74 88 76 55 95
Sample Output
Scholarship Marks:
100 97 93 85 81
"""
# solution
"""
n=int(input("enter no of students: "))
m=[]
for i in range(n):
    x=int(input("enter marks: "))
    m.append(x)
b=sorted(map(lambda x:x+5 ,filter(lambda x:x>=75,m)),reverse=True)
print("scholarship marks: ")
for i in b:
    print(i,end=" ")
    """
# recursion 

#question==1
"""
Assignment 1: Smart Street Lights (Fibonacci Series)

A smart city installs street lights in a newly developed area. The number of lights installed each month follows the Fibonacci pattern.

Month 1 → 0 lights
Month 2 → 1 light
Every following month, the number of lights installed is the sum of the previous two months.

As a software developer, your task is to help the city planning department generate the installation schedule.

Task

Write a recursive function to print the first N Fibonacci numbers.

Inputs
Enter the number of months:
7
Output
0 1 1 2 3 5 8
"""