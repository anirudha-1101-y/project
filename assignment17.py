#question==1
"""
1. Adjacent Digit Difference Analyzer

A system analyzes differences between consecutive digits in a number.

Write a program to:

Find the difference between every pair of adjacent digits
Display all differences
Count how many differences are even
Find the largest difference
If all differences are same → print Uniform Difference
Else → print Non-Uniform Pattern

Input:
84261

Output:
Differences: 4 2 4 5
Even Differences Count = 3
Max Difference = 5
Non-Uniform Pattern
"""
"""
n=int(input("enter the no"))

rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10


print("reverse ",rev)
c=rev%10
rev=rev//10
l=0
count=0

while rev>0:
    rem=rev%10
    
    d=abs(c-rem)
    c=rem
    print(d,end=" ")
    rev=rev//10
    if rem%2==0:
        count=count+1
    if l<d:
        l=d
    
print("even count",count)
print("max diffrence",l)

"""


#questiom==2
"""

A validation system checks symmetry in digit sums.

Write a program to:

Split number into two halves
Find sum of first half digits
Find sum of second half digits
Display both sums
If both sums are equal → print Balanced Number
Else → print Unbalanced Number

Input:
123321

Output:
First Half Sum = 6
Second Half Sum = 6
Balanced Number
"""
"""
n=int(input("enter the no"))

len=len(str(n))
l=len//2
if len%2==0:
    ls=n//(10**l)
    rs=n%(10**l)
    sum1=0
    sum2=0
    while ls>0:
        r=ls%10
        sum1=sum1+r
        ls=ls//10
    while rs>0:
        r=rs%10
        sum2=sum2+r
        rs=rs//10
    print("sum of fist half",sum1)
    print("sum of second half",sum2)
    if sum1==sum2:
       print("balance no")
    else:
       print("unbalance no")
else:
    print("please enter even series odd no is not divided in half")
 """


#question==5
"""
Tech Number Checker

A number is called a Tech Number if:

It has even number of digits
Split it into two equal halves
Add both halves
Square the sum
If result equals original number → Tech Number

Write a program to:

Count digits
If digits are even, split the number
Find sum of both halves
Square the sum
Display intermediate values
Check and print result

Input:
2025

Output:
First Half = 20
Second Half = 25
Sum = 45
Square = 2025
Tech Number

"""
"""
n=int(input("enter the no"))
len=len(str(n))
l=len//2
sum1=0
sum2=0
if len%2==0:
    fh=n//(10**l)
    sum1=sum1+fh
    sh=n%(10**l)
    sum2=sum2+sh
    sum=sum1+sum2
    print("sum ",sum)
    s=sum*sum
    print("square",s)


    if s==n:
        print("tech no")
    else:
        print(" non tech no")
else:
    print("please enter even digit")

"""
#question==4
"""
A system analyzes the gap between consecutive digits.

Write a program to:

Traverse digits from left to right
Find the absolute difference between current digit and next digit
Display each difference
Count how many differences are greater than 2
Find the maximum difference
If all differences ≤ 2 → print Smooth Number
Else → print Irregular Pattern

Input:
86421

Output:
Differences: 2 2 2 1
Count (>2) = 0
Max Difference = 2
Smooth Number

"""
"""
n=int(input("enter the no"))
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("reverse no:",rev)
l=0
count=0
c=rev%10
rev=rev//10
while rev>0:
    rem=rev%10
    d=abs(c-rem)
    c=rem
    print(d,end=" ")
    rev=rev//10
    if d>2:
        count=count+1
    if l<d:
        l=d
print()
print("count(>2)",count)
print("max diffrence",l)
if count==0:
    print("smooth number")
else:
    print("not smooth no")

"""



















    





















    
    
