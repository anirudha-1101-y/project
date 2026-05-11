print("hello")
#question=1         puzzel of odd no up to N
"""
n=int(input("enter your no:"))
sum=1
for i in range(1,n+1):
    if i%2==1:
        sum=sum*i
print("no is :",sum)
"""
"""
n=int(input("enter the no"))
sum=1
i=1
while n>=i:
    if i%2==1:
        sum=sum*i
    i=i+1
print("no is :",sum)

"""

#question =2           count no divisible by 7
"""
n1=int(input("enter the start no:"))
n2=int(input("enter ending no:"))
count=0
for i in range(n1,n2):
    if i%7==0:
        count+=1
print("no divisible by7:",count)
"""


#question==3          display number ending with 5
"""
n1=int(input("enter the first no:"))
n2=int(input("enter the second no:"))
sum=0
for i in range(n1,n2+1):
    if i%10==5:
        print(sum+i,end=" ")

"""
"""
n1=int(input("enter the first no:"))
n2=int(input("enter the second no:"))
sum=0

i=n1
while i<=n2:
    if i%10==5:
        print(sum+i,end=" ")
    i=i+1
"""




#question=4            strong number checker
"""

n=int(input("enter the no:"))

temp=n
sum=0

while n>0:
    rem=n%10
    f=1
    for i in range(1,rem+1):
        f=f*i
    sum=sum+f
    n=n//10
if sum==temp:
    print("strong no")
else:
    print("not a strong no")



"""
"""
n=int(input("enter the no:"))
l=len(str(n))
temp=n
sum=0

for i in range(1,l+1):
    rem=n%10
    f=1
    for i in range(1,rem+1):
        f=f*i
    sum=sum+f
    n=n//10
if sum==temp:
    print("strong no")
else:
    print("not a strong no")

"""

#question==5               harsad no:
"""
n=int(input("enter the no:"))
temp=n
sum=0
while n>0:
    rem=n%10
    sum=sum+rem

    n=n//10
if temp%sum==0:
    print("harshad no")
else:
    print("not a harshad no")
"""
"""
n=int(input("enter the no:"))
l=len(str(n))
temp=n
sum=0
for i in range(1,l+1):
    rem=n%10
    sum=sum+rem

    n=n//10
if temp%sum==0:
    print("harshad no")
else:
    print("not a harshad no")
"""
#question==6            automorphic number checker
"""
n=int(input("enter the no"))
l=len(str(n))
p=1
for i in range(1,l+1):
    p=p*n
if p%(10**l)==n:
    print("automorphic no")
else:
    print("not a automorphic no")


"""
"""
n=int(input("enter the no"))
l=len(str(n))
temp=n
p=1
i=1
while n>i:
    p=p*n
    i=i+1
if p%(10**l)==n:
    print("automorphic no")
else:
    print("not automorphic no")
"""
#question==7          find duck no
"""
n=int(input("enter the no:"))
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
nn=rev
a="not duck no"
while nn>0:
    nr=nn%10
    if nr==0:
        a="duck no"
        break
    nn=nn//10
print(a)
    
"""  

#question=8              mirror diffrence tracnsaction verification system
"""
n=int(input("enter the no"))
rev=0
temp=n
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print("reverse value is",rev)

if rev>temp:
    d=rev-temp
elif temp>rev:
    d=temp-rev
else:
    d=0

print("diffrence is",d)

l=len(str(d))

if d%10==0:
    print(l,"perfect match")
elif d%10==9:
    print(l,"varified")
else:
    print("reject")

    

"""
#question==9     step diffrence analyzer
"""
n=int(input("enter the no:"))
le=len(str(n))
rev=0
while n>0:
   rem=n%10
   rev=rev*10+rem
   n=n/10
print("reverse no",rev)
n1=rev
sd=0
while n1>0:
    rem1=n1%10
    n1=n1//10
    rem2=n1%10
    d=abs(rem1-rem2)
    sd=sd*10+d
    sd=sd//10
print("step diff",sd)
n2=sd
sum=0
while sd>0:
    rem3=sd%10
    sum=sum+rem3
    sd=sd//10
print("sum",sum)


l=0
while n2>0:
    r4=n2%10
    if r4>l:
        l=r4
    n2=n2//10
print("largest no",l)
if sum%le==0:
    print("balanced")
else:
    print("unbalanced")


"""





















