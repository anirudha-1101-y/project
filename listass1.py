"""
1.Student Marks Management
Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75

Test Cases:

Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3
"""
#n=int(input("enter no list element"))
"""
stu=[]
for i in range(n):
    x=input("enter not of stuent")
    stu.append(x)
print(stu)
"""
"""
marks=[]
for i in range(n):
    y=int(input("enter marks"))
    marks.append(y)
print(marks)
max=0
min=marks[0]
for i in marks:
    if i>max:
        max=i
for i in range(n):
    ch=marks[i]
    if min>ch:
        min=ch
c=0
for i in marks:
    if i>=75:
        c=c+1


    
print("maximum marks",max,"min marks",min,"count above",c)

"""

#question==2
"""
2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []

"""
"""
n=int(input("enter no of element"))
s=[]
for i in range(n):
    
    x=int(input("enter your salary="))
    s.append(x)
print(s)
su=0
for i in s:
    su=su+i
av=su/n

for i in s.copy():
    if i>=av:
        if i>av:
            print("above average",i)
        

for i in s.copy():
    if i<15000:
        s.remove(i)
print("reamining list =",s)
"""

"""
3.
# Assignment: Prime Number Analyzer using List (Python)

## Scenario

A coaching institute stores student lucky numbers in a Python List.
Your task is to analyze the list and identify prime numbers for a scholarship selection process.

You must iterate through every element of the list and perform prime number analysis.

---

# Requirements

Write a Python program to:

1. Store integer values in a List
2. Iterate through all elements of the List
3. Check whether each number is prime or not
4. Display all prime numbers
5. Count total prime numbers
6. Count total non-prime numbers
7. Find the largest prime number from the List
8. Store all prime numbers into another List
9. Sort the prime numbers in ascending order and display them

---

# Test Case 1

## Input

[2, 3, 4, 5, 6, 7, 8]

## Expected Output

Prime Numbers: 2 3 5 7
Prime Count: 4
Non-Prime Count: 3
Largest Prime Number: 7
Prime List: [2, 3, 5, 7]
Sorted Prime List: [2, 3, 5, 7]

---

# Test Case 2

## Input

[10, 11, 12, 13, 14, 15]

## Expected Output

Prime Numbers: 11 13
Prime Count: 2
Non-Prime Count: 4
Largest Prime Number: 13
Prime List: [11, 13]
Sorted Prime List: [11, 13]

---

# Test Case 3

## Input

[1, 2, 17, 19, 20, 25]

## Expected Output

Prime Numbers: 2 17 19
Prime Count: 3
Non-Prime Count: 3
Largest Prime Number: 19
Prime List: [2, 17, 19]
Sorted Prime List: [2, 17, 19]

---

# Test Case 4

## Input

[4, 6, 8, 9, 10]

## Expected Output

Prime Numbers: None
Prime Count: 0
Non-Prime Count: 5
Largest Prime Number: Not Available
Prime List: []
Sorted Prime List: []

---

# Test Case 5

## Input

[29, 31, 37, 41]

## Expected Output

Prime Numbers: 29 31 37 41
Prime Count: 4
Non-Prime Count: 0
Largest Prime Number: 41
Prime List: [29, 31, 37, 41]
Sorted Prime List: [29, 31, 37, 41]
"""
"""
n=int(input("enter no of element ="))
arr=[]
for i in range(n):
    x=int(input("enter elenment="))
    arr.append(x)
print(arr)
p=[]
np=[]
c=0
for i in arr:
    if i<2:
        np.append(i)
        c=c+1
        continue
    x=0
    
    for j in range(2,i):
        if i%j==0:
            x=1
            c=c+1
            break
        
            
    if x==0: 
        p.append(i)
    else:
        np.append(i)

if len(p)>0:
    a=p[0]
    for i in p:
       if a<i:
        a=i
    print("largest element",a)

print("prime list",p)
print("prime count",len(arr)-c)
print("non prime count",c)
print("sorted prime list",sorted(p))
if len(p)>0:
    a=p[0]
    for i in p:
       if a<i:
        a=i
    print("largest element",a)

print("non prime list",np)

"""
"""
4.
Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]

"""
"""
n=int(input("enter no of list element="))
arr=[]
for i in range(n):
    x=int(input("enter element="))
    arr.append(x)
print("list",arr)
p=[]
np=[]
for i in arr:
    rev=0
    a=i
    j=i
    while j>0:
        r=j%10
        rev=rev*10+r
        j=j//10
        
    if i==rev:
        p.append(i)
    else:
        np.append(i)
print("palindrome list",p)
print("paindrome count",len(p))
if len(p)>0:
    a=p[0]
    for i in p:
        if a<i:
            a=i
    print("maximum palindome no",a)
print("sorted",sorted(p))
"""
"""
5.
 Student Grade Classification System (Python List Assignment)


A school stores student marks in a list. The system must analyze the marks and generate a *clear performance report* 
by grouping students into grade categories.



Write a Python program to:

* Iterate through the list of marks
* Assign grades based on marks:

  * *>= 90 → A*
  * *>= 75 and < 90 → B*
  * *>= 50 and < 75 → C*
  * *< 50 → Fail*
* Store each category in separate lists
* Count students in each category
* Display a *final structured report (important)*

---

## 📌 Output Format (Mandatory)

Your output must be displayed exactly in this format:


===== STUDENT GRADE REPORT =====

A Grade Students   : [list]
B Grade Students   : [list]
C Grade Students   : [list]
Fail Students      : [list]

--------------------------------
A Count   : X
B Count   : X
C Count   : X
Fail Count: X
--------------------------------

Total Students: X


---

 Input

[95, 82, 67, 45, 30]

Output


===== STUDENT GRADE REPORT =====

A Grade Students   : [95]
B Grade Students   : [82]
C Grade Students   : [67]
Fail Students      : [45, 30]

--------------------------------
A Count   : 1
B Count   : 1
C Count   : 1
Fail Count: 2
--------------------------------

Total Students: 5
"""
"""
print("================marks student list==================")
n=int(input("enter no of list element="))
m=[]
for i in range(n):
    x=int(input("enter element="))
    m.append(x)
print("list",m)
a=[]
b=[]
c=[]
f=[]


for i in m:
    if i>=90:
        a.append(i)
        
    elif 75<=i<90:
        b.append(i)
        
    elif 50<=i<75:
        c.append(i)
    else:
        f.append(i)
print("A grade student",a)
print("B grade student",b)
print("C grade student",c)
print("FAIL STUDENT",f)
print("A count",len(a))
print("B count",len(b))
print("C count",len(c))
print("FAIL count",len(f))

"""
"""
6.

 Frequency Count of Elements (Advanced Scenario-Based Problem)


A government survey department collects responses from different regions. Each response is stored as an integer in a list (representing selected option IDs).

The department wants to analyze:

* How many times each option was selected
* Most popular option
* Least popular option
* Detect invalid entries (negative numbers or zeros)

---

 Requirements

Write a Python program to:

1. Store survey responses in a list
2. Ignore invalid entries (≤ 0)
3. Count frequency of each valid number
4. Display frequency in sorted order
5. Find the most frequently selected option
6. Find the least frequently selected option (excluding invalid data)
7. Store frequency in a dictionary

---


NOTE:
* Avoid using built-in `Counter`

## Input Format

A list of integers representing responses.

---

# Scenario 1: Normal Survey Data

## Input

[1, 2, 2, 3, 3, 3, 4, 1, 2]

## Output


Frequency Count:
1 → 2
2 → 3
3 → 3
4 → 1

Most Frequent: 2 or 3 (tie)
Least Frequent: 4


---

# Scenario 2: Data with Invalid Entries

## Input

[1, 2, -1, 3, 0, 2, 4, -5, 3, 3]

## Output


Invalid Entries Ignored: [-1, 0, -5]

Frequency Count:
1 → 1
2 → 2
3 → 3
4 → 1

Most Frequent: 3
Least Frequent: 1 or 4


---

# Scenario 3: Highly Skewed Data

## Input

[5, 5, 5, 5, 2, 2, 1]

## Output


Frequency Count:
1 → 1
2 → 2
5 → 4

Most Frequent: 5
Least Frequent: 1


---

# Scenario 4: All Same Values

## Input

[7, 7, 7, 7, 7]

## Output


Frequency Count:
7 → 5

Most Frequent: 7
Least Frequent: 7


---

# Scenario 5: Empty / Invalid Only Data

## Input

[-1, 0, -3]

## Output


No valid data found
```
"""
"""
r=list(map(int,input("enter respone").split()))
o=[1,2,3,4]
mfc=0
mf=0
lf=0
lfc=len(r)

print("Frequency Count:")
for i in o:
    c=0
    for j in r:
        if i==j:
            c+=1
    else:
#large frequency count:

        print(i,"->",c)
        if c>mfc:
           mfc=c
           mf=str(i)
        elif c==mfc:
            mf=mf+" OR "+str(i)
        else:
            pass
#least frequency count:

        if c<lfc:
           lfc=c
           lf=str(i)
        elif c==lfc:
            mf=mf+" "+str(i)
        else:
            pass

print("Most Frequent:",mf)
print("Least Frequent:",lf)
    """