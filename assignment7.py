#print("electricity department bill")
"""
unit=int(input("enter your total unit:"))
if unit<=100:
    bill=unit*5
elif 100<unit<=200:
    bill=unit*7
else:
    bill=unit*10
print("the bill is",bill)
"""
#college result processing
"""
marks=int(input("enter your marks:"))
if marks>=90:
    print("Grade A")
elif 75<marks<90:
    print("Grade B") 
elif 60<marks<74:
    print("Grade C") 
elif 50<marks<59:
    print("Grade D")
else:
    print("FAIL")
    """
#income tax department
"""
i=int(input("enter your income"))
if i<=250000:
    print("NO tax")
elif 250000<i<500000:
    print("tax",i*0.05)
elif 500001<i<1000000:
    print("tax",i*0.2)
elif i>1000000:
    print("tax",i*0.3)

"""
#e commerce discount engine
"""
a=int(input("enter your total amount"))
if a<2000:
    d=a-(a*0.05)
elif 2000<a<5000:
    d=a-(a*0.10)
else:
    d=a-(a*0.20)
print("final amount:",d)

      """
#cinema hall
"""
age=int(input("enter your age:"))
if age<12:
    p="RS =100"
elif 12<age<60:
    p="RS =200"
else:
    p="RS =150"
print("TICKET PRICE:",p)
"""
#company bonus distribution
"""
sa=int(input("enter your salary:"))
exp=int(input("enter your experience"))
if exp>10:
    b=sa*0.2
elif 5<exp<10:
    b=sa*0.10
elif 2<exp<5:
    b=sa*0.05
else:
    b="no bonus"
print("bomus amount=",b)
"""
#banking withdrawal limit system
"""
bal=int(input("enter your bank balance:"))
if bal<1000:
    l="Withdrawal not allowed"
elif 1000<bal<5000:
    l="maximum withdrawal limit RS1000"
else:
    l="maximum withdrawal limit RS 5000"
print(l)
"""
#weather monitoring system
"""
temp=int(input("enter temperature (in celcius):"))
if temp<0:
    print("freezing")
elif 0<temp<20:
    print("cold")
elif 21<temp<35:
    print("warm")
else:
    print("hot")
    """
#student attendance eligibility system
"""
att=int(input("enter your attendance percentage(%) :"))
if att>75:
    a="Eligible"
elif 60<att<74:
    a="Eligible with warning"
else:
    a="Not eligble"
print("status=",a)
"""
#mobile data plan advisor
"""
du=float(input("enter your data usage(per/day)"))
if du>3:
    print("premium plan")
elif 1<du<3:
    print("standard plan")
else:
    print("basic plan")
"""
#railway ticket fare system         DOUBT
"""
dis=int(input("enter distance (km):"))
cla=input("enter class (sleeper/AC):")
if dis<=100 and cla="AC":
    print("total fare= AC-1000")
elif 101<dis<500:
    print("Sleeper-300 , AC-600")
else:
    print("Sleeper-100 , AC-200")
    """
#restaurant bill with gst
"""
bill=int(input("enter your bill amount:"))
#tax=int(input("enter your tax(GST)"))

if bill<=1000:
    a=bill+(bill*0.05)
elif 1001<bill<2999:
    a=bill+(bill*0.12)
elif 3000<bill<5000:
    a=bill+(bill*0.18)+200
else: 
    a=bill+(bill*0.18)+200
print("Finale bill amount :",a)
"""
#employee performance appraisal system
"""
rt=int(input("enter rating:"))
s=int(input("enter your salary:"))
if s<20000:
    if rt==5:
        print(s+(s*0.25)+2000)
    elif rt==4:
        print(s+(s*0.20)+2000)
    elif rt==3:
        print(s+(s*0.10))
    elif rt==2:
        print(s+(s*0.05))
    elif rt==1:
        print("no hike")
    
else:
    if rt==5:
        print(s+(s*0.25))
    elif rt==4:
        print(s+(s*0.20)) 
    elif rt==3:
        print(s+(s*0.10))
    elif rt==2:
        print(s+(s*0.05))   
    else:
        print("no hike")
"""

# online course fee system
"""
Programming = 5000
Design = 4000
Marketing = 3000

course = input("Enter course category: ")
user = input("Enter user type: ")

if course == "Programming":
    if user=="Student":
        print(f"Final Course Fee: ₹{int(Programming*80/100)}")
    elif user=="Working":
        print(f"Final Course Fee: ₹{int(Programming*90/100)}")
    else:
        print(f"Final Course Fee: ₹{Programming}")

elif course == "Design":
    if user=="Student":
        print(f"Final Course Fee: ₹{int(Design*80/100)}")
    elif user=="Working":
        print(f"Final Course Fee: ₹{int(Design*90/100)}")
    else:
        print(f"Final Course Fee: ₹{Design}")

elif course == "Marketing":
    if user=="Student":
        print(f"Final Course Fee: ₹{int(Marketing*80/100)}")
    elif user=="Working":
        print(f"Final Course Fee: ₹{int(Marketing*90/100)}")
    else:
        print(f"Final Course Fee: ₹{Marketing}")
        """
#smart parking system
"""
b=10
c=20
bu=50
v=input("enter vehicle tpe: ")
h=int(input("enter hours parked: "))
if v=="c":
    if h<=5:
        print(20*h)
    else:
        print((20*h)+100)
elif v=="b":
    if h<=5:
        print(10*h)
    else:
        print((10*h)+100)
else:
    if h<=5:
        print(50*h)
    else:
        print((50*h)+100)
        """