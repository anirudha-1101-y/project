"""
#question==1
1. Two Sum
Easy
Topics
premium lock icon
Companies
Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
"""
nums =list(map(int,input("enter element").split()))
target = int(input("enter target: "))

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
            break
"""
"""
#question==2
26. Remove Duplicates from Sorted Array
Easy
Topics
premium lock icon
Companies
Hint
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
"""
l=list(map(int,input("enter element").split()))


l1=[]
for i in l:
    if i in l1:
        pass
    else:
        l1.append(i)

print(len(l1))
print(l1)
"""
#question==3
"""
27. Remove Element
Easy
Topics
premium lock icon
Companies
Hint
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
"""
l=list(map(int,input("enter your element: ").split()))
v=int(input("enete value: "))
out=[]
l1=[]
c=0
for i in l:
    if i!=v:
        out.append(i)
        c=c+1
    else:
        l1.append("_")


print(c,"-",out+l1)
"""
#question==4
"""
35. Search Insert Position
Easy
Topics
premium lock icon
Companies
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""
"""
nums = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter target: "))

for i in range(len(nums)):
    if nums[i] >= target:
        print(i)
        break
else:
    print(len(nums))
"""
#question==5
"""
66. Plus One
Easy
Topics
premium lock icon
Companies
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0]
"""
"""
l=list(map(int,input("enter list").split()))
print(l)
l1=int("".join(map(str,l)))
l2=l1+1
print(list(map(int,str(l2))))
"""

    

#question==6
"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 """
"""
a=input("enter value 1")
b=input("enter value 2")
print(bin(int(a,2)+int(b,2))[2:])
"""
#question ==7
"""
Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1
"""
"""
l=list(map(int,input("enter your element").split()))

for i in l:
    c=0
    for j in l:
        if i==j:
            c=c+1
    else:
        if c==1:
            print(i,end=" ")
"""
#question==8
"""
Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation
"""
"""
l=list(map(int,input("enter your element: ").split()))
f=False
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            f=True
            break
   
print(f)

"""
"""
l=list(map(int,input("enter your element: ").split()))
s=set(l)
if len(s)==len(l):
    print("false")
else:
    print("true")
"""
"""
print("additon of two matrix ")
while True:
    print("1.sum of two matrix")
    print("2.multiplication of two matrix")
    print("exit")
    ch=int(input("enter your choice: "))
    match ch:
        case 1:
            rows=int(input("enter no of rows: "))
            cols=int(input("enter no of cols"))
            mat1=[]
            for i in range(rows):
                r=[]
                for j in range(cols):
                    x=int(input("enter element: "))
                    r.append(x)
                mat1.append(r)
            print("element =2")
            mat2=[]
            for i in range(rows):
                r=[]
                for j in range(cols):
                    x=int(input("enter element: "))
                    r.append(x)
                mat2.append(r)
            mat3=[]
            for i in range(rows):
                r=[]
                for j in range(cols):
                    r.append(0)
                mat3.append(r)
            print(" matrix==1")
            for i in mat1:
                for j in i:
                    print(j,end=" ")
                print()
            print("matrix ==2")
            for i in mat2:
                for j in i:
                    print(j,end=" ")
                print()
            for i in range(rows):
                for j in range(cols):
                    mat3[i][j]=mat1[i][j]+mat2[i][j]
            print("matrix==resultant")
            for i in mat3:
                for j in i:
                    print(j,end=" ")
                print()
        case 2:
            rows1=int(input("enter no of rows: "))
            cols1=int(input("enter no of cols"))

            mat1=[]
            
            for i in range(rows1):
                r=[]
                for j in range(cols1):
                    x=int(input("enter element: "))
                    r.append(x)
                mat1.append(r)
            
            rows2=int(input("enter no of rows: "))
            cols2=int(input("enter no of cols"))

            mat2=[]
            
            for i in range(rows2):
                r=[]
                for j in range(cols2):
                    x=int(input("enter element: "))
                    r.append(x)
                mat2.append(r)
            if cols1==rows2:
                mat3=[]
                for i in range(rows1):
                    r=[]
                    for j in range(cols2):
                        r.append(0)
                    mat3.append(r)
                for i in range(rows1):
                    for j in range(cols2):
                        for k in range(cols1):
                            mat3[i][j]=mat3[i][j]+mat1[i][k]+mat2[k][j]
                for i in mat3:
                    for j in i:
                        print(j,end=" ")
                    print()

"""
"""
2.

=========================================================
            MATRIX ANALYSIS SYSTEM
=========================================================


A research laboratory stores experimental data in matrix form.
Scientists want a program that can analyze the matrix and provide
different statistics through a menu-driven application.

The application should allow the user to:

1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

     """
"""
rows=int(input("enter no of rows: "))
cols=int(input("enter no of cols: "))
mat=[]
for i in range(rows):
    r=[]
    for j in range(cols):
        x=int(input("entre element: "))
        r.append(x) 
    mat.append(r)          
print(mat)            
while True:
    print("1. Count Prime Numbers Row-wise")
    print("2. Count Perfect Numbers Column-wise")
    print("3. Display Row-wise Sum")
    print("4. Exit")
    ch=int(input("enter your choice :"))

    match ch:
        case 1:
            for i in range(rows):
                c=0
                for j in range(cols):
                    s=mat[i][j]
                    if s>1:
                        for k in range(2,s//2+1):
                          if s%k==0:
                              break
                        else:
                           c=c+1
                print("row",i+1,"count is",c)
        case 2:
            for i in range(len(mat[0])):
                c=0

                for j in range(len(mat)):
                    a=mat[j][i]
                    sum=0
                    for k in range(1,a//2+1):
                        if a%k==0:
                            sum=sum+k
                    
                    if sum==a:
                            c=c+1
                print("column",i+1,"count",c)
        case 3:
            for i in range(len(mat)):
                sum=0
                for j in range(len(mat[i])):
                    s=mat[i][j]
                    sum=sum+s
                print("row",i+1,"sum",sum)
        case 4:
            print("exit ")
            break

"""

