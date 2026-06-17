"""
1. First Non-Repeating Number
  
Scenario

An online voting system stores vote IDs in a list.

Find the first vote ID that appears only once.

Requirements

* Read N and list elements from user
* Find the first non-repeating number
* If no such number exists, display an appropriate message

Test Case 1

Input:
[4, 5, 1, 2, 1, 2, 4]

Output:
First Non-Repeating Number = 5

Test Case 2

Input:
[7, 7, 8, 8]

Output:
No Non-Repeating Number Found
"""
"""
n=int(input("Enter the number of element: "))
arr=[]
for i in range(n):
    x=int(input("enter element"))
    arr.append(x)
print(arr)
for i in arr:
    c=0
    for j in arr:
        if i==j:
            c=c+1
    else:
        if c==1:
            print("first non repeting character",i)
            break
else:
    print("no non repeating character find")
    """
"""
2. First Repeating Number
=========================

Scenario

A security system logs employee IDs.

Find the first ID that repeats in the list.

Requirements

* Read N and list elements from user
* Find the first repeating number
* If no repeating number exists, display an appropriate message

Test Case 1

Input:
[10, 5, 3, 4, 3, 5]

Output:
First Repeating Number = 3

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Repeating Number Found
"""
"""
n=int(input("Enter the number of element: "))
arr=[]
for i in range(n):
    x=int(input("enter element"))
    arr.append(x)
print(arr)
for i in arr:
    c=0
    for j in arr:
        if i==j:
            c=c+1
    else:
        if c>1:
            print("first repeting character",i)
            break
else:
    print("no non repeating character find")
    """
"""
3. Missing Number Detector
==========================

Scenario

Numbers from 1 to N should exist in a sequence, but one number is missing.

Requirements

* Read N and list elements from user
* Find the missing number
* Assume numbers belong to the range 1 to N+1

Test Case 1

Input:
[1, 2, 3, 5]

Output:
Missing Number = 4

Test Case 2

Input:
[2, 3, 4, 5]

Output:
Missing Number = 1

Test Case 3

Input:
[1, 2, 4, 5]

Output:
Missing Number = 3
"""
"""
3. Missing Number Detector
==========================

Scenario

Numbers from 1 to N should exist in a sequence, but one number is missing.

Requirements

* Read N and list elements from user
* Find the missing number
* Assume numbers belong to the range 1 to N+1

Test Case 1

Input:
[1, 2, 3, 5]

Output:
Missing Number = 4

Test Case 2

Input:
[2, 3, 4, 5]

Output:
Missing Number = 1

Test Case 3

Input:
[1, 2, 4, 5]

Output:
Missing Number = 3
"""
"""
l=list(map(int,input("enter your list").split()))
k=1
for i in l:
    if i==k:
        pass
    else:
        print("missing no",k)
        break
    k=k+1
else:
    print("no missing value find")

"""



















"""
4. Longest Consecutive Sequence
===============================

Scenario

Find the longest sequence of consecutive numbers present in the list.

Requirements

* Read N and list elements from user
* Find the length of the longest consecutive sequence
* Display the sequence length

Test Case 1

Input:
[100, 4, 200, 1, 3, 2]

Output:
Longest Consecutive Length = 4

Explanation:
Sequence = 1, 2, 3, 4

Test Case 2

Input:
[10, 11, 12, 20]

Output:
Longest Consecutive Length = 3
"""
"""
n=int(input("Enter the number of element: "))

l=[]
for i in range(n):
    x=int(input("Enter the element "))
    l.append(x)

ls=0
for i in l:
    j=i
    c=0
    while True:
        if j in l:
           c=c+1
        else:
            break
        j=j+1
    if c>ls:
        ls=c
print("Longest Consecutive Length =",ls)
"""
"""
5. Equilibrium Index Finder
===========================

Scenario

Find an index where:

# Sum of elements on the left side

Sum of elements on the right side

Requirements

* Read N and list elements from user
* Find equilibrium index
* If not found, display message

Test Case 1

Input:
[1, 3, 5, 2, 2]

Output:
Equilibrium Index = 2

Explanation:
1 + 3 = 2 + 2

Test Case 2

Input:
[1, 2, 3]

Output:
No Equilibrium Index Found
"""
"""
n=int(input("Enter the number of element: "))

l=[]
for i in range(n):
    x=int(input("Enter the element "))
    l.append(x)
for i in range(len(l)):
    if i==0 or i==len(l)-1:
        pass
    else:
        sum1=0
        sum2=0
        for j in range(i-1,-1,-1):
             s=l[j]
             sum1+=s
        for j in range(i+1,len(l)):
             s=l[j]
             sum2+=s
        if sum1==sum2:
            print("Equilibrium Index =",i)
            break
else:
    print("No Equilibrium Index Found")
"""
"""
6. Product Except Self
======================

Scenario

For every element, calculate the product of all other elements except itself.

Requirements

* Read N and list elements from user
* Create a new list containing products
* Display the result

Test Case 1

Input:
[1, 2, 3, 4]

Output:
[24, 12, 8, 6]

Test Case 2

Input:
[2, 3, 5]

Output:
[15, 10, 6]
"""
"""
n=int(input("enter no"))
l=[]
for i in range(n):
    x=int(input("enter element: "))
    l.append(x)
print(l)
f=[]
for i in l:
    p=1
    for j in l:
        if i==j:
            pass
        else:
            p=p*j
    else:
        f.append(p)
print(f)
"""


"""
7. Array Rotation Analyzer
==========================

Scenario

Rotate the array K times towards the right.

Requirements

* Read N and list elements from user
* Read K
* Rotate the array
* Display rotated array

Test Case 1

Input:
Array = [1, 2, 3, 4, 5]
K = 2

Output:
[4, 5, 1, 2, 3]

Test Case 2

Input:
Array = [10, 20, 30, 40]
K = 1

Output:
[40, 10, 20, 30]
"""
"""
n=int(input("Enter the number of element: "))

l=[]
for i in range(n):
    x=int(input("Enter the element "))
    l.append(x)
k=int(input("Enter the rotation value "))

c=[]
for i in range(len(l)-k):
    s=l[i]
    c.append(s)

r=[]
for i in range(len(l)-k,len(l)):
    s=l[i]
    r.append(s)

final=r+c
print(final)
"""
"""
8. Majority Element Detector
============================

Scenario

Find an element occurring more than N/2 times.

Requirements

* Read N and list elements from user
* Find majority element
* If not present, display appropriate message

Test Case 1

Input:
[2, 2, 1, 2, 3, 2, 2]

Output:
Majority Element = 2

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Majority Element Found
"""
"""
n=int(input("Enter the number of element: "))

l=[]
for i in range(n):
    x=int(input("Enter the element "))
    l.append(x)


for i in l:
    c=0
    for j in l:
       if i==j:
          c=c+1
    else:
        if c>n/2:
           print("Majority Element =",i)
           break
else:
    print("No Majority Element Found")
"""
"""
9. Happy Number List Analyzer
=============================

Scenario

Store numbers in a list and identify Happy Numbers.

A number is called Happy if repeatedly replacing it by the sum of squares of its digits eventually becomes 1.

Example

19

1² + 9² = 82

8² + 2² = 68

6² + 8² = 100

1² + 0² + 0² = 1

Therefore, 19 is a Happy Number.

Another Example

7

7² = 49

4² + 9² = 97

9² + 7² = 130

1² + 3² + 0² = 10

1² + 0² = 1

Therefore, 7 is a Happy Number.

Non-Happy Number Example

4

4² = 16

1² + 6² = 37

3² + 7² = 58

5² + 8² = 89

8² + 9² = 145

1² + 4² + 5² = 42

4² + 2² = 20

2² + 0² = 4

Again 4 appears and the cycle repeats.

Therefore, 4 is NOT a Happy Number.

Requirements

* Read N and list elements from user
* Find all Happy Numbers
* Store Happy Numbers in another list
* Count Happy Numbers
* Find Largest Happy Number
* Display Happy Number List

Test Case 1

Input:
[19, 7, 4, 20]

Output:
Happy Numbers = [19, 7]
Count = 2
Largest Happy Number = 19

Test Case 2

Input:
[13, 10, 4]

Output:
Happy Numbers = [13, 10]
Count = 2
Largest Happy Number = 13

Test Case 3

Input:
[2, 3, 4]

Output:
Happy Numbers = []
Count = 0
Largest Happy Number = Not Available
"""
"""
n=int(input("Enter the number of element: "))

l=[]
for i in range(n):
    x=int(input("Enter the element "))
    l.append(x)

happy=[]
for i in l:
    if i<9:
       j=i**2
    else:
        j=i
    while True:
        if j>9:
            sum=0
            for k in str(j):
                k=int(k)
                sum=sum+k**2
            j=sum
        else:
            if j==1:
                happy.append(i)
            else:
                pass
            break
print(happy)
print("Count =",len(happy))

if len(happy)>0:
     ma=max(happy)
else:
    ma="Not Available"
print("Largest Happy Number =",ma)
"""
"""
10. Find Duplicate Numbers
Scenario
A company stores employee IDs in a list. Some IDs may appear more than once due to data entry errors.
Requirements
* Read N and list elements from user
* Find all duplicate numbers
* Store duplicates in another list
* Count total duplicate numbers
* Display duplicates in sorted order

Test Case 1

Input:
[1, 2, 3, 2, 4, 5, 1]

Output:
Duplicate Numbers = [1, 2]
Count = 2

Test Case 2

Input:
[10, 20, 30]

Output:
No Duplicate Numbers Found
"""
"""
n=int(input("Enter the number of element: "))

l=[]
for i in range(n):
    x=int(input("Enter the element "))
    l.append(x)

du=[]
for i in l:
    c=0
    for j in l:
        if i==j:
           c=c+1
    else:
        if c>1:
           if i not in du:
              du.append(i)
a=len(du)
if a>0:
    print("Duplicate Numbers =",du)
    print("Count =",a)
else:
"""