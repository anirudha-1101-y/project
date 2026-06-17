#question==1
#*****
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=n:
        if i==1:
            print("*",end="")
        j=j+1
    i=i+1

 """
#question==2
"""
*
*
*
*
*
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if j==1:
            print("*",end="")
        j=j+1
    i=i+1
"""
#question==3
"""
*
 *
  *
   *
    *
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if i==j:
            print("*",end="")
        else:
            print(" ",end="")
        j=j+1
    i=i+1

"""
#question==4
"""
*****
*****
*****
*****
*****
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=n:
        print("*",end="")
        j=j+1
    i=i+1
"""
#question==5
"""
12345
12345
12345
12345
12345
"""
"""

n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=n:
        print(j,end="")
        j=j+1
    i=i+1
    
"""
#question==6
"""
11111
22222
33333
44444
55555
"""
"""
n=int(input("enter no"))
i=1
while i<=n:
    print()
    j=1
    while j<=n:
        print(i,end="")
        j=j+1
    i=i+1
"""






#question==7
"""
1
00
111
0000
11111
"""
"""
n=int(input("enter no :"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if i%2==0:
            print("0",end="")
        else:
            print("1",end="")
        j=j+1
    i=i+1
"""







#question==8
"""
*
**
***
****
*****
"""
"""
n=int(input("enter no:"))
for i in range(1,n+1):
    print()
    j=1
    for j in range(1,i+1):
        print("*",end="")
"""
#question==9
"""
1
12
123
1234
12345
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    i=i+1

"""
#question==10
"""
1
22
333
4444
55555
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        print(i,end="")
        j=j+1
    i=i+1

"""
#question==11
"""
A
AB
ABC
ABCD
ABCDE
"""
"""
n=int(input("enter no:"))
i=1

while i<=n:
    print()
    j=1
    k=65
    while j<=i:
        print(chr(k),end="")
        k=k+1
        j=j+1
    i=i+1
    
"""
#question==12
"""
a
ab
abc
abcd
abcde
"""
"""
n=int(input("enter no:"))
i=1

while i<=n:
    print()
    j=1
    k=97
    while j<=i:
        print(chr(k),end="")
        k=k+1
        j=j+1
    i=i+1

"""
#question==13
"""
1
01
101
0101
10101
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        
        if (i+j)%2==0:
            print("1",end="")
        else:
            print("0",end="")
        j=j+1
    i=i+1
"""
#question==14
"""
1
23
456
78910
"""
 # jab hume line by line  no incerase karna ho to aap k ki value sabse pehele hi d dnge
"""
n=int(input("enter no "))
i=1
k=1
while i<=n:
    print()
    j=1
    while j<=i:
        print(k,end="")
        k=k+1
        j=j+1
    i=i+1
"""










#question==15
"""
A
BB
CCC
DDDD
EEEEE
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    k=65+i-1
    while j<=i:
        print(chr(k),end="")
        j=j+1
    i=i+1
"""
#question==16
"""

a
bc
def
ghij
klmno
"""
"""
n=int(input("enter no: "))
i=1
k=97+i-1
while i<=n:
    print()
    j=1
    
    while j<=i:
        print(chr(k),end="")
        j=j+1
        k=k+1
    i=i+1
"""


#question==17
"""
*
##
***
####
*****
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if i%2==0:
            print("#",end="")
        else:
            print("*",end="")
        j=j+1
    i=i+1

"""
#question==18
"""
1
10
101
1010
10101
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if j%2==0:
            print("0",end="")
        else:
            print("1",end="")
        j=j+1
    i=i+1
"""
#question==19
"""
*
* *
*  *
*   *
* * * * *
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if i==j or i==n or j==1:
            print("*",end="")
        
        else:
            print(" ",end="")

        j=j+1
    i=i+1
"""
#question==20
"""
1
12
1 3
1  4
12345
"""
"""
n=int(input("entre no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if j==1 :
            print("1",end="")
        elif i==j:
            print(i,end="")
        elif i==n:
            print(j,end="")
        else:
            print(" ",end="")
        j=j+1
    i=i+1

 """
#question==21
"""
1
22
3 3
4  4
55555
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if i==j or i==n or j==1:
            print(i,end="")
        else:
            print(" ",end="")
 
        j=j+1
    i=i+1
"""
#question==22
"""
A
AB
A C
A  D
ABCDE
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    k=65
    while j<=i:
        if j==i or j==1 or i==n:
            print(chr(k),end="")
        else:
            print(" ",end="")
        k=k+1
        j=j+1
    i=i+1
    
"""
#question==23
"""
a
bc
d f
g  j
klmno
"""
"""
n=int(input("enter no:"))
i=1
k=97+i-1
while i<=n:
    print()
    j=1
    while j<=i:
        if j==1 or i==n or j==i:
            print(chr(k),end="")
        else:
            print(" ",end="")
        j=j+1
        k=k+1
    i=i+1
    
"""



#question==14
"""
*
**
*@*
*@@*
* * * * *
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if j==1 or i==j or i==n:
            print("*",end="")
        else:
            print("#",end="")
        j=j+1
    i=i+1
  """
#question==25
"""
5
54
543
5432
54321
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=5
    while j>=6-i:
        print(j,end="")
        j=j-1
    i=i+1
"""
#question==26
""" 
*
*#
*#*
*#*#
*#*#*
"""
"""
n=int(input("enter no :"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if j%2==0:
            print("#",end="")
        else:
            print("*",end="")
        j=j+1
    i=i+1
"""
#question==27
"""
1
10
1 1
1  0
10101

"""
"""
n=int(input("enetr no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if i==j or i==n:
            if j%2==0:
                print("0",end="")
            else:
                print("1",end="")
        elif j==1 :
            print("1",end="")
        else:
            print(" ",end="")
        j=j+1
    i=i+1
"""
#questin==28
"""
1
123
12345
1234567
123456789
"""
"""
n=int(input("enter no:"))
i=0
while i<=n:
    print()
    j=1
    while j<=(i*2)-1:
        print(j,end="")
        j=j+1
    i=i+1
"""
#question==29
"""
1
222
33333
4444444
555555555
"""
"""
n=int(input("enter no:"))
i=0
while i<=n:
    print()
    j=1
    while j<=(i*2)-1:
        print(i,end="")
        j=j+1
    i=i+1
"""
#question==30
"""
***** 
**** 
***
**
* 

"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    i=i-1
"""
#question==31
"""
12345
1234
123
12
1
"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    i=i-1
"""
#question==32
"""
55555
4444
333
22
1
"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    j=1
    while j<=i:
        print(i,end="")
        j=j+1
    i=i-1
"""
#question==33
"""
ABCDE
ABCD
ABC
AB
A
"""
"""
n=int(input("enter no"))
i=n
while i>=1:
    print()
    j=1
    k=65
    while j<=i:
        print(chr(k),end="")
        j=j+1
        k=k+1
    i=i-1
"""



#question==34
"""
EEEEE
DDDD
CCC
BB
A
"""










"""
n=int(input("enter no:"))
i=n
k=69
while i>=1:
    print()
    j=1
    
    while j<=i:
        print(chr(k),end="")
        
        j=j+1
    k=k-1  
    i-=1

"""
#question==35
"""
*****
*  *
* *
**
*
"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    j=1
    while j<=i:
        if i==j or j==1 or i==n:
            print("*",end="")
        else:
            print(" ",end="")
        j=j+1
    i=i-1
"""
#question==36
"""
ABCDE
A  D
A C
AB
A
"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    j=1
    k=65
    while j<=i:
        if i==j or i==n or j==1:
            print(chr(k),end="")
        else:
            print(" ",end="")
        j=j+1
        k=k+1
    i=i-1

"""
#question==37
"""
*****
####
***
##
*
"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    j=1
    while j<=i:
        if i%2==0:
            print("#",end="")
        else:
            print("*",end="")
        j=j+1
    i=i-1
"""
#question==38
"""
55555
4  4
3 3
22
1
"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    j=i
    while j>=1:
        if i==n or i==j or j==1:
            print(j,end="")
        else:
            print(" ",end="")
        j=j-1
    i=i-1

 """
#question==39
"""
123456
54321
1234
321
12
1
"""
"""
n=int(input("enter no"))
i=n
while i>=1:
        print()
    
        if i%2==0:
            j=1
            while j<=i:
                print(j,end="")
                j=j+1
        else:
            j=i
            while j>=1:
                print(j,end="")
                j=j-1
            
        i=i-1
"""
            


#question==40
"""
*
**                           #doubt
****
*******
***********
"""








#question==41
"""
A
BCD
EFGHI
JKLMNOP
"""
"""
n=int(input("enter no:"))
i=1
k=65
while i<=n:
    print()
    j=0
    while j<(i*2)-1:
        print(chr(k),end="")
        j=j+1
        k=k+1
    i=i+1
"""
#question==42
"""
54321
5432
543
54
5
"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    j=n
    while j>=n-i+1:
        print(j,end="")
        j=j-1
    i=i-1
"""
#question==43
"""
    1
   12
  123
 1234
12345

"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=n-i:
        print(" ",end="")
        j=j+1
    k=1
    while k<=i:
        print(k,end="")
        k=k+1
    i=i+1


"""
#question==44
"""
    1
   22
  333
 4444
55555
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1                    #space
    while j<=n-i:
        print(" ",end="")
        j=j+1
    k=1
    while k<=i:
        print(i,end="")
        k=k+1
    i=i+1
"""
#question==45
"""
    5
   44
  333
 2222
11111
"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    j=1                    #space
    while j<=i-1:
        print(" ",end="")
        j=j+1
    k=n
    while  k>=i:
         print(i,end="")
         k=k-1
    i=i-1
"""

#question==46
"""
    A
   AB
  abc
 ABCD
ABCDE
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    k=65
    j=1
    while j<=i:
        print(chr(k),end="")
        k=k+1
        j=j+1
    i=i+1
"""



#question==47
"""
    1
   11
  1*1
 1**1
11111
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        if i==n or j==1 or j==i :

            print("1",end="")
        else:
            print("*",end="")

        j=j+1

    i=i+1


"""

#uestion==48
"""
    A
   AB
  A_C
 A__D
ABCDE
"""
"""

n=int(input("nter no:"))
i=1
while i<=n:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    k=65
    while j<=i:
        if  i==n or j==i or j==1 :
            print(chr(k),end="")
        else:
            print("-",end="")
        k=k+1
        j=j+1
    i=i+1
"""
#question==49
"""
    1
   10
  101
 1010
10101

"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1

    j=1
    while j<=i:
        if j%2!=0 or j==1:
            print("1",end="")
        else:
            print("0",end="")
        j=j+1
    i=i+1
  
"""
#question==50
"""
12345
 1234
  123
   12
    1
"""
"""
n=int(input("enter no"))
i=n
while i>=1:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    i=i-1

"""




#question==51
"""
55555
 4444
  333
   22
    1
"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print(i,end="")
        j=j+1
    i=i-1
"""
#question==52
"""
12345
 1__4
  1_3
   12
    1
"""
"""
n=int(input("enter no"))
i=n
while i>=1:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        if j==1 or j==i or i==n:
            print(j,end="")
        else:
            print("_",end="")
        j=j+1
    i=i-1
"""



#question==53
"""
55555
 4__4
  3_3
   22
    1
"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
            if j==1 or i==n or i==j:
                 print(i,end="")
       
            else:
                print("*",end="")
            j=j+1
    i=i-1

"""
#question==54
"""
ABCDE
 A__D
  A_C
   AB
    A
"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    k=65
    while j<=i:
        if i==n or i==j or j==n or j==1:
            print(chr(k),end="")
        else:
            print("-",end="")
        k=k+1
        j=j+1
    i=i-1

"""
#question==55
"""
ABCDE
 ABCD
  ABC
   AB
    A
"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    k=65
    while j<=i:
        print(chr(k),end="")
        k=k+1
        j=j+1
    i=i-1

"""
#question==56
"""
11111
 2222
  333
   44
    5
"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    k=n-i+1
    while j<=i:
        print(k,end="")
        j=j+1
    i=i-1
"""
#question==57
"""
        *
      * *
    * * *
  * * * *
* * * * *
"""
"""
n=int(input("enter no:"))

i=1
while i<=n:
    print()
    s=1
    while s<=n-i:
        print("  ",end="")
        s=s+1
    j=1
    while j<=i:
        print("* ",end="")
        j=j+1
    i=i+1

"""


#queestion===58
"""
*
* *
* * *
* * * *
* * * * *

"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        print("* ",end="")
        j=j+1
    i=i+1

"""
#question==58
"""
    1
   12
  123
 1234
12345


"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    i=i+1
"""
#question==59
"""
A
A B
A B C
A B C D
A B C D E  
"""
"""
n=int(input("enter no:"))
i=1

while i<=n:
    print()
    j=1
    k=65
    while j<=i:
        print(chr(k)+" ",end="")
        k=k+1
        j=j+1
    i=i+1
"""
"""
        A
      A B
    A B C
  A B C D
A B C D E  
"""
"""
n=int(input("enter no:"))
i=1

while i<=n:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    k=65
    while j<=i:
        print(chr(k)+" ",end="")
        k=k+1
        j=j+1
    i=i+1
"""
#question==60
"""
X 
X X 
X__X
X____X
X X X X X
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if j==1 or i==n or i==j:
            print("X",end="")
            
        else:
            print("_",end="")
       
        j=j+1
    i=i+1

"""


"""
    x
   X X 
  X__X
 X____X
X X X X X
"""
"""
n=int(input("enter no"))
i=1
while i<=n:
     print()
     s=1
     while s<=n-i:
        print(" ",end="")
        s=s+1
     j=1
     while j<=i:
        if j==1 or j==i or i==n:
            print("X ",end="")
        else:
            print("_ ",end="")
        j=j+1
     i=i+1

"""








#question==61
"""	
    *
   ***
  *****
 *******
*********
"""
"""
n=int(input("enter no"))
i=1
while i<=n:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i*2-1:
        print("*",end="")
        j=j+1
    i=i+1
"""


#question==62
"""
    1
   123
  12345
 1234567
123456789
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    
    k=1
    while k<=(i*2)-1:
        print(k,end="")
        k=k+1
 
        
    i=i+1
 
"""
#question==63
"""
    A
   ABC
  ABCDE
 ABCDEEF
ABCDEFGHI
"""

"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    k=65
    while j<=(i*2)-1:
        print(chr(k),end="")
        k=k+1
        j=j+1
    i=i+1
  """     
#question==64
"""
    *
   *_*
  *___* 
 *_____* 
*********
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<i*2:
        if j==1 or j==i*2-1:
            print("*",end="")
        elif i==n:
            print("*",end="")
        else:
            print("-",end="")
        j=j+1
    i=i+1
"""    

#question==65
"""
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
"""
"""
n = int(input("enter no: "))
i = 0

while i < n:
    print()

    # spaces
    s = 0
    while s < n - i - 1:
        print(" ", end="")
        s = s + 1

    # numbers
    k = 1
    j = 0

    while j <= i:
        print(k, end=" ")

        k = k * (i - j) // (j + 1)

        j = j + 1

    i = i + 1
"""
#qestion==66
"""
    1
   1*1
  1***1
 1*****1
111111111	
 
"""
"""
n=int(input("enter "))
i=1
while i<=n:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i*2-1:
        if j==1 or i==n or j==i*2-1:
            print("1",end="")
        else:
            print("*",end="")
        j=j+1
    i=i+1
"""











#question==67
"""
    A
   B B
  C   C
 D     D
EEEEEEEEE
"""
"""
n=int(input("enter no:"))
i=1
k=65
while i<=n:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
 
    
    while j<=i*2-1:
        if j==1 or i==n or j==i*2-1:
            print(chr(k),end="")
        else:
            print(" ",end="")
        j=j+1
    k=k+1
    i=i+1
"""
#question=68
"""
    #
   *#* 
  **#** 
 ***#*** 
****#****
"""
"""
n=int(input("enetr no:"))
i=1
while i<=n:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i*2-1:
        if j==i:
            print("#",end="")
        else:
            print("*",end="")
        j=j+1
    i=i+1
       
        
 """   
#question==69
"""   
*********
 ******* 
  ***** 
   ***
    * 

"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i*2-1:
        print("*",end="")
        j=j+1
    i=i-1

"""
#question==70
"""
 * * * * * 
  * * * * 
   * * * 
    * * 
     *
"""
"""
n=int(input("enter:"))
i=n
while i>=1:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print("* ",end="")
        j=j+1
    i=i-1


"""
#question==71
"""
123456789
 1234567
  12345
   123
    1

"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i*2-1:
        print(j,end="")
        j=j+1
    i=i-1

"""
#question==72
"""
A B C D E
 A B C D
  A B C
   A B
    A
"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    k=65
    while j<=i:
        print(chr(k)+" ",end="")
        k=k+1
        j=j+1
    i=i-1
"""


#question==73
"""
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1
"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print(str(i)+" ",end="")
        j=j+1
    i=i-1

"""
#question==74
"""
123456789
 1     7
  1   5
   1 3
    1

"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i*2-1:
        if j==1 or j==i*2-1 or i==n:
            print(j,end="")
        else:
            print(" ",end="")
        j=j+1
    i=i-1


"""



#question==75
"""
123456789
 1+++++7
  1+++5
   1+3
    1
"""
"""
n=int(input("enter no:"))
for i in range(n,0,-1):
    print()
    for s in range(1,n-i+1):
        print(" ",end="")
    for j in range(1,((i*2)-1)+1):
        if j==1 or i==n or j==i*2-1:
            print(j,end="")
        else:
            print("+",end="")
       

"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i*2-1:
        if j==1 or i==n or j==i*2-1:
            print(j,end="")
        else:
            print("+",end="")
        j=j+1
    i=i-1

"""

#question==76
"""
x
xx
xxx
xxxx
xxx
xx
x
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    i=i+1
i=n-1
while i>=1:
    print()
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    i=i-1
    
        
"""



#question==77
"""
1
12
123
1234
123
12
1
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    i=i+1
i=n-1
while i>=1:
    print()
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    i=i-1
"""
"""
n=int(input("enter no:"))
for i in range(1,n+1):
    print()
    for j in range(1,i+1):
        print(j,end="")
for e in range(n-1,0,-1):
    print()
    for j in range(1,e):
        print(j,end="")
"""
#question==78
"""
   1
  12
 123
1234
 123
  12
   1
"""
"""
n=int(input("enter no :"))
i=1
while i<=n:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    i=i+1
i=n-1
while i>=1:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    i=i-1

"""



















#question==79
"""
1
1 2
1  3
1   4
1  3
1 2
1
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if j==1 or i==j:
            print(j,end="")
        else:
            print(" ",end="")
        j=j+1
    i=i+1
i=n-1
while i>=1:
   print()
   j=1
   while j<=i:
        if j==1 or i==j:
            print(j,end="")
        else:
            print(" ",end="")
        j=j+1
   i=i-1

"""
#question==80
"""
   *
  *_*
 *_*_*
*_*_*_*
 *_*_*
  *_*
   *
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i*2-1:
        if j==1 or j%2!=0 or j==i*2-1:
            print("*",end="")
        else:
            print("_",end="")
        j=j+1
    i=i+1

i=n-1
while i>=1:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i*2-1:
        if j==1 or j%2!=0 or j==i*2-1:
            print("*",end="")
        else:
            print("_",end="")
        j=j+1
    i=i-1

"""












#question==81
"""
   *
  ***
 ***** 
******* 
 ***** 
  *** 
   *

"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i*2-1:
        print("*",end="")
        j=j+1
    i=i+1

i=n-1
while i>=1:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i*2-1:
        print("*",end="")
        j=j+1
    i=i-1
"""
#question==82
"""
   *
  *_* 
 *___* 
*_____*
 *___* 
  *_*
   *
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    s=0
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i*2-1:
        if j==1 or j==i*2-1:
            print("*",end="")
        else:
            print("-",end="")
        j=j+1
    i=i+1
i=n-1
while i>=1:
    print()
    s=1
    while s<=n-i+1:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i*2-1:
        if j==1 or j==i*2-1:
            print("*",end="")
        else:
            print("-",end="")
        j=j+1
    i=i-1

"""
#question==83
"""
    1
   212
  32123
 4321234
543212345

"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=i
    while j>=1:
        print(j,end="")
        j=j-1
    k=1
    j=i
    while j>1:
        print(k,end="")
        k=k+1
        j=j-1
    i=i+1

"""

#question== 84
"""
*        *
**      **
***    ***
****  ****
***** *****
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    s=1
    while s<=(n-i)*2:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
       print("*",end="")
       j=j+1
    i=i+1
"""
#question==85
"""
***** *****
****   ****
***     ***
**       **
*         *
"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    j=i
    while j>=1:
        print("*",end="")
        j=j-1
    s=1
    while s<=(n-i)*2:
        print(" ",end="")
        s=s+1
    j=i
    while j>=1:
        print("*",end="")
        j=j-1
    i=i-1
"""
#question==86
"""

***** *****
****   ****
***     ***
**       **
*         *
*         *
**       **
***     ***
****   ****
***** *****
"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    j=1
    while j<=i:
        print("#",end="")#or "*"
        j=j+1
    s=1
    while s<=(n-i)*2:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    i=i-1


#second half loop
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    s=1
    while s<=(n-i)*2:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print("#",end="")#"*"
        j=j+1
    i=i+1

"""
#question==87
"""
    1
    2
    3
    4
123454321
    4
    3
    2
    1
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=n:
      
       print(j,end="")
      
       j=j+1
    i=i+1

"""
#question==88
"""
     1               
    101            
   10101         
  1010101           
 101010101   
10101010101

"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=(i*2)-1:
        if j%2==0:
            print("0",end="")
        else:
            print("1",end="")
        j=j+1
    i=i+1
"""
#question==89
"""
*         *
  *      *
    *  *
     *
    *  *
  *      *
 *         *
 

"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    s=1
    while s<=i:
        print(" ",end="")
        s=s+1
    
    j=1
    while j<=i:
        if j==i:
            print("*",end="")
        j=j+1
    s=1
    while s<=(n-i)*2:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        if j==i :
            print("*",end="")
        j=j+1
    i=i+1
i=1
while i<=n:
    print()
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1

    
    j=1
    while j<=i:
        if j==1:
            print("*",end="")
        j=j+1
    s=1
    while s<=(i*2)-1:
        print(" ",end="")
        s=s+1
         
           
    j=1
    while j<=i:
        if j==i:
            print("*",end="")
        j=j+1
    i=i+1




"""





















































