"""
n=int(input("enter no"))
sum=1
for i in range(n,0,-1):
    sum=sum*i
print("factorial is",sum)

"""
n=int(input("enter no"))
if n%2==0:
    print(n," = even ")
else:
    print(n, " = odd")