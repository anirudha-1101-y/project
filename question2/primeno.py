def prino(n):
    if n>1:
        x=0
        for i in range(2,n//2+1):
            if n%i==0:
                x=1
                break
        if x==0:
            print("prime no")
        else:
            print("not a prime no")
    else:
        print("not a prime number")
