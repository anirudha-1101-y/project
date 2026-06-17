"""
1.  Bank Customer Account Privacy System

A national bank is developing a secure customer portal where account
numbers should not be displayed completely on the screen. For security
reasons, the system should hide all digits except the last four digits
before showing them to users.

Conditions: - Display only the last 4 digits - Replace all previous
characters with *

Input: Enter account number: 123456789012

Output: Masked Account: ****9012
"""
"""
s=input("enter str : ")
i=0
l=len(s)
while i<l:
    if i<l-4:
        print("*",end="")
    else:
        print(s[i],end="")
    i=i+1
    """

"""
2.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST
"""
"""
s=input("enter str : ")
i=0
r=""
while i<len(s):
    ch=s[i]
    if i==0 or s[i-1]==" ":
       upp=s[i].upper()
       r=r+upp
    i=i+1
print(r)
"""
"""
3.  Smart Chat Message Cleaner

A social media company noticed that users often enter messages with
unnecessary spaces. To improve readability and storage efficiency, the
system should remove extra spaces and keep only a single space between
words.

Input: Enter message: Java is easy

Output: Cleaned Message: Java is easy
"""
"""
s=input("enter str : ")
s1=s.split()
print(s1)
print(" ".join(s1))
"""
"""
4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop
"""
"""
s=input("enter str : ")
s1=s.split()
l=len(s1)
j=""
for i in s1:
     j=j+i[::-1]+" "
print(j)
"""
"""
5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website

"""
"""
s=input("enter str : ")
l=len(s)
i=0
while i<l:
    l1=s[0]
    l2=s[1]
    l3=s[2]
    ch=s[i]
    if l1=="W" and l2=="W" and l3=="W":
        pass
    elif ch>="a" and ch<="z":
        pass
    else:
        if s[l-4]==".":
            pass
        elif s[l-3]=="c":
            pass
        elif s[l-2]=="o":
            pass
        elif s[l-1]=="m":
            pass
        print("valid")
    print("invlid")
    i=i+1

else:
    print("valid")

"""


