"""
cr=int(input("enter credit score: "))
el=int(input("enter exitiing loan: "))
salary=int(input("enter salary: "))
if salary>=30000:
    if cr>=750:
        print("loan should approved")
    else:
        if el<2:
            print("loan should be conditionally approved")
        else:
            print("reject")
else:
    print("reject")
    """
#palindrome
"""
n=int(input("enter no"))
t=n

rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10

if rev==t:
    print("palindrome")
else:
    print("not palindrome")
"""
"""
4. Electricity Bill Management System

You are developing an Electricity Bill Management System for a power distribution company. The system helps calculate electricity bills for customers based on their unit consumption.

Sometimes, the operator may try to calculate the bill or apply surcharge before entering the number of units consumed. Your system must handle such situations properly.

👉 Important Condition:
If units are not entered, the system should display:
"Please enter units consumed first"
and should not perform further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Units Consumed
2 → Calculate Bill Amount

* First 100 units → ₹5 per unit
* Next 100 units → ₹7 per unit
* Above 200 units → ₹10 per unit
  3 → Apply Surcharge
* If bill > 2000 → 10% surcharge
* Otherwise → 5% surcharge
  4 → Display Final Bill
  5 → Exit
  """
"""
x=0
while True:
    print("menu")
    print("1 → Enter Units Consumed")
    print("2 → Calculate Bill Amount")
    print(" 3 → Apply Surcharge")
    print("4 → Display Final Bill")
    print("exit")
    ch=int(input("enter your choice: "))
   
    match ch:
        case 1:
            unit=int(input("enter your unit:"))
            x=1
        case 2:
            if x==0:
                print("pls enter unit fiest")
            else:
                if unit<=100:
                    b=5*unit
                elif 101<unit<200:
                    b=(unit-100)*7+500
                elif unit>=200:
                    b=(unit-200)*10+1200
        case 3:
            if b>2000:
                
                c=b*10//100
            else:
                c=b*5//100
            print("surcharge=",c)
        case 4:
            print("=====final bill=========")
            print("bill=",b)
            print("sub charge",c)
            print(b+c)
        case 5:
            print("exit")
"""
"""
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
"""
"""
n=int(input("enter n"))
for i in range(1,n+1):
    print(n,"x",i,"=",n*i)
"""
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
from collections import namedtuple
employee=namedtuple("employee",["emp_id","emp_name","department","salary"])
n=int(input("enter no of emp:"))
emp=[]
for i in range(n):
    id=int(input("enter emp id"))
    name=input("enter name")
    d=input("enter deaprtement")
    s=int(input("enter salary"))
    emp.append(employee(id,name,d,s))
for i in emp:
    for j in i:
        print(j,end=" ")
    print()
#highest salary
h=0
hsi=1
for i in range(len(emp)):
    if emp[i][3]>h:
        h=emp[i][3]
        hsi=i
for j in range(len(emp[i])):
    print(emp[hsi][j],end=" ")
print()
print()
l=emp[0][3]
lsi=1
for i in range(len(emp)):
    if emp[i][3]<l:
        l=emp[i][3]
        lsi=i
for i in range(len(emp[i])):
    print(emp[hsi][j],end=" ")
print()
