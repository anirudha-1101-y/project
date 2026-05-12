"""
1) Hollow Pyramid
        *
       * *
      *   *
     *     *
    *********
"""




"""
2) Hollow Rectangle
    *********
    *       *
    *       *
    *       *
    *********
"""
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    j=i
    while j>=1:
        if i==j:
            print("*",end="")
        elif j==1:
            print("*",end="")
        else:
            print(" ",end="")

   
        j=j-1
    i=i-1
"""





"""
3) X Star Pattern
    *   *
     * *
      *
     * *
    *   *
"""
"""
4) Vertical Diamond
       *
      * *
     *   *
    *     *
     *   *
      * *
       *
"""
"""
5) Number-Star Palindrome
    12344321
    123**321
    12****21
    1******1
"""
"""
n=int(input("enter   no:"))
i=n
while i>=1:
    print()
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    

    space=1
    while space<=(n-i)*2:
        print("*",end="")
        space=space+1

    j=i
    while j>=1:
        print(j,end="")
        j=j-1
    i=i-1
"""














"""
6) Number Triangle with Dashes
    - - - - 1
    - - - 2 3
    - - 3 4 5
    - 4 5 6 7
    5 6 7 8 9
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    d=1
    while d<=n-i:
        print("-",end="")
        d=d+1
    j=1
    k=i
    while j<=i:
        print(k,end="")
        k=k+1
        j=j+1
      
    i=i+1

"""


"""
7) Reverse Number Triangle
    - - - -
    2 - - -
    4 3 - -
    6 5 4 -
    8 7 

"""







"""

8) Border Number Pattern
    1 2 3 4 5
    2       5
    3       5
    4       5
    5 5 5 5 5
"""
"""
9) Hollow Diamond Square
    ***********
    ****   ****
    ***     ***
    **       **
    *         *
    *         *
    **       **
    ***     ***
    ****   ****
    ***********
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    space=n
    while space>=i:
        print("*",end="")
        space=space-1
    j=i
    while j>1:
        print("  ",end="")
        j=j-1
    space=n
    while space>=i:
        print("*",end="")
        space=space-1
    i=i+1
i=1
while i<=n:
    print()
    space=1
    while space<=i:
        print("*",end="")
        space=space+1
    
    j=1
    while j<=n-i:
        print("  ",end="")
        j=j+1
    space=1
    while space<=i:
        print("*",end="")
        space=space+1
    i=i+1


"""
 

"""
10) Slanted Star Block
    ****
     ****
      ****
       ****
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    space=1
    while space<=i:
        print(" ",end="")
        space=space+1
    


    j=1
    while j<=n:
        print("*",end="")
        j=j+1
    i=i+1
 """

"""
11) Butterfly Number Pattern
    1      1
    12    21
    123  321
    12344321
    123  321
    12    21
    1      1

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

    space=1
    while space<=2*(n-i):
        print(" ",end="")
   
        space=space+1
    j=i
    while j>=1:
        print(j,end="")
        j=j-1

    i=i+1
i=n-1
while i>=1:
    print()
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
    space=1
    while space<=2*(n-i):
        print(" ",end="")
        space=space+1
    j=i
    while j>=1:
        print(j,end="")
        j=j-1
    i=i-1
    
"""

"""
12) Hollow Diamond Numbers
       1
      2 2
     3   3
    4     4
     3   3
      2 2
       1
"""
"""
13) Number X Pattern
    1   5
     2 4
      3
     2 4
    1   5

"""
"""

14) Spiral Number Square
     1   2   3   4
    12  13  14   5
    11  16  15   6
    10   9   8   7

"""
"""
15) Zig-Zag Star
    *   *   *
      *   *
    *   *   *
"""
"""
16) Palindrome Pyramid
            1
           121
          12321
         1234321
        123454321
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    space=1
    while space<n-i:
        print(" ",end="")
        space=space+1
    k=1
    while k<i:
        print(k,end="")
        k=k+1
    j=i
    while j>=1:
        print(j,end="")
        j=j-1
    i=i+1
    
"""
    





"""
17) Hollow Hourglass
    * * * * *
      *     *
        * *
          *
        * *
      *     *
    * * * * *
"""
"""

18) Binary Floyd Triangle
    1
    0 1
    1 0 1
    0 1 0 1
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




"""
19) Reverse Number Cross
    5   5
     4 4
      3
     4 4
    5   5
"""
"""
20) Continuous Diamond Numbers
           1
          2 3
         4 5 6
        7 8 9 10
         4 5 6
          2 3
           1

"""
"""

21) Hollow Pyramid (Practice)
            *
           * *
          *   *
         *     *
        *********
"""
"""
22) Inverted Hollow Pyramid
    *********
     *     *
      *   *
       * *
        *
"""
"""
23) Plus Star Pattern
          *
          *
    *********
          *
          *
"""
"""
24) Hollow X Pattern
    *   *
     * *
      *
     * *
    *   *
"""
"""
25) Number Sandglass
    123454321
     1234321
      12321
       121
        1
       121
      12321
     1234321
    123454321
"""
n=int(input("enter no:"))
i=n
while i>=1:
    print()
    space=0
    while space<=n-i:
        print(" ",end="")
        space=space+1
    j=1
    while j<=i:
        print(j,end="")
        j=j+1
  
       i=i-1
 








"""
26) Right Hollow Number Triangle
    1
    12
    1 3
    1  4
    12345
"""







"""
27) Continuous Number Pyramid
            1
           2 3
          4 5 6
         7 8 9 10

"""
"""
n=int(input("enter no:"))
i=1
k=1
while i<=n:
    print()
    space=1
    while space<=(n-i):
        print(" ",end="")
        space=space+1
    j=1
    while j<=i:
        print(k,end="")
        k=k+1
        j=j+1
    i=i+1

"""
"""
28) Hollow Square
    *****
    *   *
    *   *
    *   *
    *****
"""
"""
29) Diagonal Number Square
    1 - - -
    - 2 - -
    - - 3 -
    - - - 4
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    j=1
    while j<=n:
        if j==i:
            print(j,end="")
        else:
            print("-",end="")
        j=j+1
    i=i+1

"""

"""
30) Extended Slanted Star Block
    ****
     ****
      ****
       ****
        ****
"""
"""
n=int(input("enter no:"))
i=1
while i<=n:
    print()
    space=0
    while space<=i:
        print(" ",end="")
        space=space+1
    j=1
    while j<=n:
        print("*",end="")
        j=j+1
    i=i+1

"""





