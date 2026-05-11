#question==1    triple operation
"""
1. Triple Operation Prime Verification System

A cybersecurity company generates a security score from entered access code.

Write a program to:

- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime

"""
#output

#1. Triple Operation Prime Verification System"
"""
n=int(input("enter the no:"))
temp=n
sum=0
rev=0
while n>0:
    rem=n%10
    sum=rem+sum
    rev=rev*10+rem
    n=n//10
    
print("sum of digit=",sum)
print("reverse=",rev)
d=abs(rev-temp)
print("diffrence =",d)
f=d+sum
print("final result =",f)
i=2
while i<f:
    if f%i==0:
        print("not prime no")
        break
    i+=1
else:
    print(" prime no")
"""

"""
n=int(input("enter the no:"))
temp=n
sum=0
rev=0
l=len(str(n))
for i in range(1,l+1):
    rem=n%10
    sum=rem+sum
    rev=rev*10+rem
    n=n//10
print("sum of digit=",sum)
print("reverse=",rev)
d=abs(rev-temp)
print("diffrence =",d)
f=d+sum
print("final result =",f)
m=len(str(f))
for i in range(2,m+1):
    if f%i==0:
        print("not prime no")
        break
else:
    print(" prime no")
"""
#question ==2
"""
2. Multi Stage Prime Lock System

A smart locker opens only if final derived number is prime.

Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime
"""
#output
"""
n=int(input("enter the no:"))
sum=0
p=1
while n>0:
    rem=n%10
    sum=sum+rem
    p=rem*p
    n=n//10

print("sum=",sum)
print("product=",p)
d=abs(sum-p)
print("diffrence=",d)
temp=d
count=0
while d>0:
    rem=d%10
    count=count+1
    d=d//10
print("count=",count)
f=count+temp
print("sum=",f)
i=2
while i<f:
    if f<=1:
        print("not prime no")

    else:
        if f%2==0:
            print("not a prime number")
            break
        i=i+1
else:
    print("prime number")

"""
"""
n=int(input("enter the no"))
l=len(str(n))
sum=0
count=0
temp=0
p=1
for i in range(1,l+1):
    rem=n%10
    sum=sum+rem
    p=p*rem
    n=n//10
print(sum,"sum of digit")
print(p,"product of digit")
d=abs(p-sum)
print("diff",d)
le=len(str(d))
a=d
for i in range(1,le+1):
    rem=d%10
    count=count+1
    d=d//10
print(count,"count")
f=a+count
b=len(str(f))
print(f,"final result")
for i in range(2,b+1):
    if n<=1:
        print("not prime")
    else:
        x=0
        
        if f%i==0:
                
                print("prime not")
                break
else:
    print(" prime no")


"""

#question==3
"""
3. Perfect Number Reward System

A gaming company rewards users if entered number is a Perfect Number.

(Perfect Number = sum of proper factors equals number)

Write a program using for-else loop to:

- Find sum of proper factors
- If sum equals number print Reward Unlocked
- Else print Try Again

Input:
6

Output:
Reward Unlocked

"""
"""
n=int(input("enter the no"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i

if sum==n:
    print("reward unlocked")
  
else:
    print("please try again")

"""
"""
n=int(input("enter the no"))
sum=0
i=1
while n>i:
    if n%i==0:
        sum=sum+i
    i=i+1
if sum==n:
    print("reward unlocked")
  
else:
    print("please try again")
"""



#question===4                        
"""
Unique Digit Security Scanner

A smart locker accepts only numbers whose all digits are unique.

Write a program using for-else loop to:

- Check every digit
- If any repeated digit found reject
- Else accept

Input:
57294

Output:
Valid Unique Code
"""
n=572942
s=str(n)
for i in s:
    num=n%10#2

    n=n//10#57294
    num=str(num)
    















#question==6
"""
Next Prime Cabin Number Generator

A luxury hotel gives only prime numbered cabins to VIP guests.

Manager enters the last allotted cabin number.
System must find the next available prime cabin number.

Write a program using loops.

Input:
24

Output:
Next Prime Cabin = 29
"""
"""
n=int(input("enter the no"))

while True:

    n=n+1
    for i in range(2,n//2+1):
        if n%i==0:
            print(n)
            break
    else:
        print("prime cabin number",n)
        break
"""
"""
n=int(input("enter the no"))

while True:

    n=n+1
    i=2
    while n>i:
        if n%i==0:
            print(n)
            break
        i=i+1
    else:
        print("prime cabin number",n)
        break
"""


#question==5
"""
Number Stability Analyzer

A science lab studies whether digits are in increasing order.

Write a program using for-else loop:

- If every next digit is greater than previous print Stable Number
- Else Unstable Number

Input:
12359

Output:
Stable Number

"""
"""
n=int(input("enter the no"))

s=9
while n>0:
    rev=n%10

    if rev<s:
        l=rev
    else:
        print("notstable number")
        break
    n=n//10
else:
    print("stable number")

"""
"""
n=int(input("enter the no"))

s=9
while n>0:
    rev=n%10

    if rev<s:
        s=rev
    else:
        print("notstable number")
        break
    n=n//10
else:
    print("stable number")
"""
#question==8
"""
ATM Note Counter

A bank ATM dispenses ₹100 notes.

Write a program to:

- Read withdrawal amount
- Count how many ₹100 notes needed using loop

Input:
700

Output:
Notes = 7
"""
"""
n=int(input("enter the amount"))
count=0
while n>=100:
    n=n-100
    count=count+1
print(count)
"""
"""
n=int(input("enter the amount"))
count=0
for i in range(100,n+1,100):
    n=n-100
    count=count+1
print(count)
"""
#question==9
"""
n=int(input("enter the amount"))
i=3000
while i<=n:
    print(i, end=" ")
    i=i+3000
"""
"""
n=int(input("enter the amount"))
i=3000
for i in range(3000,n+1,3000):
    print(i, end=" ")
  """  
#question==7
"""
.
 Alternate Digit Prime Checker

A math lab adds alternate digits from right side.

Write a program to:

- Find sum of alternate digits
- Check whether sum is Prime or Not

Input:
12345

Output:
Alternate Sum = 9
Not Prime.
"""
"""
n=input("enter the number")
sum=0
num=0
for i in n:
    num=num+1
    if num % 2 == 0:
        continue
    sum=sum+int(i)

print(sum)
i=2
while i<sum:
    if sum%2==0:
        print(" composite no")
        break
    i=i+1
else:
    print(" prime no")
"""
#question==10

"""
mode=int(input("enter the mode"))
n=int(input("enter stsrting pint"))
m=int(input("enter destination"))
if mode==1:
    for i in range(n,m+1):
        print(i,end=" ")
elif mode==2:
    for i in range(n,m,-1):
        print(i,end=" ")
elif mode==3:
    for i in range(0,m+1,2):
        print(i,end=" ")
else:
    for i in range(0,4):
        print("emergency alarm")
    """
    

















