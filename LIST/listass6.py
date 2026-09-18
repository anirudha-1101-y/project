"""
1. Count Pairs with Difference K

A company records the ages of employees. Find how many pairs of employees have an age difference exactly equal to K.

Problem Statement:

Given an array of employee ages and an integer K, count the number of pairs whose absolute difference is K.

Example:

Input:

N = 5
K = 2
ages[] = {1, 5, 3, 4, 2}

Output:

3

Explanation:

(1,3), (3,5), (2,4)
"""
"""
n=list(map(int,input("enter elemnet: ").split()))
k=int(input("enter diffrence: "))
c=0
for i in n:
    for j in n:
        if j-i==k:
            c=c+1
        else:
            pass
else:
    print(c)
    """
"""
2.
Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output

3

Explanation

("abc","de")
("abc","fg")
("de","fg")
"""

"""
3.MATRIX PERFORMANCE EVALUATION SYSTEM

A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

The HR department wants a menu-driven application to analyze employee performance.

Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit
Requirements
Choice 1 – Find Employee with Highest Total Score
Calculate the sum of each row.
Display the employee number having the highest total score.
Choice 2 – Find Month with Lowest Average Score
Calculate the average of each column.
Display the month having the lowest average score.
Choice 3 – Display Employee-wise Maximum Score
Find and display the maximum value present in each row.
Sample Input
10 20 30
40 50 60
25 35 45
Output
Employee 2 has Highest Total Score = 150

Month 1 Average = 25
Month 2 Average = 35
Month 3 Average = 45

Employee 1 Max Score = 30
Employee 2 Max Score = 60
Employee 3 Max Score = 45
"""
"""
while True:
    print("Menu")
    print("1. Find Employee with Highest Total Score")
    print("2. Find Month with Lowest Average Score")
    print("3. Display Employee-wise Maximum Score")
    print("4. Exit")

    rows=int(input("enter no of rows : "))
    cols=int(input("enter no of column: "))
    mat=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            x=int(input("enter element: "))
            row.append(x)
        mat.append(row)
    
    choice=int(input("enter your choice: "))
    match choice:
        case 1:
            print("output: ")
            max=0
            for i in range(len(mat)):
                sum=0
                for j in range(len(mat[i])):
                    n=mat[i][j]
                    sum=sum+n
                if sum>max:
                    max=sum
                    line=i+1
            print("employee",line,"has highest total score",max)
        case 2:
            print("output: ")
            for j in range(cols):
                sum=0
                for i in range(rows):
                    n=mat[i][j]
                    sum=sum+n
                av=sum//cols
                print("month",j+1,"avarage",av)
        case 3:
            print("output: ")
            for i in range(len(mat)):
                max=mat[i][0]
                for j in range(len(mat[i])):
                    n=mat[i][j]
                    if max<n:
                        max=n
                print("employee",i+1,"maximum no",max)
        case 4:
            print("exit")
            break
                    
"""
"""
4.
Find common elements in three sorted arrays.
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?
Example 1:
Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C
"""
"""
n1=int(input("enter no1 "))
a=[]
for i in range(n1):
    x=int(input("enter element: "))
    a.append(x)
n2=int(input("enter no1 "))
b=[]
for i in range(n2):
    x=int(input("enter element: "))
    b.append(x)
n3=int(input("enter no1 "))
c=[]
for i in range(n3):
    x=int(input("enter element: "))
    c.append(x)
r=[]
for i in a:
    for j in b:
        for k in c:
            if i==j==k:
                r.append(i)
for i in r:
    
        print(i,end=" ")
        """
"""
5.

Rearrange the array in alternating positive and negative items
Given an unsorted array Arr of N positive and negative numbers. 
Your task is to create an array of alternate positive and negative numbers 
without changing the relative order of positive and negative numbers.
Note: Array should start with positive number.

Example 1:
Input: 
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output:
9 -2 4 -1 5 -5 0 -3 2
Example 2:
Input: 
N = 10
Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output:
5 -5 2 -2 4 -8 7 1 8 0
"""
n1=int(input("enter no1 "))
a=[]
for i in range(n1):
    x=int(input("enter element: "))
    a.append(x)
print(a)
p=[]
n=[]
for i in a:
    if i>=0:
        p.append(i)
    else:
        n.append(i)
print(p)
print(n)
res=[]
i=0
j=0
while i<len(p) or j<len(p):
    res.append(p[i])
    res.append(n[j])
    i=i+1
    j=j+1
print(res)
