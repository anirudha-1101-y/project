#question==1
"""
1.
Multiplication Table Generator

Scenario:
A school learning app helps students practice multiplication tables.
The user enters a number n, and the system prints multiplication tables from 1 to n using nested loops.

Input:
Enter limit: 3

Output:
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
"""
"""
n=int(input("enter the no"))
for i in range(1,n+1):
    for a in range(1,n+1):
        print(i,"x",a,"=",a*i)
    print()
"""
"""
n=int(input("enter the no:"))
i=1
while n>=i:
    for a in range(1,n+1):
        print(a*i)
    i=i+1
    print()
"""
#question==2
"""
Perfect Number Analyzer

A mathematics research system analyzes special numbers within a given range.
The user enters a starting number and ending number.
The system checks every number in that range and displays all Perfect Numbers using nested loops.

(A Perfect Number is a number whose sum of proper divisors is equal to the number itself.)

Input:
Enter starting number: 1
Enter ending number: 1000

Output:
Perfect Numbers are:
6
28
496
"""
"""
n1=int(input("enter the starting point:"))
n2=int(input("enter the last point:"))


for i in range(n1,n2+1):
    sum=0
    for a in range(1,i):
        if i%a==0:
            sum=sum+a
       
    if sum==i:
        print("perfect no:",sum)
      
"""
#question==3
"""
3.
Prime Number Range Checker

A cyber security system generates prime numbers for encryption analysis.
The user enters a starting number and ending number.
The system checks and displays all prime numbers between the given range using nested loops.

Input:
Enter starting number: 10
Enter ending number: 50

Output:
Prime Numbers are:
11
13
17
19
23
29
31
37
41
43
47
"""
"""
n1=int(input("enter the first no:"))
n2=int(input("enter the last no:"))
for i in range(n1,n2+1):
    x=0
    if i<=1:
            continue
    for a in range(2,i):
        if i%a==0:
            x=1
            break
    else:
        if x==0:
            print("perfect no:",i)

"""
#question==4
"""
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407
"""
"""
n1=int(input("enter the first number :"))
n2=int(input("enter the last number:"))
for i in range(n1,n2+1):
    temp=i
    l=len(str(i))
    p=0
    while i>0:
        rem=i%10
        p=p+(rem**l)
        i=i//10
        
      
    if p==temp:
        print("armstrong no",p)
 """ 
    
#question==5
"""
trong Number Detector

A banking security system uses Strong Numbers for special authentication testing.
The user enters a range of numbers.
The system identifies all Strong Numbers between the given range using nested loops.

A Strong Number is a number in which the sum of factorials of its digits is equal to the original number.

Example:
145

1! + 4! + 5!
= 1 + 24 + 120
= 145

Since the sum is equal to the original number, 145 is called a Strong Number.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Strong Numbers are:
1
2
145

"""
"""
n1=int(input("enter the starting no:"))
n2=int(input("enter the ending no:"))
for i in range(n1,n2+1):
    temp=i
    sum=0
    f=1
    while i>0:
        f=1

        
        rem=i%10
        for b in range(1,rem+1):
            f=f*b
        sum=sum+f
        i=i//10
    
    if temp==sum:
        print("strong no",temp)
 """



#question==6

"""    
        
6.
Palindrome Number Range Checker

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191

"""
"""
n1=int(input("enter the starting no:"))
n2=int(input("enter the ending no:"))
for i in range(n1,n2+1):
    rev=0
    temp=i
    while i>0:
        rem=i%10
        rev=rev*10+rem
        i=i//10
    if rev==temp:
        print("palindrome no",temp)

"""
#question==7

"""
Neon Number Detector

Scenario:
A smart calculator system checks special numbers used in mathematical testing.
The user enters a range of numbers.
The system identifies all Neon Numbers using nested loops.

Theory:
A Neon Number is a number where the sum of digits of its square is equal to the original number.

Example:
9

Square of 9 = 81

8 + 1 = 9

Since the sum is equal to the original number, 9 is called a Neon Number.

Input:
Enter starting number: 1
Enter ending number: 100

Output:
Neon Numbers are:

"""
"""
n1=int(input("enter the starting no:"))
n2=int(input("enter the ending no:"))
for i in range(n1,n2+1):
    temp=i
    sum=0
    sq=i**2
    while sq>0:
        
        rem=sq%10
        sum=sum+rem
        sq=sq//10
    if temp==sum:
       print("neon sumber",temp)

"""
#question===8
"""
.
Online Exam Result Processing System

An online examination system stores marks of multiple classes.
Each class contains multiple students, and each student has marks for multiple subjects.

The program should use:
- First loop for classes
- Second loop for students
- Third loop for subjects

The system calculates total marks of every student.

Input:
Enter number of classes: 2
Enter students per class: 2
Enter subjects per student: 3

Class 1

Student 1
Enter mark: 70
Enter mark: 80
Enter mark: 90

Student 2
Enter mark: 60
Enter mark: 75
Enter mark: 85

Class 2

Student 1
Enter mark: 88
Enter mark: 77
Enter mark: 66

Student 2
Enter mark: 90
Enter mark: 92
Enter mark: 95

Output:
Class 1
Student 1 Total = 240
Student 2 Total = 220

Class 2
Student 1 Total = 231
Student 2 Total = 277

"""
"""
cla=int(input("enter the class :"))
stu=int(input("enter the students:"))
sub=int(input("enter youe marks:"))

for i in range(1,cla+1):
    print("class",i)

    for a in range(1,stu+1):
        print("student",a)
 
        for b in range(1,sub+1):
            mark=int(input("enter marks:"))
 """       
            
        














