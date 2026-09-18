#question==1
"""
1.
Student Registration System – Longest Name

A school is organizing an inter-school cultural event. During the registration process, the coordinator notices that some students have very long names, which may not fit properly on the printed ID cards.

As a software developer, your task is to write a Python program that identifies the student with the longest name from the list of registered students using the reduce() function along with a lambda expression.

Input
students = ["Riya", "Christopher", "Aman", "Neha", "Siddharth"]
Expected Output
Student with the longest name: Christopher
"""
"""
from functools import reduce
stu=list(map(str,input("enter studebt name").split()))
r=reduce(lambda x,y:x if len(x)>len(y) else y ,stu)
print(r)
"""
#qyestion==2
"""
2.
Hospital Management System – Oldest Patient

A hospital wants to give priority to the oldest patient during a free health check-up camp. The patient details are stored as tuples containing the patient's name and age.

As a Python developer, write a program to identify the oldest patient using the reduce() function with a lambda expression.

Input
patients = [
    ("Rahul", 45),
    ("Sneha", 62),
    ("Amit", 38),
    ("Kiran", 71),
    ("Pooja", 55)
]
Expected Output
Oldest Patient: Kiran
"""
"""
from functools import reduce
n=int(input("enter no of patient: "))
p=[]
for i in range(n):
    n=input("enter patient name: ")
    id=int(input("enter id: "))
    p.append((n,id))

r=reduce(lambda x,y:x if x[1]>y[1] else y ,p)
for i in r:
    print("oldest patient",i)
    break

#print(r[0])
"""
#question==3
"""
3.
Cricket Tournament – Highest Run Scorer

A cricket academy wants to reward the player who scored the highest number of runs in a tournament.

Write a Python program to identify the highest run scorer using reduce() and a lambda expression.

Input
players = [
    ("Virat", 78),
    ("Rohit", 102),
    ("Gill", 89),
    ("KL Rahul", 65),
    ("Iyer", 91)
]
Expected Output
Highest Run Scorer: Rohit
"""
"""
from functools import reduce
n=int(input("enter no of patient: "))
p=[]
for i in range(n):
    n=input("enter patient name: ")
    run=int(input("enter id: "))
    p.append((n,run))
r=reduce(lambda x,y:x if x[1]>y[1] else y ,p)
print("highest run",r[0],"runs",r[1])
"""
#question==4
"""
4.
Assignment 10: Cyber Security (Strong Password Check)

A cybersecurity company considers a numeric password to be "strong" if every digit is even.

Task

Write a recursive function to check whether all digits of the given number are even.

Input 1
Enter Password:
248620
Output 1
Strong Password
Input 2
Enter Password:
248621
Output 2
Weak Password
"""