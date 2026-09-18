"""
1.
=========================================================
        MATRIX OPERATIONS MANAGEMENT SYSTEM
=========================================================


A data analysis company stores numerical information in matrix form.
To help employees perform matrix-related operations efficiently,
the company wants a menu-driven application.

The application should allow the user to:

1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

The user must enter the number of rows, columns, and all matrix
elements. The program should perform the selected operation and
display the result.

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user chooses Exit.

   1. Add Two Matrices
   2. Subtract Two Matrices
   3. Compare Two Matrices
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all elements of Matrix A and Matrix B from the user whenever
   required.

4. Based on the user's choice:

   Choice 1 - Add Two Matrices
   --------------------------------
   Add corresponding elements of both matrices and display
   the resultant matrix.

5. Choice 2 - Subtract Two Matrices
   --------------------------------
   Subtract corresponding elements of Matrix B from Matrix A
   and display the resultant matrix.

6. Choice 3 - Compare Two Matrices
   --------------------------------
   Check whether both matrices are equal.

   Two matrices are considered equal if:
   - They have the same dimensions.
   - Corresponding elements are equal.

   Display:
   "Matrices are Equal"
   or
   "Matrices are Not Equal"

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Operations Management System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 1

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
5 6
7 8

Result Matrix:
6 8
10 12

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 3

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
1 2
3 4

Output:
Matrices are Equal

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Operations Management System

=========================================================
"""
"""
while True:

    print("========menu===============")
    print("1. Add two matrix")
    print("2. subtract two matrix")
    print("3. compare two matrix")
    print("4.exit")
    

    choice=int(input("enter your choice"))
  
    match choice:
        

        case 1:
            rows=int(input("enter no of rows"))
            cols=int(input("enter no of cols"))
            
            print("matrix one")
            mat1=[]
            for i in range(rows):
                row=[]
                for j in range(cols):
                    x=int(input("enter element"))
                    row.append(x)
                mat1.append(row)
            print("matrix==2")
            mat2=[]
            for i in range(rows):
                row=[]
                for j in range(cols):
                    x=int(input("enter elelemnt"))
                    row.append(x)
                mat2.append(row)
            
            print("matrix==3" "before addition")
            mat3=[]
            for i in range(rows):
                row=[]
                for j in range(cols):
                    row.append(0)
                mat3.append(row)
            for i in range(len(mat3)):
                for j in range(len(mat3[i])):
                    mat3[i][j]=mat1[i][j]+mat2[i][j]

            print("matrix")
            for i in mat1:
                for j in i:
                    print(j,end=" ")
                print()
            print("matrix=2")
            for i in mat2:
                for j in i:
                    print(j,end=" ")
                print()
            print("matrix==3 after adding of matrix one nd mtrix two")
            for i in mat3:
                for j in i:
                    print(j,end=" ")
                print()
        case 2:
            rows=int(input("enter no of rows"))
            cols=int(input("enter no of cols"))
            print("matrix one")
            mat1=[]
            for i in range(rows):
                row=[]
                for j in range(cols):
                    x=int(input("enter element"))
                    row.append(x)
                mat1.append(row)
            print("matrix==2")
            mat2=[]
            for i in range(rows):
                row=[]
                for j in range(cols):
                    x=int(input("enter elelemnt"))
                    row.append(x)
                mat2.append(row)
            
            
            mat3=[]
            for i in range(rows):
                row=[]
                for j in range(cols):
                    row.append(0)
                mat3.append(row)
            for i in range(len(mat3)):
                for j in range(len(mat3[i])):
                    mat3[i][j]=mat2[i][j]-mat1[i][j]

            print("matrix")
            for i in mat1:
                for j in i:
                    print(j,end=" ")
                print()
            print("matrix=2")
            for i in mat2:
                for j in i:
                    print(j,end=" ")
                print()
            print("matrix==3 after Subtractinf  of matrix one nd mtrix two")
            for i in mat3:
                for j in i:
                    print(j,end=" ")
                print()

        case 3:


            if mat1==mat2:
                print("==same matrix ")
            else:
                print("==not same matrix")
        case 4:
            print("exit")
            break
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

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Prime Numbers Row-wise
   2. Count Perfect Numbers Column-wise
   3. Display Row-wise Sum
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Prime Numbers Row-wise
   ---------------------------------------
   Count and display the number of prime numbers present
   in each row of the matrix.

5. Choice 2 - Count Perfect Numbers Column-wise
   --------------------------------------------
   Count and display the number of perfect numbers present
   in each column of the matrix.

   Note:
   A perfect number is a number that is equal to the sum
   of its proper divisors.

   Examples:
   6  = 1 + 2 + 3
   28 = 1 + 2 + 4 + 7 + 14

6. Choice 3 - Display Row-wise Sum
   --------------------------------
   Calculate and display the sum of each row.

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
2 4 5
6 7 8
11 28 13

Output:
Row 1 Prime Count = 2
Row 2 Prime Count = 1
Row 3 Prime Count = 2

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 2

Output:
Column 1 Perfect Number Count = 1
Column 2 Perfect Number Count = 1
Column 3 Perfect Number Count = 0

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 3

Output:
Row 1 Sum = 11
Row 2 Sum = 21
Row 3 Sum = 52

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Analysis System

=========================================================

"""
"""

while True:
    print("1. Count Prime Numbers Row-wise")
    print("2. Count Perfect Numbers Column-wise")
    print("3. Display Row-wise Sum")
    print("4. Exit")

    rows=int(input("enter no of rows"))
    cols=int(input("enter no of column"))
    mat=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            x=int(input("enter element:-"))
            row.append(x)
        mat.append(row)
    choice=int(input("enter your choice "))

    match choice:
        case 1:
            print("output :")
            for i in range(len(mat)):
                c=0
                for j in range(len(mat[i])):
                    a=mat[i][j]
                    if a>1:
                        for k in range(2,a//2+1):
                            if a%k==0:
                                break
                        else:
                            c=c+1
                    

                print("row",i+1,"prime count",c)
        case 2:
            print("output :")
            for i in range(len(mat[0])):
                c=0
                sum=0
                for j in range(len(mat)):
                    a=mat[i][j]
                    for k in range(a//2+1):
                        if a%2==0:
                            sum=sum+k
                    else:
                        if sum==a:
                            c=c+1
                print("column",i+1,"perfect number count",c)
        case 3:
            print("output :")
            for i in range(len(mat)):
                sum=0
                for j in range(len(mat[i])):
                    a=mat[i][j]
                    sum=sum+a
                print("row",i+1,"sum=",sum)
        case 4:
            print("Thank You for Using Matrix Analysis System")
            break

      """      
"""
3.

=========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================

Scenario

A manufacturing company records quality inspection values in
matrix form. The Quality Control team wants a menu-driven
application to analyze the inspection data and generate reports.

The application should allow the user to:

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Armstrong Numbers Row-wise
   2. Count Palindrome Numbers Column-wise
   3. Display Average of Each Row
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Armstrong Numbers Row-wise
   -------------------------------------------
   Count and display the number of Armstrong numbers
   present in each row.

   Examples:
   153, 370, 371, 407

5. Choice 2 - Count Palindrome Numbers Column-wise
   -----------------------------------------------
   Count and display the number of palindrome numbers
   present in each column.

   Examples:
   121, 131, 444, 1221

6. Choice 3 - Display Average of Each Row
   --------------------------------------
   Calculate and display the average of each row.

7. Choice 4 - Exit
   --------------------------------------
   Display:
   "Thank You for Using Matrix Quality Check System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
153 121 10
370 22 44
407 15 131

Output:
Row 1 Armstrong Count = 1
Row 2 Armstrong Count = 1
Row 3 Armstrong Count = 1

---------------------------------------------------------

Enter your choice: 2

Output:
Column 1 Palindrome Count = 0
Column 2 Palindrome Count = 3
Column 3 Palindrome Count = 2

=========================================================
"""
"""
while True:
    print("1. Count Armstrong Numbers Row-wise")
    print("2. Count Palindrome Numbers Column-wise")
    print("3. Display Average of Each Row")
    print("4. Exit")

    rows=int(input("enter no of rows"))
    cols=int(input("enter no of "))

    mat=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            x=int(input("enter element "))
            row.append(x)
        mat.append(row)
    choice=int(input("enter youe choice : "))

    match choice:
        case 1:
            print("output :")
            for i in range(cols):
                c=0
                for j in range(rows):

                    n=mat[j][i]
                    rev=0
                    temp=n
                    while n>0:
                        rem=n%10
                        rev=rev*10+rem
                        n=n//10
                    else:
                      if rev==temp:
                        c=c+1
                print("column",i+1,"plaindrome count",c)
        case 2:
            print("output : ")
            for i in range(len(mat)):
                c=0
                for j in range(len(mat[i])):
                    n=mat[i][j]
                    b=n
                    sum=0
                    while n>0:
                        rem=n%10
                        sum=sum+rem**len(str(b))
                        n=n//10
                    else:
                        if sum==b:
                            c=c+1
                print("row",i+1,"armstrong count",c)
        case 3:
            for i in range(len(mat)):
                sum=0
                for j in range(len(mat[i])):
                    n=mat[i][j]
                    sum=sum+n

                else:
                    av=sum//len(mat[i])
                print("row",i+1,"avareage",av)

"""

"""
4.

=========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================

Scenario

A security company stores surveillance data in matrix form.
The analyst wants a menu-driven application to examine the
diagonal elements of the matrix and generate reports.

The application should allow the user to:

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Display Main Diagonal Elements
   2. Display Secondary Diagonal Elements
   3. Compare Main and Secondary Diagonal Sums
   4. Exit

2. Read the size of a square matrix from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Display Main Diagonal Elements
   -----------------------------------------
   Display all elements present in the main diagonal.

5. Choice 2 - Display Secondary Diagonal Elements
   ----------------------------------------------
   Display all elements present in the secondary diagonal.

6. Choice 3 - Compare Main and Secondary Diagonal Sums
   ---------------------------------------------------
   Calculate the sum of both diagonals and display:

   - Main Diagonal Sum
   - Secondary Diagonal Sum
   - Which diagonal has the greater sum
   - Or whether both sums are equal

7. Choice 4 - Exit
   -----------------------------------------
   Display:
   "Thank You for Using Matrix Diagonal Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Enter size of matrix: 3

Enter matrix elements:

1 2 3
4 5 6
7 8 9

Menu
1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

Enter your choice: 1

Output:
Main Diagonal Elements:
1 5 9

---------------------------------------------------------

Enter your choice: 2

Output:
Secondary Diagonal Elements:
3 5 7

---------------------------------------------------------

Enter your choice: 3

Output:
Main Diagonal Sum = 15
Secondary Diagonal Sum = 15
Both Diagonal Sums are Equal

=========================================================



                        
"""
"""
while True:
    print("1. Display Main Diagonal Elements")
    print("2. Display Secondary Diagonal Elements")
    print("3. Compare Main and Secondary Diagonal Sums")
    print("4. Exit")

    rows=int(input('enter no of rows: '))
    cols=int(input("enter no of column: "))
    mat=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            x=int(input("enter element : "))
            row.append(x)
        mat.append(row)
    
    choice=int(input("enter your choice : "))

    match choice:
        case 1:
            if rows==cols:

                for i in range(len(mat)):
                    print(mat[i][i],end=" ")
                print()
            else:
                print("daigonal are not found")
        case 2:
            if rows==cols:

                for i in range(cols):
                    print(mat[i][cols-i-1],end=" ")
                print()

            else:
                print("daigonal are not found ")
        case 3:
            sum=0
            sum1=0
            for i in range(cols):
                sum=sum+mat[i][i]
            for i in range(cols):
                sum1=sum1+mat[i][cols-i-1]
            print("Main Diagonal Sum",sum)
            print("Secondary Diagonal Sum",sum1)

            if sum==sum1:
                print("Both Diagonal Sums are Equal")
            else:
                print("not same")
        case 4:
            print("exit")
            break


          """

      

                


                    

