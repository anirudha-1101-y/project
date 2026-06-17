"""
1.
=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================

A college has two clubs:
1. Coding Club
2. Robotics Club

Store student IDs of both clubs using sets.

Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit

Requirements:
- Use two sets.
- Apply intersection, difference, and union operations
"""
"""
coding=set()
robotic=set()


while True:
    print("1. Add Student to Coding Club")
    print("2. Add Student to Robotics Club")
    print("3. Display Students in Coding Club")
    print("4. Display Students in Robotics Club")
    print("5. Find Students in Both Clubs")
    print("6. Find Students Only in Coding Club")
    print("7. Find Students Only in Robotics Club")
    print("8. Display All Unique Club Members")
    print("9. Display Total Unique Club Members")
    print("10. Exit")
    ch=int(input("enter your choice: "))
    match ch:
        case 1:
            n=int(input("enter number : "))
            for i in range(n):
                x=int(input("enter id: "))
                coding.add(x)
           
        case 2:
            n=int(input("enter number : "))
            for i in range(n):
                x=int(input("enter id: "))
                robotic.add(x)
        case 3:
            print(coding)
        case 4:
            print(robotic)
        case 5:
            print(coding|robotic)
        case 6:
            print(coding-robotic)
        case 7:
            print(robotic-coding)
        case 8:
            print(coding^robotic)
        case 9:
            print(len(coding^robotic))
        case 10:
            print("exit")
            break


"""
"""
2.
=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================

An institute offers:
1. Python Course
2. Java Course

Store enrolled student email IDs using sets.

Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit

Requirements:
- Use two sets.
- Use membership operator (in).
- Use union, intersection and difference operations.
"""
"""
python=set()
java=set()
p=0

j=0
while True:
    print("1. Enroll Student in Python")
    print("2. Enroll Student in Java")
    print("3. Display Python Students")
    print("4. Display Java Students")
    print("5. Find Students Enrolled in Both Courses")
    print("6. Find Students Enrolled Only in Python")
    print("7. Find Students Enrolled Only in Java")
    print("8. Check Enrollment in Python Course")
    print("9. Display Total Unique Students")
    print("10. Exit")

    choice=int(input("enter your choice: "))
    match choice:
        case 1:
            python=set(input("enter email ").split())
            p=1
        case 2:
            java=set(input("enter email ").split())
            j=1
        case 3:
            if p==0:
                print("pls enter element in pyhone")
            else:
                print(python)
        case 4:
            if j==0:
                print("pls enter element in java")
            else:
                print(java)
        case 5:
            if j==0 and p==0:
                print("pls enter email first")
            else:
                print(python&java)
        case 6:
            if p==0:
                print("pls enroll first")
            else:
                print(python-java)
        case 7:
            if java==0:
                print("pls enroll first")
            else:
                print(java-python)
        case 8:
            if p==0:
                print("pls enter first")
            else:
                n=input("enter your name")
                if n in python:
                    print("student in python")
                else:
                    print("not found")
        case 9:
            print(python|java)
        case 10:
            print("exit")
            break
"""
"""
3.
=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================

A website stores unique visitor IDs.

3.
=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================

A website stores unique visitor IDs.

Menu:
1. Add Visitor
2. Remove Visitor
3. Check Visitor
4. Display All Visitors
5. Count Unique Visitors
6. Clear Visitor Data
7. Exit

Requirements:
- Use a set to store visitor IDs.
- Duplicate visitor IDs should not be stored.
- Use add(), remove(), and membership operations
Requirements:
- Use a set to store visitor IDs.
- Duplicate visitor IDs should not be stored.
- Use add(), remove(), and membership operations
"""
"""
n=int(input("enter no  of id's:"))
x=0
s=set()
while True:
    print("Menu:")
    print("1. Add Visitor")
    print("2. Remove Visitor")
    print("3. Check Visitor")
    print("4. Display All Visitors")
    print("5. Count Unique Visitors")
    print("6. Clear Visitor Data")
    print("7. Exit")


    ch=int(input("enter your choice: "))
    match ch:
        case 1:
            
            for i in range(n):
                x=int(input("enter element"))
                s.add(x)
        case 2:
            idd=int(input("enter item to remove"))
            if idd in s:
                s.remove(idd)
                print("visitor removed successfully")
            else:
                print("not found")
        case 3:
            id=int(input("enter your id"))
            if id in s:
                print("visitor exixts")
            else:
                print("not found")
        case 4:
            print("visitor :",s)
        case 5:
            print(len(s))
        case 6:
            s.clear()
            print(s)
        case 7:
            print("exist")
            break
        
"""
"""
4.
=========================================
FROZEN SET SUBJECT MANAGEMENT
=========================================

An institute offers fixed subjects:

Python
Java
MySQL
React
Spring Boot

These subjects cannot be modified after creation.

Menu:
1. Display Subjects
2. Search Subject
3. Count Subjects
4. Attempt to Add Subject
5. Exit

Requirements:
- Use Frozen Set.
- Show that modification is not allowed


"""
"""
s=frozenset(["Python","Java","MySQL","React","Spring Boot"])
while True:
    print("Menu:")
    print("1. Display Subjects")
    print("2. Search Subject")
    print("3. Count Subjects")
    print("4. Attempt to Add Subject")
    print("5. Exit")
    ch=int(input("enter your choice:"))
    match ch:
        case 1:
            for i in s:
                print( i,end= " , ")
        case 2:
            sr=input("enter your subject: ")
            if sr in s:
                print("suject exist ")
            else:
                print("subject not found")
        case 3:
            print("count=",len(s))
        case 4:
            print("cannot add subjevt because frozen set is immutable ")
        case 5:
            print("exit")
            break

"""
"""
5.
=========================================
LIBRARY ISBN MANAGER
=========================================

A library stores unique ISBN numbers of books.

Menu:
1. Add ISBN
2. Remove ISBN
3. Search ISBN
4. Display ISBN List
5. Count Books
6. Exit

Requirements:
- Use Set.
- Duplicate ISBNs are not allowed
    

"""
"""
lib=set()
print()
while True:
    print("Menu:")
    print("1. Add ISBN")
    print("2. Remove ISBN")
    print("3. Search ISBN")
    print("4. Display ISBN List")
    print("5. Count Books")
    print("6. Exit")

    ch=int(input("enter your choice "))
    match ch:
        case 1:
            n=int(input("enter no if book"))
            for i in range(n):
                x=int(input("enter book ISBN="))
                lib.add(x)

        case 2:
            i=int(input("enter remove ISBN:"))
            if i in lib:
                lib.remove(i)
            else:
                print("not found")
        case 3:
            s=int(input("enter searching ISBN:"))
            if s in lib:
                print("ISBN found")

            else:
                print("NOT FOUND")
        case 4:
            for i in lib:
                print(i,end="  ")
            print()
        case 5:
            print("count=",len(lib))
        case 6:
            print("exit")
            break

"""
"""
6.

=========================================
COMMON CHARACTER FINDER
=========================================

Enter two strings and find common characters.

Menu:
1. Enter First String
2. Enter Second String
3. Display Common Characters
4. Count Common Characters
5. Exit

Example:
String1: python
String2: typhoon

Output:
{p, t, h, o, n}
"""
"""

while True:
    print("Menu:")
    print("1. Enter First String")
    print("2. Enter Second String")
    print("3. Display Common Characters")
    print("4. Count Common Characters")
    print("5. Exit")

    ch=int(input("enter your choice: "))
    match ch:
        case 1:
            n1=input("enter firdt string")
            s=set(n1)
        case 2:
            n2=input("enter seconf string")
            s1=set(n2)

        case 3:
            print("common character",s.intersection(s1))
        case 4:
            print("common character count",len(s&s1))
        case 5:
            print("exit")
            break
"""
"""
7.
=========================================
MISSING ALPHABET FINDER
=========================================

Enter a sentence and find which
alphabets are missing.

Menu:
1. Enter Sentence
2. Display Missing Alphabets
3. Count Missing Alphabets
4. Exit

Requirements:
- Use Set containing a-z

"""
"""
alpha=set("abcdefghijklmnopqrstuvwxyz")
sen=set()
while True:
    print("Menu:")
    print("1. Enter Sentence")
    print("2. Display Missing Alphabets")
    print("3. Count Missing Alphabets")
    print("4. common in both")
    print("exit")
    
    ch=int(input("enter your choice: "))
    match ch:
        case 1:
            s=input("enter your sentence")
            sen=set(s)
        case 2:
            a=alpha-sen
            print("missing alphabet",a)
        case 3:
            print(len(a))
        case 4:
            print("common in both",alpha&sen)
        case 5:
            print(exit)
            break
"""
"""
8.
=========================================
ALLOWED CHARACTER VALIDATOR
=========================================

Allowed characters are:
A-Z, a-z, 0-9

Store allowed characters in a Frozen Set.

Menu:
1. Enter Username
2. Validate Username
3. Display Allowed Characters
4. Exit

Requirements:
- Use Frozen Set.
- Username should contain only allowed characters

"""
"""
allowed = frozenset(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
)

username = ""

while True:
    print("\nMenu:")
    print("1. Enter Username")
    print("2. Validate Username")
    print("3. Display Allowed Characters")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    match ch:
        case 1:
            username = input("Enter Username: ")

        case 2:
            if set(username).issubset(allowed):
                print("Valid Username")
            else:
                print("Invalid Username")

        case 3:
            print("Allowed Characters:")
            for i in allowed:
                print(i, end=" ")
            print()

        case 4:
            print("Exit")
            break

        case _:
            print("Invalid Choice")


"""