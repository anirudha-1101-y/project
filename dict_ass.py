"""
1.

=========================================
ONLINE SHOPPING CART
====================

A shopping website stores purchased products in a dictionary where:
Key = Product Name
Value = Quantity Purchased

Write a program to:

* Accept a dictionary from the user.
* Calculate and display the total quantity of products purchased.

Sample Input:
{"Laptop":2,"Mouse":3,"Keyboard":1}

Sample Output:
Total Quantity = 6
"""

"""
n=int(input("enter no product: "))
d={}
for i in range(n):
    key=input("enter product name: ")
    value=int(input("enter quantity: "))
    d[key]=value
print(d)
print("total quantity",sum(d.values()))
"""
"""
2.

=========================================
EMPLOYEE DEPARTMENT COUNT
=========================

A company stores employee department names in a list.

employees = ["HR","IT","HR","Sales","IT","IT","Finance"]

Write a program to:

* Count how many employees belong to each department.
* Store the result in a dictionary.

Sample Output:
{'HR': 2, 'IT': 3, 'Sales': 1, 'Finance': 1
"""
"""
employees = ["HR","IT","HR","Sales","IT","IT","Finance"]

d={}
for i in employees:
    d[i]=d.get(i,0)+1

print(d)
"""
"""
3.

=========================================
WEBSITE PAGE VISIT TRACKER
==========================

A website records page visits.

pages = ["Home","About","Home","Contact","Home","About"]

Write a program to:

* Count visits of each page using a dictionary.
* Display page name and visit count.

Sample Output:
Home visited 3 times
About visited 2 times
Contact visited 1 time

---
"""
"""
pages = ["Home","About","Home","Contact","Home","About"]
d={}
for i in pages:
    d[i]=d.get(i,0)+1
print(d)
for k,v in d.items():
    print(k,"visited",v,"times")
"""
#taking list also from input
"""
n=int(input("enter no element in list"))
pages=[]
for i in range(n):
    x=input("enter element: ")
    pages.append(x)
print(pages)
d={}
for i in pages:
    d[i]=d.get(i,0)+1

for k,v in d.items():
    print(k,"visited",v,"times")
    """
"""
4.

=========================================
STUDENT GRADE ANALYSIS
======================

Store student marks in a dictionary.

students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65
"""
"""
students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}
l=list(students.values())
print(l)
max=l[0]
for i in l:
    if i>max:
        max=i
min=l[0]
for i in l:
    if i<min:
        min=i
for k,v in students.items():
    if v==max:
        print("Highest Marks:",k ,v)
    if v==min:
        print("lowest marks:",k,v)
"""

"""

5.

=========================================
WORD LENGTH GROUPING
====================

A content management system stores article tags.

tags = ["python","java","api","react","html","css"]

Write a program to:

* Group words according to their length.
* Store result in dictionary.

Sample Output:
{
3:['api','css'],
4:['java','html'],
5:['react'],
6:['python']
}
"""
"""
tags = ["python","java","api","react","html","css"]
d={}
for i in tags:
    if i not in d:
        l=len(i)
        if l not in d:
            d[l]=[]
        d[l].append(i)
print(d)

print(dict(sorted(d.items())))
"""

"""

6.

=========================================
MOBILE APP DOWNLOAD COUNTER
===========================

Downloads received from different cities:

cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]

Write a program to:

* Count downloads city-wise.
* Display city with maximum downloads.

Sample Output:
{'Indore':3,'Bhopal':1,'Pune':2,'Delhi':1}
Most Downloads : Indore
"""
"""
cities = ["Indore","Bhopal","Indore","Pune","Delhi","Pune","Indore"]
d={}
for i in cities:
    d[i]=d.get(i,0)+1
print(d)
l=list(d.values())
max=l[0]
for i in l:
    if i>max:
        max=i
for k,v in d.items():
    if v==max:
        print("most downloaded:",k)
        """
"""
7.

=========================================
ONLINE EXAM RESULT SYSTEM
=========================

Store student marks in a dictionary.

results = {
"Ajay":88,
"Ravi":45,
"Neha":76,
"Aman":39
}

Write a program to:

* Display names of students who passed.
  (Passing Marks = 50)

Sample Output:
Ajay
Neha
Rav
"""
"""
n=int(input("enter how many stu: "))
d={}
for i in range(n):
    key=input("enter your name: ")
    value=int(input("enter your marks: "))
    d[key]=value
print(d)
for k,v in d.items():
    if v>=50:
        print("pass student",k)
        """
"""
8.

=========================================
LIBRARY BOOK ISSUE TRACKER
==========================

A library records issued books.

books = [
"Python",
"Java",
"Python",
"C++",
"Java",
"Python"
]

Write a program to:

* Count how many times each book was issued.

Sample Output:
{
'Python':3,
'Java':2,
'C++':1
}

"""
books = [
"Python",
"Java",
"Python",
"C++",
"Java",
"Python"
]
"""
d={}
for i in books:
    c=0
    for j in books:
        if i==j:
            c=c+1
    d[i]=c
print(d)
"""
#orrrrrrrrrrrrrrrrrorrrrrrrrrrrr
"""
d={}
for i in books:
    d[i]=d.get(i,0)+1
print(d)
"""
"""

9.

=========================================
INVENTORY MANAGEMENT SYSTEM
===========================

Store product stock in a dictionary.

stock = {
"Pen":50,
"Pencil":100,
"Eraser":25,
"Marker":10
}

Write a program to:

* Display products having stock less than 30.

Sample Output:
Eraser
Marker
"""
"""
stock = {
"Pen":50,
"Pencil":100,
"Eraser":25,
"Marker":10
}
print(stock)
for k,v in stock.items():
    if v<=30:
        print(k)
        """
"""
10.

=========================================
EMAIL DOMAIN COUNTER
====================

emails = [
"[ajay@gmail.com](mailto:ajay@gmail.com)",
"[ravi@yahoo.com](mailto:ravi@yahoo.com)",
"[neha@gmail.com](mailto:neha@gmail.com)",
"[aman@outlook.com](mailto:aman@outlook.com)",
"[abc@gmail.com](mailto:abc@gmail.com)"
]

Write a program to:

* Count users belonging to each email domain.

Sample Output:
{
'gmail.com':3,
'yahoo.com':1,
'outlook.com':1
}

"""
"""
11.

=========================================
PRODUCT SALES ANALYSIS
======================

sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]

Write a program to:

* Count sales of each product.
* Display products in sorted order.

Sample Output:
Laptop : 2
Mobile : 3
Tablet : 1
"""
"""
sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]

d={}
for i in sales:
    c=0
    for j in sales:
        if i==j:
            c=c+1
    d[i]=c
print(d)
for k,v in d.items():
    print(k,":",v)
    """
#orrrrrrrr
"""
sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]
d={}
for i in sales:
    d[i]=d.get(i,0)+1
print(d)
for k,v in d.items():
    print(k,":",v)
    """
"""
12.

=========================================
ONLINE FOOD DELIVERY ANALYSIS
=============================

orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

Write a program to:

* Count orders of each food item.
* Find the most ordered item.

Sample Output:
Pizza : 3
Burger : 2
Pasta : 2

Most Ordered : Pizza
"""
"""
orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

d={}

for i in orders:
    c=0
    for j in orders:
        if i==j:
            c=c+1
    d[i]=c
l=list(d.values())
max=l[0]
for i in l:
    if max<i:
        max=i
for k,v in d.items():
    print(k,":",v)
for k,v in d.items():
    if v==max:
        print("most ordered: ",k)


"""
"""
for i in orders:
    d[i]=d.get(i,0)+1
l=list(d.values())
max=l[0]
for i in l:
    if max<i:
        max=i
for k,v in d.items():
    print(k,":",v)
for k,v in d.items():
    if v==max:
        print("most ordered: ",k)
    """