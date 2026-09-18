"""
l=[10,20,30,40]
l.append(60)
print(l)
"""
"""
l=[2]
print(l*2)
"""
"""
l=[10,20,30,40]
for  i in l:
    print(i,end=" ")
    """
"""
l=[10,20,30,40]
for i in range(len(l)):
    print("index",i,"value",l[i])
    """
"""
l=[1,2,3,4,5]
print(l[:3])
print(l[2:])
print(l[::-1])
"""
#insert method
"""
l=[10,20,30,40]
l.insert(len(l),99)
print(l)
"""
"""
l=[10,20,30,40]
l.insert(-10,999)
l.insert(10,777)
print(l)
"""
#extend methiod
"""
l=[10,20,30,40,50]
l.extend([40,50,60])
print(l)
"""
#updationg list element
"""
l=[10,20,30,40]
l[1]=100
print(l)
l[-1]=99
print(l)
"""
"""
l=[10,20,30,40,50,60]
l[1:3]=[200,300,500,526]
print(l)
"""
"""
l=[10,20,30,40]
for i in range(len(l)):
    print("index=",i,"value",l[i])
"""
"""
l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    i=i*2
    print(i,end=" ")
    """
"""
m=list(map(int,input("enter marks").split()))
print(m)
i=int(input("enter index"))
new=int(input("enter new value"))
m[i]=new
print(m)
"""
"""
stu=["deepika","rashmiks","katappa"]
marks=[10,20,30]
name=input("enter student name")
if name in stu:
    i=stu.index(name)
    new=input("enter new marks")
    marks[i]=new
    print(marks)
else:
    print("not found")
    """
"""
a=[10,20,60,520]
a.remove(20)
print(a)
"""
"""
a=[10,20,60,520]
a.pop(1)

print(a)
"""
"""
a=[10,20,60,520]
print(len(a))
a.clear()
print(len(a))
print(a)
"""
#del keyword
"""
a=[10,20,50,80]
del a[1]
print(a)
"""
#sort
"""
a=[2,25,2,58,65,85]
a.sort(reverse=True)
print(a)
"""
"""
a=["depikka,","ani","amyaank"]
a.sort(key=len)
print(a)
"""
#sorted
"""
a=[10,25,2,5,85,9]
b=sorted(a)
print(a)
print(b)
"""
"""
a=[10,25,85,95,56]
a.reverse()
print(a)
"""
"""
a=[10,25,85,95,56]
print(max(a))
print(min(a))
"""
#sum
"""
a=[10,25,85,95,56]
print(sum(a))
"""
"""
a=[10,25,85,95,56]
for i,v in enumerate(a):
    print("index",i,"value",v)
    """
#zip
"""
name=["ani","mayank","aaradhya","aayush","aman"]
m=[10,20,30,40]
for m,n in zip(name,m):
    print("name",m,"and marks",n)
    """
"""
n=int(input("enter total no element"))
m=[]
for i in range(n):
    x=int(input("enter ="))
    m.append(x)
print(m)
"""
#list compehension
"""
a=[1,2,3,4,5,6]
b=[i*2 for i in a]
print(b)
"""
"""
a=[1,2,3,4,5,6,7,8]
b=[i*2 if i%2!=0 else i for i in a]
print(b)
"""
"""
a=[10,20,30,40,50,60]
b=[i for i in a if i>20]
print(b)
"""
"""

a=['ani','mayank','anirudha']
b=[len(i) for i in a]
print(b)
"""
"""
a=['ani','mayank','anirudha']
b=[i for i in a if len(i)>5]
print(b)
"""
"""
a=['ani','mayank','anirudha']
b=[i.upper() for i in a]
print(b)
"""
#nested list
"""
a=[10,20,[30,40],50]
print(a[2][1])
print(a[2])
"""
#traversing in nested loop
a=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
"""
for i in a:
    print(i)
print()
"""
"""
for i in a:
    print()
    for j in i:
        print(j,end=" ")
        """
#using indx based loop
"""
a=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
for i in range(len(a)):
    print()
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
        """
"""
a=[
    [10,20],
    [40,50,60],
    [70],
    ["abc","xyz"]
]
print()
a[2]=[70,80,90]
print()
print(a)
"""
#addiingelement in nested list
"""
a=[
    [10,20,30],
    [40,50,60]
]
print(a)
a.append([70,80,90])
print(a)
"""
#remove element for nested list
"""
a=[
    [10,20,30],
    [40,50,60]
]
a[0].remove(20)
print(a)
"""
"""
a=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
print(a)
a.pop(0)
print(a)
"""
"""
#matrix form ==
a=[
    [10,20,30],
    [40,50,60]
]
for i in a:
     for j in i:
        print(j,end=" ")
     print()
     """
#user input matrix=============
"""
rows=int(input("enter no of rows"))
cols=int(input("enter no of column"))
mat=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        x=int(input("enter element"))
        row.append(x)
    mat.append(row)
print(mat)
for i in mat:
    for j in i:
        print(j, end=" ")
    print()
    """
"""
rows=int(input("enter no of rows"))
cols=int(input("enter no of column"))
mat=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        x=int(input("enter element"))
        row.append(x)
    mat.append(row)
print(mat)
sum=0
for i in mat:

    for j in i:
        sum=sum+j
print(sum)
"""
"""
rows=int(input("enter no of rows"))
cols=int(input("enter no of column"))
mat=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        x=int(input("enter element"))
        row.append(x)
    mat.append(row)
print(mat)
sum=0
i=0
while i<len(mat):
    j=0
    while j<len(mat[i]):
        sum=sum+mat[i][j]
        j=j+1
    i=i+1
print(sum)
"""
"""
rows=int(input("enter no of rows"))
cols=int(input("enter noof columns"))
mat=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        x=int(input("enter your element"))
        row.append(x)
    mat.append(row)
print(mat)
gt=0
max=0

for i in range(len(mat)):
    sum=0
    for j in range(len(mat[i])):
        e=mat[i][j]
        sum=sum+e
    print("row",i+1,"sum",sum)
    print("row",i+1,"avarage",sum/len(mat[i]))
    gt=gt+sum
    if max<sum:
        max=sum
        r=i+1
print("row",r)
print("greatest sum",gt)
    

"""






"""
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j],end=" ")
    print()
    """


# make two matrix
"""
rows=int(input("enter no of rows"))
cols=int(input("enter no of column"))
mat1=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        x=int(input("enter element"))
        row.append(x)
    mat1.append(row)
print(mat1)
print("matrix ==1")
for i in mat1:
    for j in i:
        print(j,end=" ")
    print()

mat2=[]

for i in range(rows):
    row=[]
    for j in range(cols):
        x=int(input("enter element"))
        row.append(x)
    mat2.append(row)
print(mat2)
print("matrix===2")
for i in range(len(mat2)):
    for j in range(len(mat2[i])):
        print(mat2[i][j],end=" ")
    print()
if mat1==mat2:
    print("same h laadle")
else:
    print("ni mila laadle")

"""
"""
rows=int(input("enter no of rows"))
cols=int(input("enter no of columns"))
print("matrix==1")
mat1=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        x=int(input("enter element"))
        row.append(x)
    mat1.append(row)
print(mat1)
for i in mat1:
    for j in i:
        print(j,end=" ")
    print()

mat2=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        x=int(input("enter element"))
        row.append(x)
    mat2.append(row)

print(mat2)
print("matrix==2")
for i in mat2:
    for j in i:
        print(j,end=" ")
    print()
print("matrix==3" "addition of matrix 1 and matrix 2")
mat3=[]
for i in range(rows):
    row=[]
    for i in range(cols):
        row.append(0)
    mat3.append(row)

for i in range(len(mat3)):
    for j in range(len(mat3[i])):
        mat3[i][j]=mat1[i][j]+mat2[i][j]

for i in mat3:
    for j in i:
        print(j,end=" ")
    print()
"""
"""
#multiplication of two matrix===
rows1=int(input("enter no of rows"))
cols1=int(input("enter no of cols"))
mat1=[]
for i in range(rows1):
    row=[]
    for j in range(cols1):
        x=int(input("enter element"))
        row.append(x)
    mat1.append(row)

rows2=int(input("enter no of rows"))
cols2=int(input("enter no of cols"))
mat2=[]
for i in range(rows2):
    row=[]
    for j in range(cols2):
        x=int(input("enter element"))
        row.append(x)
    mat2.append(row)

if cols1!=rows2:
    print("multiplication not possible")
else:
    print("resultant matrix ")
    res=[]
    for i in range(rows1):
        row=[]
        for j in range(cols2):
            row.append(0)
        res.append(row)
    
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                res[i][j]=res[i][j]+mat1[i][k]*mat2[k][j]
    print("matrix=1")
    for i in mat1:
        for j in i:
            print(j,end=" ")
        print()
    print("matrix=2")
    for i in mat2:
        for j in i:
            print(j,end=" ")
        print()
    print("resultant matrix==")
    for i in res:
        for j in i:
            print(j,end=" ")
        print()
            """

#named tuple
"""
from collections import namedtuple
student=namedtuple("stu",["name","rollno","city"])
s=student("ani",125,"mumbai")
print(s)
print(s.name)
print(s.rollno)
print(s.city)
"""
"""
from collections import namedtuple
account=namedtuple("Account",["accno","holdername","balance"])
a=int(input("enter account no"))
n=input("enter your name ")
b=float(input("enter your balance"))
acc=account(a,n,b)
print(acc)
print(acc.accno)
print(acc.holdername)
print(acc.balance)
"""
#practise question from daily task
"""

1. Find Leaders in a List
A leader is an element that is greater than all the elements to its right.
Input
Python
[16, 17, 4, 3, 5, 2]
Output
Python
[17, 5, 2]

"""
"""
e=list(map(int,input("enter your element").split()))
peak=[]
if len(e)>1:

    for i in range(len(e)):
        x=e[i]
        if i==0 and x>e[i+1]:
              peak.append(x)
        elif i!=0 and i!=len(e)-1:
             if x>e[i+1] :
                  peak.append(x)
        elif i==len(e)-1 :
             
                  peak.append(x)
else:
     peak.append(e)
print(peak)
 
"""
"""
2. Find the Longest Consecutive Sequence
Find the longest sequence of consecutive numbers in the list.
Input
Python
[100, 4, 200, 1, 3, 2]
Output
Python
[1, 2, 3, 4]

"""

"""
3. Move All Zeros to the End
Move all 0s to the end while maintaining the order of other elements.
Input
Python
[0, 1, 0, 3, 12, 0, 5]
Output
Python
[1, 3, 12, 5, 0, 0, 0
"""
"""
e=list(map(int,input("enter your element").split()))
z=[]
p=[]
for i in e:
    if i==0:
        z.append(i)
    else:
        p.append(i)
print(p+z)

"""
"""
4. Find All Unique Pairs with a Given Sum
Find all unique pairs whose sum is equal to a target value.
Input
Python
List = [2, 4, 3, 5, 7, 8, 9]
Target = 7
Output
Python
[(2, 5), (3, 4)]
"""
"""
e=list(map(int,input("enter your element").split()))
tar=int(input("enter target value: "))
m=[]
for i in range(len(e)):
    for j in range(i+1,len(e)):
        a=e[i]
        b=e[j]
        if a+b==tar:
            m.append((a,b))
print(m)


"""

"""

5. Find the Majority Element
A majority element appears more than n/2 times in the list. If none exists, print "No Majority Element".
Input 1
Python
[2, 2, 1, 2, 3, 2, 2]
Output 1
Python
2
Input 2
Python
[1, 2, 3, 4]
Output 2
Python
No Majority Elemen
"""
"""
e=list(map(int,input("enter your element").split()))
t=int(input("enter target: "))
c=0
for i in range(len(e)):
    if e[i]==t:
        c=c+1
else:
    if c>=len(e)/2:
        print("majority element")
    else:
        print("no majority element")
        """

#from daily task
"""
1. Second Largest Without sort() or max()

Write a program to find the second largest unique element in a list.

Input:

[12, 45, 67, 45, 89, 67]

Output:

67
"""
"""
l=list(map(int,input("enter your element: ").split()))
l1=sorted(l)
print(l1[-2])
"""
#doubt




"""
2. Frequency Without count()

Print the frequency of every element without using count().

Input:

[1, 2, 1, 3, 2, 1, 4]

Output:

1 -> 3
2 -> 2
3 -> 1
4 -> 1

"""
"""
l=list(map(int,input("enter your element: ").split()))
v=[]
for i in l:
    if i not in v:
        c=0
        for j in l:
            if i==j:
                c=c+1
        print(i,"-->",c)
        v.append(i)

"""
"""
3. Rotate List

Rotate the list to the right by k positions.

Input:

List: [1,2,3,4,5]
k = 2

Output:

[4,5,1,2,3]
"""
"""
4. Missing Number

A list contains numbers from 1 to n, but one number is missing.

Find the missing number.

Input:

[1,2,3,5,6,7]

Output:

4
"""
"""
l=list(map(int,input("enter your element: ").split()))
for i in range(1,len(l)):
    if i in l:
        pass
    else:
        print(i)
    
 """
"""
5. Longest Consecutive Sequence

Find the length of the longest consecutive sequence.

Input:

[100,4,200,1,3,2]

Output:

4

Explanation:

1,2,3,4
"""
"""
6. Remove Duplicates While Preserving Order

Do not use set().

Input:

[5,2,5,1,2,3,1]

Output:

[5,2,1,3]
    

"""
"""
l=list(map(int,input("enter your element: ").split()))
v=[]
for i in l:
    if i not in v:
        v.append(i)
print(v)
"""
"""
7. Leaders in a List

A leader is greater than all elements to its right.

Input:

[16,17,4,3,5,2]

Output:

17 5 2
"""
"""
v=[]
e=list(map(int,input("enter evalution").split()))


if len(e)>1:
    for i in range(len(e)):
        x=e[i]
        if i==0 and x>e[1]:
            v.append(x)
        elif i!=0 and i!=len(e)-1:
            if x>e[i-1] and x>e[i+1]:
                v.append(x)
        elif i==len(e)-1 and x>e[-2]:
            v.append(x)
        else:
            pass
print(v)
"""
"""
8. Find Pair With Given Sum

Print every unique pair whose sum equals the target.

Input:

List = [2,7,11,15,3,6,5]
Target = 9

Output:

(2,7)
(3,6)
"""
"""
l=list(map(int,input("enter your element: ").split()))
t=int(input("enter target"))
for i in range(len(l)):
    a=l[i]
    for j in range(i+1,len(l)):
        b=l[j]
        if a+b==t:
            print((a,b))
    
"""
"""
9. Matrix Row and Column Sum

Given a 2D list, print the sum of every row and every column.

Input:

[
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

Output:

Row Sum:
6
15
24

Column Sum:
12
15
18

"""
"""

r=int(input("enter no of rows"))
c=int(input("enter no of column"))
mat=[]
for i in range(r):
    row=[]
    for j in range(c):
        x=int(input("enter your element first: "))
        row.append(x)
    mat.append(row)
print(mat)


for i in range(r):
    sum=0
    for j in range(c):
        sum=sum+mat[i][j]
    print("row",i+1,sum)
    
print()
for i in range(r):
    sum=0
    for j in range(c):
        sum=sum+mat[j][i]
    print("colum",i+1,sum)
"""



"""
10. Maximum Difference

Find the maximum difference arr[j] - arr[i] where j > i.

Input:

[7,1,5,3,6,4]

Output:

5

Explanation:

6 - 1 = 5
"""
#solution
"""
l=list(map(int,input("enter your element: ").split()))
max=0
for i in range(len(l)):
    a=l[i]
    for j in range(i+1,len(l)):
        b=l[j]
        if b-a>max:
            max=b-a
print(max)
        
"""