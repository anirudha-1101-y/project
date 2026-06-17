"""
1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8
"""

"""
s=input("enter")
c=0
i=0
while i<len(s):
    ch=s[i]
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        c=c+1
    else:
        pass
    i=i+1
print("vowel count",c)
"""


"""
2.
Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5

"""
"""
s=input("enter chat message : ")
c=0
i=0
while i<len(s):
    ch=s[i]
    if ch==" ":
        c=c+1
    else:
        pass
    i=i+1
print("total space=",c)
"""

#question==3
"""

3.
Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o

Output: Character 'o' occurs: 4 times
"""
"""
s=input("enter product review : ")
w=input("character : ")
c=0
i=0
while i<len(s):
    ch=s[i]
    if ch==w:
        c=c+1
    else:
        pass
    i=i+1
print("character",w,"occure",c)
"""
#question==4
"""
4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11

"""
"""
s=input("enter student name: ").lower()
c=0
i=0
while i<len(s):
    ch=s[i]
    if ch>="a" and ch<="z" and ch!="a" and ch!="e" and ch!="i" and ch!="o" and ch!="u":
        c=c+1
    i=i+1
print("total consonants:",c)

"""
""""""
#question==5
"""
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password

"""
"""
s=input("enter no   ")
u=False
lo=False
d=False
sp=False
spp=False
l=len(s)
i=0
if 8<=l<=15:
    i=0
    while i<l:
        ch=s[i]
        if ch>="A" and ch<="Z":
            u=True
        elif ch>="a" and ch<="z":
            lo=True
        elif ch>="0" and ch<="9":
            d=True
        elif ch==" ":
            spp=True
        else:
            sp=True
        i=i+1
    if u==True and lo==True and d==True and spp==False and sp==True:
        print("secure password")
    else:
        print("invalid password")
else:
    print("invalid password")

print("heyyy")

"""
"""

6.
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number
"""
"""
s=input("enter no : ")
l=len(s)
n=0

if l==12:
    i=0
    while i<l:
        l1=s[0]
        l2=s[1]
        l3=s[2]
        if l1=="P" and l2=="N" and l3=="R":
            pass
        else:
            print("invalid pnr")
            break
        if i>2:
            ch=s[i]
            if ch>="0" and ch<="9":
                pass
            else:
                print("invalid pnr")
                break
        i=i+1
    else:
        print("invalid PNR")
else:
    print("invalid pnr")
"""

           



