
#we all know for loop used for a sequesnce or a list and while loop is used for infinite #iterative

#question==1                  sum of natural no
"""
n=int(input("enter the no:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
    i+=1
print("total sum:",sum)

"""
"""
#while loop
n=int(input("input n:"))
sum=0
i=1
while n>=i:
    sum=sum+i
    i=i+1
print(sum)
"""
#question==2                  factorial
"""
n=int(input("enter the no"))
f=1
for i in range(1,n+1):
    f=f*i
print("factorial is",f)


"""
"""
n=int(input("input n"))
f=1
i=1
while n>=i:
    f=f*i
    i=i+1
print(f)
"""
#question==3                 multiplication table
"""
n=int(input("enter the no:"))

for i in range(1,11):
    print(n*i)
    i+=1
print("out")
   
"""
"""
n=int(input("entertheno"))
i=1
while i<=10:
    print(n*i)
    i=i+1
print("table completed")
    
"""



#question ==4              reverse the no
"""
n=int(input("enter the no:"))
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("reverse no is:",rev)          

or

n=int(input("enter the no:"))
rev=0
while n>0:
    rem=n%10
    
    print(rem,end="")          
    n=n//10


"""
"""
n=int(input("enter the no"))
l=len(str(n))
rev=0
for i in range(1,l+1):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)
"""
#or 
#question==5          palindrome
"""
n=int(input("enter the no:"))
rev=0
temp=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if temp==rev:
    print("palindrome")
else:
    print("not palindrome")

"""
"""
n=int(input("enter the no:"))
l=len(str(n))
rev=0
temp=n
for i in range(1,l+1):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if temp==rev:
    print("palindrome")
else:
    print("not palindrome")
"""
#question ==6        armstrong no
"""
n=int(input("enter the no"))
l=len(str(n))
temp=n
sum=0
while n>0:
    rem=n%10
    sum=sum+(rem**l)
    n=n//10
if temp==sum:
    print("armstrong no")
else:
    print("not a armstrong no")

"""
"""

n=int(input("enter the no "))
rev=0
sum=0
temp=n
l=len(str(n))
for i in range(1,l+1):
    rem=n%10
    sum=sum+(rem**l)
    n=n//10
if temp==sum:
    print("armstrong no")
else:
    print("not armstrong no")


"""
#question==7         count even no
"""
n=int(input("enter the no"))
count=0
while n>0:
    d=n%10
    if d%2==0:
        count+=1
    n=n//10
print("even digit count=",count)
       
"""
"""
n=int(input("entre the no"))
count=0
l=len(str(n))
for i in range(1,l+1):
    rem=n%10
    if rem%2==0:
        count+=1
    n=n//10
print(count)
"""
#question==8               count odd no.
"""
n=int(input("enter the no"))
count=0
while n>0:
    d=n%10
    if d%2!=0:
        count+=1
    n=n//10
print("odd digit count=",count)

"""
"""
n=int(input("entre the no"))
count=0
l=len(str(n))
for i in range(1,l+1):
    rem=n%10
    if rem%2==1:
        count+=1
    n=n//10
print(count)

"""
#question==9              check all even digit 
"""
n=int(input("enter the no:"))
flag=True
while n>0:
    rem=n%10
    if rem%2!=0:
        flag=False
    n=n//10
if flag:
    print("all are even")
else:
    print("not all are even")
"""
"""

n=int(input("enter the no"))
count=0
l=len(str(n))
for i in range(1,l+1):
    rem=n%10
    if rem%2==0:
        count+=1
    n=n//10
if l==count:
    print("all even")
else:
    print("not all even")

"""


#question=10            even number between two number
"""
n1=int(input("enter the first no:"))
n2=int(input("enter the second no:"))
for i in range(n1,n2+1):
    if i%2==0:
         print(i,end="")
"""
"""
n1=int(input("entre the no"))
n2=int(input("enter the no"))
i=n1
while i<=n2:
    if i%2==0:
        print(i, end=" ")
    i=i+1

"""
#question=11                count occurrence of a digit 
"""
n=int(input("enter number:"))
d=int(input("enter digit:"))
count=0
while n>0:
    rem=n%10
    if rem==d:
        count+=1
    n=n//10
print("repeated " ,count,"times")

"""
"""
n=int(input("enter the no"))
d=int(input("enterthe d"))
l=len(str(n))
count=0

for i in range(1,l+1):
    rem=n%10
    if rem==d:
        count=count+1
    n=n//10
print("apperar",count)


"""

#question=12             multiplication og digit
"""
n=int(input("enter the no"))
sum=1
while n>0:
    rem=n%10
    sum=sum*rem
    n=n//10
print(sum)
if sum%2==0:
    print("even")
else:
    print("odd")

"""
"""
n=int(input("enter the no"))
l=len(str(n))
sum=1
for i in range(1,l+1):
    rem=n%10
    sum=sum*rem
    n=n//10
print("sum",sum)
if sum%2==0:
    print("even")
else:
    print("odd")

"""

#question==13                       number range display
"""
n1=int(input("enter the first no:"))
n2=int(input("enter the secondno:"))
if n1<n2:
    for i in range(n1,n2+1):
        print(i,end="")
elif n1>n2:
    for i in range(n2,n1-1):
        print(i,end="")
else:
    print("both are same")


"""
#question 13        doubt for while loop                  




#question==14                   floor movement system     doubt for while loop
"""
n1=int(input("enter the first no:"))
n2=int(input("enter the secondno:"))
if n1<n2:
    for i in range(n1,n2+1):
        print(i,end="->")
elif n1>n2:
    for i in range(n1,n2-1,-1):
        print(i,end="->")
else:
    print("both are same")

"""

"""
n=int(input("Enter a number: "))
len=len(str(n))
l=len//2
if len%2==0:
    a=n//(10**l)
    print("First half =",a)
    b=n%(10**l)
    print("Second half =",b)
    sum=a+b
    print("Sum =",sum)
    s=sum**2
    print("Sqaure =",s)
    if s==n:
        print("Tech number")
    else :
        print("Not tech number")
else:
    print("enter even digit number")

"""































