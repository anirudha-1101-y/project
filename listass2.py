"""
1.
Mountain Hiking Elevation Analysis

Problem Statement

A trekking company records the elevation (in meters) reached by a hiker at different checkpoints during a mountain climb.

A checkpoint is considered a peak checkpoint if its elevation is not smaller than its adjacent checkpoints.

Given an array elevation[] of size N, find the index of any one peak checkpoint.

Test Case 1

Input:
elevation = [1200, 1450, 1700, 1600, 1500]

Output:
2

Explanation:
1700 is greater than both adjacent values 1450 and 1600.

Test Case 2

Input:
elevation = [800, 900, 950, 1000]

Output:
3

Explanation:
Last element can also be a peak because it has no right neighbor.

Test Case 3

Input:
elevation = [3000]

Output:
0

Explanation:
Single element is always a peak.

"""
"""
e=list(map(int,input("enter evalution").split()))
peak=0

if len(e)>1:
    for i in range(len(e)):
        x=e[i]
        if i==0 and x>e[1]:
            peak=i
        elif i!=0 and i!=len(e)-1:
            if x>e[i-1] and x>e[i+1]:
                peak=i
        elif i==len(e)-1 and x>e[-2]:
            peak=i
        else:
            pass
else:
    peak=0
print(peak)
"""
"""
2.
Smart City Traffic Peak Load Analyzer

Problem Statement

A smart city monitors traffic density at different time intervals in a day.

An element is called a peak traffic point if it is greater than or equal to its adjacent elements.

You are given an array traffic[] of size N.

Tasks:

Find all peak elements
Calculate the sum of all peak traffic values
Find the product of all peak traffic values
Return the maximum peak value

Note:
If only one element exists, it is the only peak.

Test Case 1

Input:
traffic = [10, 50, 30, 70, 60, 90, 80]

Output:
Peaks = [50, 70, 90]
Sum = 210
Product = 315000
Max Peak = 90

Test Case 2

Input:
traffic = [100, 200, 150, 180, 170]

Output:
Peaks = [200, 180]
Sum = 380
Product = 36000
Max Peak = 200

Test Case 3

Input:
traffic = [5]

Output:
Peaks = [5]
Sum = 5
Product = 5
Max Peak = 5
"""
"""
e=list(map(int,input("enter your element").split()))
peak=[]
if len(e)>1:
    for i in range(len(e)):
        x=e[i]
        if i==0 and x>e[1]:
            peak.append(x)
        elif i!=0 and i!=len(e)-1:
            if x>e[i-1] and x>e[i+1]:
                peak.append(x)
        elif i==len(e)-1 and x>e[-2]:
            peak.append(x)
        else:
            pass
else:
    peak.append(e[0])
print("peak=",peak)


if len(peak)>1:
    sum=1
    add=0
    for i in peak:
        sum=sum*i
        add=add+i
        m=max(peak)
else:
    sum=peak[0]
    add=peak[0]
    m=peak[0]
print("product=",sum) 
print("sum =",add)
print("maximum=",m)
"""
"""
3.
Industrial Sensor Peak Energy Monitoring System

Problem Statement

A factory machine records energy consumption at regular intervals.

A peak is defined as a value greater than or equal to its neighbors.

Tasks:

Find all peak energy values
Compute sum of squares of peak values
Compute average of peak values
Return difference between max peak and min peak
If no peaks, return -1

Test Case 1

Input:
energy = [20, 40, 30, 60, 50]

Output:
Peaks = [40, 60]
Sum of squares = 5200
Average = 50
Difference = 20

Test Case 2

Input:
energy = [10, 20, 15, 25, 20, 30]

Output:
Peaks = [20, 25, 30]
Sum of squares = 1525
Average = 25
Difference = 10

Test Case 3

Input:
energy = [5]

Output:
Peaks = [5]
Sum of squares = 25
Average = 5
Difference = 0
"""
"""
e=list(map(int,input("enter element=").split()))
p=[]
if len(e)>1:
    for i in range(len(e)):
        x=e[i]
        if i==0 and x>e[1]:
            p.append(x)
        elif i!=0 and i!=len(e)-1:
            if x>e[i-1] and x>e[i+1]:
                p.append(x)
        elif i==len(e)-1 and x>e[-2]:
            p.append(x)
        else:
            pass
else:
    p.append(e[0])
print("peak=",p)
av=0
d=0
sq=0
for i in p:
    sq=sq+i*i
    av=(av+i)
    d=max(p)-min(p)
print("sum of squres",sq)
print("average",av//len(p))
print("diffrence",d)
    

"""
"""
4.

Problem: Sum of Leaders in an Array After Filtering Invalid Data (Python)

Definition

A company collects daily performance scores of employees. However, the dataset may contain invalid entries.

An element is called a leader if:

It is greater than all elements to its right side
The element must be valid, i.e., it should not be:
Negative number
Zero

Rightmost valid element is always considered a leader.

Input Format
First line → integer n
Second line → n space-separated integers

Output Format
Single integer → sum of all valid leader elements
If no valid elements exist → return -1

Rules
Before finding leaders:

Ignore all negative values and zeros
Work only on positive numbers
Then find leaders from the filtered sequence

Test Case 1

Input:
8
16 0 17 4 -3 3 5 2

Processing:
Filtered array:
[16, 17, 4, 3, 5, 2]

Leaders:
[17, 5, 2]

Output:
24

Test Case 2

Input:
6
-1 0 -5 0 -2 -3

Output:
-1

Test Case 3

Input:
5
10 20 30 40 50

Processing:
Filtered array:
[10, 20, 30, 40, 50]

Leaders:
[50]

Output:
50

"""
"""
e=list(map(int,input("enter element=").split()))
p=[]
if len(e)>1:
    for i in e:
        if i>0: 
            if i not in p:
                p.append(i)
    print(p)
else:
    print(-1)


pp=[]
if len(p)>0:
     for i in range(len(p)):
        x=p[i]
        if i==0 and x>p[i]:
            pp.append(x)
        elif i!=0 and i!=len(p)-1:
            if x>p[i-1] and x>p[i+1]:
                pp.append(x)
        elif i==len(p)-1:
            pp.append(x)
        else:
            pass
     print(pp)
     sum=0
     for i in pp:
        sum=sum+i
     print(sum) 
else:
    print(-1)

"""
"""
5.
Given an unsorted array arr[] of size N having both negative and positive integers. 
The task is place all negative element at the end of array without changing the order of positive element and negative element.

Example 1:
Input : 
N = 8
arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
Output : 
1  3  2  11  6  -1  -7  -5

Example 2:
Input : 
N=8
arr[] = {-5, 7, -3, -4, 9, 10, -1, 11}
Output :
7  9  10  11  -5  -3  -4  -1
"""
"""
n=int(input("enter noof element"))
arr=[]
for i in range(n):
    x=int(input("enter element= "))
    arr.append(x)
print(arr)
p=[]
n=[]
for i in arr:
    if i>=0:
        p.append(i)
    else:
        n.append(i)
r=p + n
print(r)
"""
"""
6.

A security system logs employee entry IDs during a day.

Only prime-numbered IDs are considered valid VIP entries.

Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)

Example 1

Input:
[12, 5, 7, 9, 11, 14, 17]

Output:
Prime IDs = [5, 7, 11, 17]
Sum = 40
Max = 17
Count = 4

Example 2

Input:
[4, 6, 8, 10]

Output:
Prime IDs = []
Sum = 0
Max = -1
Count = 0
"""
"""
e=list(map(int,input("enter your element").split()))
np=[]
p=[]
for i in e:
    if i<2:
        np.append(i)
    else:
        x=1
    
        for j in range(2,i):
            if i%j==0:
                x=0
            
        if x==1:
            p.append(i)
        else:
            np.append(i)

print(p)
if len(p)>=1:
    m=p[0]
    sum=0
    c=0
    for i in p:
        c=c+1
        sum=sum+i
        if m<i:
            m=i
    print(p)
    print("sum",sum)
    print("max",m)
    print("count",c)
else:
    print("primr id []")
    print("sum 0")
    print("max -1")
    print("count 0")
"""
"""
7.
Factory Production – Factorial Expansion List

Problem Statement

A factory produces items where production capacity is defined using factorial growth.

Given a list of numbers, replace each number with its factorial value.

Then perform analysis on the resulting list.

Tasks:

Convert each element to factorial
Find sum of all factorial values
Find maximum factorial value
Count how many factorial values are even

Input:
A list of integers

Example 1

Input:
[3, 4, 5]

Processing:
3! = 6
4! = 24
5! = 120

Output:
[6, 24, 120]
Sum = 150
Max = 120
Even Count = 
"""
"""
e=list(map(int,input("enter your list").split()))
f=[]

for i in e:
    fa=1
    
    for j in range(1,i+1):
        fa=fa*j


    f.append(fa)
sum=0
max=f[0]
ev=0
print(f)
for i in f:
    sum=sum+i
    if max<i:
        max=i
    if i%2==0:
        ev=ev+1
print("sum",sum)
print("max",max)
print("even count",ev)
"""
