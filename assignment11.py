#question ==1           find the largest no
"""
n=int(input("enter the no: "))
sum=0
while n>0:
    rem=n%10
    if rem>sum:
        sum=rem
    n=n//10
print(sum,"largest no")
"""
"""
n=int(input("enter the no:"))
l=len(str(n))
sum=0
lar=0
for i in range(1,l+1):
    rem=n%10
    if rem>lar:
        lar=rem
    n=n//10
print("largest no",lar)
    """

#question==2               find sortest no
"""
n=int(input("enter the no"))
sum=9
while n>0:
    rem=n%10
    if rem<sum:
        sum=rem
    n=n//10
print("sortest no",sum)
"""

"""
n=int(input("enter the no"))
l=len(str(n))
sum=9
for i in range(1,l+1):
    rem=n%10
    if rem<sum:
        sum=rem
    n=n//10
print("sortest no",sum)

"""
#question==3                find first digit
"""
n=int(input("enter the no"))


while n>0:
    rem=n%10
    n=n//10
print(rem)
    """
"""
n=int(input("enter the no"))
l=len(str(n))

for i in range(1,l+1):
    rem=n%10
    n=n//10
print(rem)

"""
#question==4                num divisible by 3 between two no
"""
n1=int(input("enter the first no:"))
n2=int(input("enter the second no:"))

for i in range(n1,n2+1):
    if i%3==0:
    
        print(i,end=" ")

"""
#question==5                 find factor 

"""
n=int(input("enter the no:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
print("factors",count)
"""
"""
n=int(input("enter the no:"))
count=0
i=1
while n>=i:
    if n%i==0:
        count+=1
    i=i+1
print("factor=",count)

"""


#question=6                find sum through factor
"""                

n=int(input("enter the factor:"))
sum=0
for i in range(1,n+1):
    if n%i==0:
        sum=sum+i
print("sum is",sum)


"""
"""
n=int(input("enter the no"))
sum=0
i=1
while n>=i:
    if n%i==0:
        sum=sum+i
    i=i+1
print("sum",sum)
"""

#question==7            power of a number    doubt

"""
n=int(input("enter the no"))
p=int(input("enter the no"))
for i in range(1,p+1):
    if i==p:
        print(n**i)
"""





#question==8            count multiples of 5 between two no
"""
n1=int(input("enter the first no:"))
n2=int(input("enter the second no:"))
count=0
for i in range(n1,n2+1):
    if i%5==0:
        count+=1
print("no multiply by 5 is:",count)

"""
#question==9           neon number LED game
"""


n=int(input("enter the no:"))
p=int(input("enter the power:"))
sum=0
square=n**p
while square>0:
    rem=square%10
    sum=sum+rem
    square=square//10
if sum==n:
    print("glowing success ! you found the neon no")
else:
    print("try again")

"""

#questopn ==10              student id validity checker count odd digit
"""
n=int(input("enter the no:"))
count=0
while n>0:
    rem=n%10
    if rem%2==1:
        count+=1
    n=n//10
print("odd digit count:",count)


"""





    