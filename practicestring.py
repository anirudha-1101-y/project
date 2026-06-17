"""
s="DEepika132"
s1=s.isdigit()
print(s1)
s2=s.lower()
print(s2)
s3=s.upper()
print(s3)
s4=s.isspace()
print(s4)
print(" ".isspace())

a= "my name is anirudha"
a1=a.istitle()
print(a1)
a1=a.title()
print(a1)
print(a.replace("anirudha","ani"))
a2=a.split()
print(a2)
print(" ".join(a2))

"""
#convert first ch  of every word in upper case
"""
s=input("enter string")
s1=""
s2=""
result=""
for i in s:
    if i.isalpha():
        s1=s1+i
    else:
        s2=s2+i

for i in sorted(s1):
    result=result+i
for i in sorted(s2):
    result=result+i
print(result)
"""
"""
s=input("enter string")
result=""
for x in s:
    if x.isalpha():
        result=result+x
        pre=x
    else:
        result=result+pre*(int(x)-1)
print(result)
"""
"""
s=input("enter string")
result=""
for x in s:
    if x.isalpha():
        result=result+x
        p=x
    else:
        new=chr(ord(p)+(int(x)))
        result=result+new
print(result)
"""
"""
s=input("enter string")
rev=""
i=len(s)-1
while i>=0:
    rev=rev+s[i]
    i=i-1
print(rev)
"""
"""
s=input("enter string")
l=s.split()
rev=""
for i in range (len(l)-1,-1,-1):
    rev=rev+l[i]
print(rev)

"""
"""
s=input("enter string")
l=s.split()
print("".join(l[::-1]))
"""