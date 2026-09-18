import question4
from question4 import age,cl,vowel,remove,long
while True:
    print("========== EMPLOYEE DATA PROCESSING SYSTEM ==========")
    print("1. Find Second Highest Employee Age")
    print("2. Count Senior Employees")
    print("3. Remove Duplicate Ages")
    print("4. Count Names Starting with a Vowel")
    print("5. Find Longest Employee Name")
    print("6. Exit")
    ch=int(input("enter choice: "))
    match ch:
        case 1:
             l=list(map(int,input("enter your age: ").split()))
             print("second highest employee age",age.age(l))
        case 2:
             l=list(map(int,input("enter your age: ").split()))
             print("senior count",cl.cl(l))
        case 3:
            l=list(map(int,input("enter your age: ").split()))
            print("remove duplicate value:",remove.remove(l))
        case 4:
            n=list(map(str,input("enter your name: ").split()))
            print("name startswith vowel",vowel.vowel(n))
        case 5:
            n=list(map(str,input("enter your name: ").split()))
            print("longest name",long.long(n))



        case 6:
            print("exit")
            break