#question ==1            prime number
"""
n=int(input("enter the no:"))

if n<=1:
    print("not a prime number")
else:
    i=2
    x=0
    while i<n:
        if n%i==0:
            x=1
            break
        i=i+1
if x==0:
    print("prime number")
else:
    print("not prime number")
"""
"""
n=int(input("enter the no:"))

if n<=1:
    print("not a prime number")
else:
    
    x=0
    for i in range(2,n):
        if n%i==0:
            x=1
            break
        
if x==0:
    print("prime number")
else:
    print("not prime number")          

"""
#question==3           composite number                                                              
"""
n=int(input("enter the no:"))

if n<=1:
    print("not a prime number")
else:
    i=2
    x=0
    while i<n:
        if n%i==0:
            x=1
            break
        i=i+1
if x==0:
    print("prime number")
else:
    print("composite number")
"""
"""
n=int(input("enter the no:"))

if n<=1:
    print("not a prime number")
else:
    
    x=0
    for i in range(2,n//2+1):
        if n%i==0:
            x=1
            break
        
if x==0:
    print("prime number")
else:
    print("composite number")

"""
"""
n=int(input("enter the no"))
for i in range(1,11):
    if n*i>50:
        break
    print(n*i)
"""

"""
i=0
while i<10:
    i=i+1
    if i==5:
        print("mil gya")
        continue
    print(i)
    
"""
"""
while True:
    n=int(input("enter the no"))
    if n<0:
        continue
    elif n==10:
        break
    else:
        print("enterred the no",n)
print("done with the loop")

"""
#question==2            
"""
n=int(input("enter the no"))
while True:
    n=n+1
    if n<=1:
       continue
    else:
        i=2
        x=0
        while i<=n//2:
            if n%i==0:
                x=1
             
            i=i+1
        if x==0:

            break
print(n)
"""
"""
n=int(input("enter the no"))
while True:
    n=n+1
print(n)
    if n<=1:
        print("not prime no")
    
    else:
        x=0
        for i in range(2,n):
            if n%i==0:
               x=1
        if x==0:
              break
"""
#question==4                check present prime no find next prime    

"""
n=int(input("enter the no:"))

if n<=1:
    print("not a prime number")
else:
    i=2
    x=0
    while i<n:
        if n%i==0:
            x=1
            break
        i=i+1
if x==0:
    print("prime number")
else:
    print("not prime number")


while True:
    n=n+1
    if n<=1:
        continue
    else:
        i=2
        x=0
        while i<=n//2:
            if n%i==0:
                x=1
                break
            i=i+1
        if x==0:
            print("next prime no",n)
            break
print(n)
    
"""
"""
n=int(input("enter the no:"))

if n<=1:
    print("not a prime number")
else:
    
    x=0
    for i in range(2,n):
        if n%i==0:
            x=1
            break
        
if x==0:
    print("prime number")
else:
    print("not prime number")


while True:
    n=n+1
    if n<=1:
        continue
    else:
        i=2
        x=0
        for i in range(2,n//2+1):
            if n%i==0:
                x=1
                break
           
        if x==0:
            print("next prime no",n)
            break
print(n)
 """  

#question==5       find gap 

"""
n=int(input("enter the no:"))
a=n
if n<=1:
    print("not a prime number")
else:
    i=2
    x=0
    while i<n:
        if n%i==0:
            x=1
            break
        i=i+1
if x==0:
    print("prime number")
else:
    print("not prime number")


while True:
    n=n+1
    if n<=1:
        continue
    else:
        i=2
        x=0
        while i<=n//2:
            if n%i==0:
                x=1
                break
            i=i+1
        if x==0:
            print("next prime no",n)
            break

print(n)
print("gap is ",n-a)

"""
"""
n=int(input("enter the no"))
a=n
if n<=1:
    print("not prime digit")
else:
    x=0
    for i in range(2,n):
        if n%i==0:
            x=1
            break
if x==0:
    print("prime no ,n")
while True:
    n=n+1
    if n<=1:
        print("not prime digit")
    else:
        x=0
        for i in range(2,n//2+1):
            if n%i==0:
                x=1
                break
        if x==0:
            print("next prime no is:",n)
            break
print("gap is",n-a)
"""


    
#{Question 6}
"""
n=int(input("enter the no"))
c=0
i=2
x=0
s=9
l=0
while i<n:
    if n%i==0:
        c+=1
        x=1
        if i<s:
            s=i
    else:
        s=0
    i+=1
if x==0:
    print("prime no")
else:
    print("composite no")
print("factors =",c)
print("smallest no =",s)

"""
"""
n=int(input("enter the no"))
c=0
i=2
x=0
s=9
for i in range(2,n):
    if n%i==0:
        c+=1
        x=1
        if i<s:
            s=i
   
    
if x==0:
    print("prime no")
else:
    print("composite no")
print("factors =",c)
print("smallest no =",s)

"""

#{Question 7}
"""
n=int(input("Enter a number: "))
sum=0
while n>0:
    r=n%10
    sum+=r
    n=n//10
print("sum",sum)
n=sum
if n<=1:
    print("Normal Number")
else:
    i=2
    x=0
    while i<=n//2:
        if n%i==0:
            x=1
        i=i+1
    if x==0:
        print("Lucky Number")
    else:
        print("Normal Number") 
"""

"""

n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    r=n%10
    sum+=r
    n=n//10
print("sum",sum)
n=sum
if n<=1:
    print("Normal Number")
else:
    i=2
    x=0
    for i in range(2,n//2+1):
        if n%i==0:
            x=1
        
    if x==0:
        print("Lucky Number")
    else:
        print("Normal Number") 
"""
#{Question 8}
"""
n=int(input("Enter the number: "))
l=0
s=9
while n>0:
    r=n%10
    if r>l:
        l=r
    if r<s:
        s=r
    n=n//10
print("Largest Number =",l)
print("Smallest number =",s)
sum=l+s
print("Sum =",sum)
n=sum
if n<=1:
    print("Not prime: ")
else:
    i=2
    x=0
    while i<=n//2:
        if n%i==0:
            x=1
        i=i+1
    if x==0:
        print("Prime number")
    else:
        print("Not Prime number") 
"""
"""
n=int(input("Enter the number: "))
l=0
s=9
for i in range(1,n+1):
    r=n%10
    if r>l:
        l=r
    if r<s:
        s=r
    n=n//10
print("Largest Number =",l)
print("Smallest number =",s)
sum=l+s
print("Sum =",sum)
n=sum
if n<=1:
    print("Not prime: ")
else:
    
    x=0
    for i in range(2,n//2+1):
        if n%i==0:
            x=1
        
    if x==0:
        print("Prime number")
    else:
        print("Not Prime number") 
"""
#{Question 9}      doubt in for loop
"""
n=int(input("Enter a number: "))
oc=0
c=0
while n>0:
    r=n%10
    if r%2==0:
        c=c+1
    else:
        oc=oc+1
    n=n//10
print("Even count =",c)
print("Odd count =",oc)
d=abs(c-oc)
print("Difference =",d)
n=d
if n<=1:
    print("Not prime")
else:
    i=2
    x=0
    while i<=n//2:
        if n%i==0:
            x=1
        i=i+1
    if x==0:
        print("Prime number")
    else:
        print("Not Prime number")

"""



























































