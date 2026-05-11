# insurance claim approval system
"""
age=int(input("enter policy age:" ))
ca=int(input("enter claim amount:"))
at=input("enter Accident type:")
if age>=2:
    if ca<50000:
        if at=="minor":
            print("claim status= approve the claim")
        else:
            print("approve with investigation")
     
    else:
        if 50001<ca<200000:
            if at=="major":
                print("approve the investigation")
            else:
                print("claim status =rejected")
else:
    if at=="minor":
        print("claim status= rejected")
    else:
        print("pending review")
"""

#question =2      university admssion system
"""
m=int(input("marks= "))
es=int(input("entrance score= "))
c=input("category")
if m>=70:
    if es>=80:
        if c=="general":
            a=" Admitted"
        else:
            a="Admit with scholarship"
    else:
        if m>=85:
            a="Admit under management quota"

        else:
            a="Reject"
else:
    if c!="general" and m>=60:
        if ec>=70:
            a="Waiting list"
        else:
            a="Reject"
    else:
        a="REJECTED"
print("Addmission  status =",a)

"""

# question 3     smart loan risk categorization
"""
s=int(input("enter your salary: "))

cs=int(input("enter credit score: "))
el=int(input("existing loans= "))
if s>=30000:
    if cs>=750:
        if el==0:
            l="Low Risk" 
        elif 0<el<2:
            l="Medium Risk"

        else:
            l="High Risk"
    else:
        if s>=50000:
            if cs>=650:
                l="Medium Risk"
            else:
                l="High Risk"
else:
    l="NOT Eligible"
print("Risk Level= ",l)
"""

#question 4       E learning course access system
"""
sb=input("enter subscription: ").lower()
p=int(input("enter Progress: "))
ts=int(input("enter Test score:"))
if sb=="premium":
    if p>=80:
        if ts>=70:
            a="unlock cretificate"
        else:
            a="Retry test"
    else:
        a="pls complete course"

elif sb=="basic":
    if p>=50:
        a="limited access"
    else: 
        a="lock content"
else:
    a="deny access"
print("Access Status=",a)

"""
#question =5       smart warehouse dispatch system
"""
s=int(input("enter stock= "))
p=input("enter Priority= ").lower()
d=int(input("enter distance= "))
if s>=100:
    if p=="high":
        if d<=200:
            ds="dispatch immediately"
        else:
            ds="fast courier"
    else:
        if s<=300:
            ds="bulk dispatch"
        else:
            ds="normal dispatch"
else:
    if s<=50 and p=="high":
        ds="partially dispatch"
    elif p=="low":
        ds="hold"
    else:
        d="mark out of stock"
print("Dispatch status=",ds)
  """
#question =6    banking fraud detection system
"""
ta=int(input("enter transaction amount: "))
l=input("enter kocation: ").lower()
aa=int(input("enter account age: "))
otp=input("enter OTP (yes/no) : ").lower()
us=input("enter unusual activity(yes/no): ").lower()
if ta>=10000:
    if l=="international":
        if otp=="yes":
            ts="Allow" 
        else:
            ts="Block"
    else:
        if ta>=50000:
            if aa>=2:
                ts="Allow"
            else:
                ts="Flagged"
        else:
            ts="Allow"
else:
    if us=="yes":
       ts="flagged"
    else:
        ts="Allowed"
print("Transaction status= ",ts)
"""
#question =7          ride booking surge pricing
"""
de=int(input("Demand= "))
t=input("time= ").lower()
di=int(input("Distance= "))

if de>=80:
    if t=="peak":
        if di>=10:
            f="2xfare"
        else:
            f="1.5xfare"
    else:
        if de>=90:
            f="1.8xfare"
        else:
            f="1.3xfare"
else:
    if de>=50:
        if t=="peak":
            f="1.2xfare"
        else:
            f="normal fare"
    else:
        f="normal fare"
print("fare multiplier= ",f)     
"""



#question =8            smart farning irrigation system   
"""
sm=int(input("soil moisture: "))
t=int(input("enter temperature: "))
c=input("enter crop: ").lower()
r=input("Rainfall expexted(yes/no) ").lower()

if sm<=30:
    if t>=35:
        if c=="wheat":
            i="High water supply"
        else:
            i="Moderate supply"
    else:
        i="Moderate supply"
elif 30<sm<60:
    if r=="yes":
        i="delay irrigation"
    else:
        i="light irrigation"
else:
     i="no irrigation"
print("irrigation=",i)


"""

#question=9        multilevel employee promotion system 
"""
e=int(input("Experience: "))
r=int(input("Rating: "))
p=int(input("project: "))
s=int(input("salary: "))
if e>=5:
    if r>=4:
        if p>=3:
            if s>=50000:
                ps="promoted with 30% hike"
            else:
                ps="promoted with 20% hike"
        
        else:
            ps="promoted with 10% hike"
    else:
        ps="no promotion"
else:
    if r==5:
        ps="fast track promotion"
    else:
        ps="no promotion"
print("promoted status=",ps)
"""

#question =10           military recruitment fitness system


a=int(input("Age: "))
b=int(input("BMI: "))
rt=int(input("running time: "))
m=input("medical: ").lower()
if 18<a<25:
    if 18<b<25:
        if rt<=15:
            if m=="fit":
                ss="Select"
            else:
                ss="Medical reject"
        else:
            ss="Physical fail"
    else:
        ss="fail"
else:
    if 26<a<30:
        if rt<=14 and m=="fit":
            ss="conditional statement"
        else:
            ss="reject"
    else:
        ss="not eligible"
print("Selection status=",ss)



















        



























