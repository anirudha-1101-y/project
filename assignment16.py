#quesion==5
"""
num = int(input("Input =  "))

n = 0
while num > 0:
    last = num % 10
    n = n * 10 + last
    num = num // 10

i = 1
total = 0  

while n > 0:
    last = n % 10

    if i % 2 != 0:  
        total += last
    else:            
        total -= last

    i += 1
    n = n // 10

print(f"Result = {total}")

if total > 0:
    print("Positive Pattern")
else:
    print("Negative Pattern"
"""
#question==4
"""
num = int(input("Input = "))
n=0
while num>0:
    last = num%10
    n = n*10 + last
    num = num//10


first = n%10
lastSec = n//10
second = lastSec%10

gap =  abs(second - first)

while n>9:
    fir = n%10
    lastSec = n//10
    sec = lastSec%10 
    digitGap = abs(fir-sec)
    if digitGap == gap:
        n = n//10
    else:
        print(f"Initial Gap = {gap}")
        print("Pattern Break Detected")
        break

else:
    print(f"Initial Gap = {gap}")
    print("Consistent Pattern"

"""
#question==3
"""
n = int(input("Input = "))
i = 0

while n>0:
    last = n%10
    if last != 0:
        i = i+1
        print(last)
        n = n//10
    else:
        print(f"Count = {i}")
        print("Zero Found - Process Stopped")
        break

else:
    print(f"Count = {i}")
    print("No Zero Found ")
"""
#question==2
"""
num = int(input("Input = "))
i = 1
n = 0

while num>0:
    last = num%10
    n = n*10 + last
    num = num//10



while n >10:
    last = n%10
    temp = n//10
    lastSec = temp%10
    if lastSec > last:
        i+=1
        n = n//10

    else:
        print(f"Break at position = {i}")
        print("Not increasing Number")
        break

else:
    print("Strictly Increasing Number")

"""
#question==1
"""
n=int(input("enter the no"))
l=len(str(n))
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
nn=rev
s=99
sum=0
print("products")
while nn>10:
    rem1=nn%10
    nn=nn//10
    rem2=nn%10
    
    p=rem1*rem2
    if p<s:
        s=p
    print(p)
    sum=sum+p
print(sum,"sum")
print("smallest number:",s)
if sum%l==0:
    print("stable no")
else:
    print("not stable no")
"""
#question==2
"""
n=int(input("enter the no"))
l=len(str(n))
flag=True
i=l
for i in range(1,l+1):
    d=n%10
    n=n//10
    d2=n%10
    if d2<d:
        flag=True
    else:
        flag=False
        break
if flag:
    print("increasing number")
else:
    print("not increasingno")
    print("break at position",l-i)
   """ 

































