#question =1 smart credit card approval system   
"""
i=int(input("income= "))
cs=int(input("credit score= "))
e=input("Employment= ").lower()
d=int(input("debt= "))
if i>=50000:
    if cs>=750:
        if d<=20000:
            ct="Approve premium card"
        else:
            ct="Gold card"
    else:
        if e=="goverment" and  cs>=650:
            ct="Gold card"
        else:
            ct="Reject"
else:
    if i>=30000 and cs>=700:
        ct="Silver card"
    else:
        ct="Reject"
print("card type=",ct)
"""

#question =2   hospital emergency priority system
"""
a=int(input("Age= "))
s=input("Severity= ").lower()
i=input("insurance (yes/no)= ").lower()
if s=="critical":
    if a>=60:
        t="Immediate ICU"
    else:
        t="Emergency ward"
elif s=="moderate":
    if i=="yes":
        t="assign priority treatment"
    else:
        t="assign general queue"
else:
    if a<=10:
        t="pediatic priority"
    else:
        t="assign wait"
print("Treatment=",t)
    
"""
#question ==3       smart scholarship allocation system
"""
m=int(input("Marks= "))
i=int(input("Income= "))
c=input("category= ").lower()
if m>=85:
    if i<=300000:
        if c!="general":
            s="Full scholarship"
        else:
            s="75% scholarship"
    else:
        s="50% scholarship"
else:
    if 70<m<84:
        if i<=200000:
            s="50% scholarship"
        else:
            s="25% scholarship"
    else:
        s="No scholarship"
print("Scholarship=",s)
"""


#question=4       airline ticket pricing engine
"""
c=input("Class: ").lower()
d=int(input("Distance: "))
b=input("Booking: ").lower()
if c=="business":
    if d>1000:
        tp="8000"
    else:
        tp="5000"
else:
    if c=="economy":
        if d>1000:
            if b=="early":
                tp="4000"
            else:
                tp=="5000"
        else:
             if d<=1000:
                 tp="2500"
print("Ticket price=",tp)
  """


#question =5       smart evalution system
"""
m=int(input("Marks: "))
a=int(input("Attendance: "))
i=int(input("Internal: "))
if m>=40:
    if a>=75:
        if i>=20:
            r="Pass"
        else:
            r="Grace pass"
    else:
        r="Result is detained"
else:
    if m>=35 and i>=25:
        r="Result is reappear"
    else:
        r="Fail"
print("Result=",r)
"""


#question =6        banking fraud detection system
"""
a=int(input("Amount:"))
t=int(input("Transaction:"))
l=input("Location:").lower()
d=input("Device:").lower()
us=input("unsual actiity(yes/no): ").lower()
if a>=50000:
    if l=="international":
        if d=="new":
            if t>3:
                rl="High risk"
            else:
                rl="medium risk"
        else:
            rl="medium risk"
    else:
        if t>5:
            rl="medium risk"
        else:
            rl="low risk"
else:
    if us=="yes":
        if d=="new":
            rl="medium risk"
        else:
            rl="low risk"
    else:
        rl="Safe"
print("Risk level=",rl)
   """

#question=7    university result classification system
"""
m=int(input("Marks: "))
b=int(input("Backlog: "))
p=int(input("Project: "))
if m>=75:
    if b==0:
        if p>=80:
            r="First class with Distinction"
        else:
            r="First class "
    else:
        r="First class"
elif 60<m<74:
    if b<=2:
        r="Second class"
    else:
        r="Pass class"
else:
    if 50<m<59:
        r="Pass"
    else:
        r="Fail"
print("Result=",r)

"""

#question=8    ecommerce dynamic pricing system
"""
d=int(input("Demand: "))
s=int(input("Stock:"))
ut=input("Usertype:").lower()
f=input("Festival: ").lower()
if d>=80:
    if s<50:
        if ut=="premium":
            if f=="yes":
                d="20%"
            else:
                d="10%"
        else:
            d="no discount"
    else:
        d="no discount"
elif 40<d<79:
    if f=="yes":
        d="10%"
    else:
        d="no discount"
else:
    if s>200:
        d="15%"
    else:
        d="no discount"
print("Discount:",d)
"""

#question =9       smart loan eligibility system 
"""
s=int(input("enter your salary:"))
age=int(input("enter your age"))
cs=int(input("enter credit score"))
emi=int(input("enter emi"))
if s>=40000:
    if 21<age<60:
        if cs>=750:
            if emi<=(s*0.4):
                print("8 % approve")
            else:
                print("10% approve")
        else:
            if cs>650:
                print("12% approve")
            else:
                print("reject")
else:
    if s>25000:
        if cs>700:
            print("13% approve")
        else:
            print("reject")

"""

























