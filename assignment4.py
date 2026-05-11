#question1
"""
total_bill=int(input("enter the total amount:"))
gst=int(input("enter the tax value:"))
service_charge=int(input("enter the tax value:"))
no=int(input("enter no of friends:"))
final=total_bill*0.05+total_bill*0.1+total_bill
t=final//no
print("total bill",final)
print("each pays:",t)
"""

#question2

"""
mp=int(input("enter the price:"))
dp=int(input("enter the dp:"))
ir=int(input("enter the ir:"))
m=int(input("enter the month:"))

a=mp-dp
b=(a*0.1)+a

c=b/m
print("remaining amount:",a)

print("total with intrest:",b)
print("total emi",c)

"""
#question3
"""
m,n,p,q,r=map(int,input("enter the marks:").split())
t=m+n+p+q+r
b=t/5
p=(t/500)*100
print("total no:",t)
print("average:",b)
print("percent:",p)
"""


#question4  travel distance

"""
speed=int(input("enter the speed km/h:"))
h,m=map(int,input("enter the time:").split())
t=h+(m/60)

print("total time hours:",t)
print("distance in km/h:",speed*t)

"""
#question5 salary breakdown
"""
ms=int(input("enter the monthly salary:"))
wd=int(input("enter the total working day:"))
sph=int(input("enter the salary perhour:"))

salary_day=ms/wd
day=36000/(wd*sph)

print("salary per day=",salary_day)
print("salry per hours=",day)
"""

#question6
"""
data=int(input("enter the data in GB:"))

mb=data*1024
kb=data*1048576
print("mb=",mb)
print("kb=",kb)


"""

#question7
"""
run=int(input("enter the total run:"))
over=float(input("enter the total over:"))
tb=(over*10)
x=tb%10
y=tb//10
ttlb=(y*6)+x
rr=run/(ttlb/6)
print("total ball=",ttlb)
print("run rate=",rr)
"""



#question 8
"""

p=int(input("enter the princple value:"))
r=int(input("emter the rate:"))
t=int(input("enter thetime in year:"))

ci=(p*(1+(r/100))**t)-p
print("the total compound intrest is:",ci)
print("the total amountis:",p+ci)

"""

#question9

"""
d=int(input("enter the distance:"))
m=int(input("enter the mileage (km/litre):"))
pp=int(input("enter the petrol price(litre)"))

petrol_used=d/m
petrol_cost=petrol_used*pp

print("petrol used:",petrol_used,"km/litre")
print("total cost:",petrol_cost)

"""

#question 10
"""
tsec=int(input("enter the total sec:"))

hours=tsec//3600
minute=(tsec%3600)//60
sec=tsec%3600%60

print("hours",hours)
print("minute",minute)
print("sec",sec)
"""


#question11
#a=50+(10*(+(2*3)))/4-(-6%4)
#print(a)


#question12
"""
a=100-(20*(3**2))+(40/(+5))-(-3)

print(a)
"""
"""

a=25+(5*(6**2)//3)-(-(8%5))+(+2)
print(a)		

"""

















