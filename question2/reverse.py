def rev(n):
    re=0
    while n>0:
        rem=n%10
        re=re*10+rem
        n=n//10
    print("reverse no",re)