#question==1


#WAP to find out the sum of all integer between 100 and 200 which are divisible by 9
"""
n1=int(input("enter first no:"))
n2=int(input("enter second no:"))
sum=0
for i in range(n1,n2+1):
    
    if i%9==0:
        print(i)
        sum=sum+i
print("sum=",sum)
""" 
#question==2
#2 WAP to print Square, Cube and Square Root of all numbers from 1 to N

"""
import math
n=int(input("enter no:"))
ch=int(input("enter your choice:"))
match ch:
    case 1:
        print(n**2)
    case 2:
        print(n**3)
    case 3:
        print(math.sqrt(n))
   
 """   
"""
import math
n=int(input("enter no"))
i=1
while i<=n:
    print("square=",i**2,"cube=",i**3,math.sqrt(i))
    i=i+1
    
"""

#question==3

#3 WAP to find out all the leap years between two entered years
"""
n=int(input("enter start year:"))
m=int(input("enter last year:"))
for i in range(n,m+1):
    if i%100==0:
        if i%400:
            print(i)
    else:
        if i%4==0:
      
            print("leap year",i)

"""
#question==4
"""
1
00
111
0000
11111
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if i%2==0:
            print("0",end="")
            
        else:
            print("1",end="")
        j=j+1
    i=i+1
"""

#question==5
"""
A
AB
ABC
ABCD
ABCDE
"""
"""
n=int(input("enter no"))
i=1
while i<=n:
    print()
    j=1
    ch=65
    while j<=i:
        print(chr(ch),end="")
        ch=ch+1
        j=j+1
    i=i+1
"""
#question==6
"""
a
ab
abc
abcd
abcde

"""
"""
n=int(input("enter no:"))
i=0
while i<=n:
    print()
    j=1
    ch=97
    while j<=i:
        print(chr(ch),end="")
        ch=ch+1
        j=j+1
    i=i+1

"""

#question==7
"""

n=int(input("enter no:"))
i=1
while i<=n:
    print()
    space=1
    while space<=n-i:
        print(" ",end="")
        space=space+1
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    i=i+1
 """
"""
#question==8
n=int(input("enterno:"))
i=1
while i<n:
    print()
    space=0
    j=n
    while space<i:
        print(" ",end="")
        space=space+1
   
    while j>=i:
        print(j,end="")
        j=j-1
    i=i+1
    """
#question==9
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    space=1
    while space<=n-i:
      
        print(" ",end="")
        space=space+1
    j=1
    while j<=i:
        if j%2==0:
            print("0",end="")
        else:
            print("1",end="")
        j=j+1
    i=i+1
 """

#question==10
"""
n=int(input("enter no:"))
i=1
while i<n:
    print()
    j=0
    while j<i:
        print(j,end="")
        j=j+1
    i=i+1
 
   """















    














