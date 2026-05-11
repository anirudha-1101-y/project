#question==1
"""
input:
name= Devendra anirudh {use split function}
age,n= 20 45 {use map funtion }

output:{give three output simple , f string , dot format}
Hello!
My name is Devendra and my friend name is anirudh
my age is 20 and my favorite number is 45
and sum = 65 and multiply = 900 and difference = 25
"""
"""
x,y=input("enter your name:").split()
a,n=map(int, input("enter your age:").split())
print("my name is ",x,"my friend name is",y)
print("my age is ",a,"my favorite no is",n)
print(f"my name is {x} my friend name is {y}")
print(f"my age is {a} my favorite no is{n}")
print("sum =",a+n,"multply=",a*n,"diffrence",abs(a-n))

print(f"sum ={a+n} multply{a*n}diffrence{abs(a-n)}")
"""


#today we learn pattern problen 
#question==1
"""
1
12
123
1234
12345
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    i=i+1
"""
"""
n=int(input("enter no:"))
for i in range(1,n+1):
    print()
    for j in range(1,i+1):
        print(j,end="")
"""
#question==2
"""
54321
4321
321
21
1
"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    j=i
    while j>=1:
        print(j,end="")
        j=j-1
    i=i-1
"""
"""

n=int(input("enter no:"))
for i in range(n,0,-1):
    print()
    for j in range(i,0,-1):
        print(j,end="")

"""
#question==3
"""
12345
2345
345
45
5
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=i
    while j<=5:
        print(j,end="")
        j=j+1
    i=i+1
"""
#question==4
"""
1
22
333
4444
55555
"""
"""
n=int(input("enter no"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        print(i,end="")
        j=j+1
    i=i+1
"""
#question==5
"""
1
**
3333
****
55555

"""
"""

n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if i%2==0:
            print("*",end="")
        else:
            print(i,end="")
        j=j+1
    i=i+1
 """

#question==6
"""
1
**
123
**
12345
"""
"""
n=int(input("enter no:"))
for i in range(1,n+1):
    print()
    for j in range(1,i+1):
        if i%2==0:
            print("*",end="")
        else:
            print(j,end="")
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if i%2==0:
            print("*",end="")
        else:
            print(j,end="")
        j=j+1
    i=i+1

"""
#question==7
"""
1
1*
1*3
1*3*
1*3*5

"""
"""
n=int(input("enterno:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if j%2!=0:
            print(j,end="")
        else:
            print("*",end="")
        j=j+1
    i=i+1


"""
#question==8
"""
1
23
456
78910
1112131415

"""
"""
n=int(input("enter no:"))
i=1
k=1
while i<=n:
    print()
    j=1
   
    while j<=i:
        print(k,end=" ")
        
        j=j+1
        k=k+1
    i=i+1

"""

#question==9
"""
1**********1
12********21
123******321
1234****4321
12345**54321
123456654321
"""
"""

n=int(input("enter no:"))
i=1
while i<=n:
    print()

    j=1
    while j<=i:
        print(" ",end="")
        j=j+1

    space=1
    while space<=(n-i)*2:
        print("*",end="")
        space=space+1

    k=i
    while k>=1:
       print(" ",end="")
       k=k-1
    i=i+1
  
"""
"""
n=int(input("enter no:"))
for i in range(1,n+1):
    print()
    j=1
    for j in range(1,i+1):
        print(j,end="")
    s=1
    for s in range(1,((n-i)*2)+1):
        print("*",end="")
    d=i
    for d in range(i,0,-1):
         print(d,end="")
"""


#question==10
"""
    1
   12
  123
 1234
12345
"""
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
        print(j,end="")
        j=j+1
    i=i+1
""" 


































        