#print("welcome")
"""
a=int(input("enter the first no:"))
b=int(input("enter the second no:"))
c=int(input("enter the third no:"))
d=int(input("enter the fourth no:"))
if a>b:
    if a>c:
        if a>d:
            print("a is greater")
        else:
            print("d is greater")
    else:
        if c>d:
            print("c is greater")
        else:
            print("d is greater")
else:
    if b>c:
        if b>d:
            print("b is greater")
        else:
            print("d is greater")
    else:
        if c>d:
            print("c is greater")
        else:
            print("d is greater")
    
"""
"""
#print("bank loan automate system")

credit_score=int(input("enter the credit score:"))
loan_no=int(input("enter loan existing no:"))
salary=int(input("enter your salary:"))
if salary>=30000:
    if credit_score>=750:
        print("loan is approved")
    else:
        if loan_no<2:
            print(" loan is conditional approved")
        else:
            print("loan is rejected")
else:
    print("loan should be rejected")
"""
"""
#print("e- commerce website")
cart_value=int(input("enter the cart value:"))
user_type=input("enter user type=")
if cart_value>=5000:
    if user_type=="premium":
        print("final value=", cart_value-(cart_value*0.20))
    else:
        print("final value=", cart_value-(cart_value*0.0))
else:
    if cart_value<=5000:
        if cart_value>=2000:
            print("final value=", cart_value-(cart_value*0.005))
        else:
            print("no discount is applied")
"""
#print("smart electricity monitoring system")
"""
no_of_unit=int(input("enter number of unit:"))
if no_of_unit>=100:
    if no_of_unit>=300:
        print("high usage")
    else:
        if no_of_unit>=200:
            print("moderate usage")
        else:
            print("normal usage")
else:
    print("low usage")
    """
#print(gym plan)
"""
age=int(input("enter your age:"))
weight=int(input("enter your weight:"))
goal=(input("enter your goal:"))
if age>=18:
    if weight>=80:
        if goal=="weight loss":
            print("cardio plan")
        else:
            print("strength plan")
    else:
        print("general fitness plan")
else:
    print("NOT ALLOWED")
    """
#print("ATM system processes")
"""
acc_bal=int(input("enter your bank balance:"))
with_amo=int(input("enter your withdrawal amount:"))
pin_status=(input("enter your pin status:"))
if acc_bal>=with_amo:
    if with_amo<=10000:
        if pin_status=="correct":
            print("transaction successful")
        else:
            print("invalid pin")
    else:
        print("limit exceeded")
else:
    print("insufficient balance")
    """

#print("movie ticket prices calcutor")
"""
age=int(input("enter your age :"))
show_time=(input("enter your show time (morning/evenng) :"))
day_type=(input("enter your day type (weekday/weekend) :"))
if age<18:
    if show_time=="morning":
        print("Ticket price is = 100")
    else:
        print("ticket price is = 150")
else:
    if show_time=="evening":
        if day_type=="weekend":
            print("ticket price is = 300")
        else:
            print("ticket price is = 250")
    else:
        if day_type!="evening":
            print("ticket price is = 200")
            """

#print("a company emoloyee bonuses on experience")
"""
exp=int(input("enter your experience in (year):"))
rating=int(input("enter rating:"))
salary=int(input("enter your salary:"))
if exp>=5:
    if rating>=4:
        if salary<=50000:
            print("Bonus",salary*0.020)
        else:
            print("Bomus",salary*0.010)
    else:
        print("Bonus assign only 5%",salary*0.005)
else:
    print("no bonus is givem")    
    """
#print("a warehouse management system")
"""
qunit1=int(input("enter quantity of unit 1:"))
qunit2=int(input("enter quantity of unit 2:"))
qunit3=int(input("enter quantity of unit 3:"))
qunit4=int(input("enter quantity of unit 4:"))
qunit5=int(input("enter quantity of unit 5:"))
qunit6=int(input("enter quantity of unit 6:"))
if qunit1>qunit2:
    if qunit1>qunit3:
        if qunit1>qunit4:
            if qunit1>qunit5:
                if qunit1>qunit6:
                    print("highest stock", qunit1)
                else:
                    print("highest stock",qunit6)
            else:
                if qunit5>qunit6:
                    print("highest stock",qunit5)
                else:
                    print("highest stock",qunit6)
        else:
            if qunit4>qunit5:
                print("highest stock",qunit4)
            else:
                print("highest stock",qunit5)
    else:
        if qunit3>qunit4:
            print("highest stock",qunit3)
        else:
            print("highest stock",qunit4)
            """
"""
unit1=int(input("enter the quantity of unit 1:"))
unit2=int(input("enter the quantity of unit 2:"))
unit3=int(input("enter the quantity of unit 3:"))
unit4=int(input("enter the quantity of unit 4:"))
unit5=int(input("enter the quantity of unit 5:"))
unit6=int(input("enter the quantity of unit 6:"))
if unit1>unit2 and unit1>unit3 and unit1>unit4 and unit1>unit5 and unit1>unit6:
    print("highest stock=",unit1)

elif unit2>unit3 and unit2>unit4 and unit2>unit5 and unit2>unit6:
    print("highest stock", unit2)
elif unit3>unit4 and unit3>unit5 and unit3>unit6:
    print("highest stock",unit3)
elif  unit4>unit5 and unit4>unit6:
    print("highest stock",unit4)
else unit5>unit6:
 """