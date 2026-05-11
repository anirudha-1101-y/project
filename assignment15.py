 #question==1
"""
1.Leap Year Event Scheduler – Multi-Year Analysis System

A city event management system schedules special festivals only in leap years.

To plan future events, the system analyzes multiple years instead of just one.

Write a program to:

- Read start year and end year from user
- For every year in the range, check whether it is a Leap Year or Not 
- Apply rules:
    - Divisible by 4 → Leap Year candidate  
    - Divisible by 100 → Not Leap Year  
    - Divisible by 400 → Leap Year  

- If leap year → print year with "Event Scheduled"
- Else → print year with "No Event"

- After checking all years:
    - Count total leap years
    - Print total events scheduled

Input:
2000
2005

Output:
2000 → Event Scheduled
2001 → No Event
2002 → No Event
2003 → No Event
2004 → Event Scheduled
2005 → No Event
"""
"""

y1=int(input("enter your first year:"))
y2=int(input("enter the second year"))
count=0
for i in range(y1,y2+1):
    if i%400==0 or i%4==0 or i%100==0:
        print("event scheduled",i)
        count=count+1
    
   
    else:
         print(i,"no event")


"""
#question==2
"""
a=0

b=1
n=int(input("enter the no"))
for i in range(1,n-1):
    if a==0:
        print(a)
        print(b)
    c=a+b
    print(c)
    a=b
    b=c
"""
#question==3                    doubt
"""

a=0

b=1
sum=a+b
count=0
n=int(input("enter the no"))
for i in range(1,n-1):
    if a==0:
        print(a)
        print(b)
    c=a+b
   
    if c>5:
        count+=1
    print(c)
    sum=sum+c
    a=b
    b=c
print("total population==",sum)
print("month with population>5:",count)
    
"""
#question==4
"""
n=int(input("enter the n0"))
sum=0
p=1
while n>0:
    rem=n%10
    sum=sum+rem
    p=p*rem
    n=n//10
print(sum)
print(p)
if sum==p:
    print("spy no")
else:
    print("not a spy no")

"""
"""
n=int(input("enter the n0"))
sum=0
p=1
l=len(str(n))
for i in range(1,l+1):
    rem=n%10
    sum=sum+rem
    p=p*rem
    n=n//10
print(sum)
print(p)
if sum==p:
    print("spy no")
else:
    print("not a spy no")

"""
#question==5
"""
n=int(input("enter the no"))
l=len(str(n))
if n%(10**l)==n:
    print("automorphic no")
else:
    print("not automorphic no")
"""
#question==6
"""
n=int(input("enter the no"))

if n%10==7 or n%7==0:
    print("buzz no")
else:
    print("not buzz no")
"""
#question==7
"""
n=int(input("enter the no"))
rev=0
revv=0
m=n**2
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
p=rev**2
while m>0: 
    rem=m%10
    revv=revv*10+rem
    m=m//10
if p==revv:
    print("adam no")
else:
    print("no adam no")


"""
#question==8
"""
n=int(input("enter the vlue"))
d=n**3
l=len(str(n))

if d%(10**l)==n:
    print("triorpjic no:")
else:
    print("not")

"""

#question==9
"""
n=int(input("enter the no"))
sum=0
i=1
while i<=n//2:
    if n%i==0:
        sum=sum+i
        print(i)
    i=i+1
if sum>=n:
    print("abumdant no")
else:
    print("not abundant no")

"""
#question==10
"""
n=int(input("enter the no of house"))
h=0
sum=0
for i in range(1,n+1):
    u=int(input("enter the unit"))
    if u<=100:
         bill=u*5
    elif 100<u<=200:
         bill=500+(u-100)*7
    else:
         bill=1200+(u-200)*10
    if bill>2000:
         bill=bill+(0.1*bill)
    if u<50:
         bill=bill-100
    sum=sum+bill
    if bill>h:
         h=bill
    print("house",i,"bill=",bill)
print("total collection=",sum)
print("highestbill",h)

"""












































