#question==1
"""
1. Smart Shopping Mall Discount System
A shopping mall offers discounts based on customer type and purchase amount.
If the customer is premium, they get 20% discount when the amount is more than 5000, otherwise 10%.
If the customer is regular, they get 10% discount when the amount is more than 3000, otherwise 5%.
Write a program to calculate the final payable amount using inline if only.

"""
"""
type=input("enter customer type:").lower()
a=int(input("enter the totalamount:"))

if type=="premium":
    print("20% discount" if a>=5000 else "10% discount")
else:
    print("10% discount" if a>=3000 else "5% discount")


"""

#question==2
"""
2. University Result Processing System
A university wants to automatically assign grades based on marks.
Marks ≥90 → A+
Marks ≥75 → A
Marks ≥60 → B
Marks ≥50 → C
Below 50 → Fail
Write a program using a single nested inline if expression to display the grade.
"""
"""
marks=int(input("enter the no"))
marks= "a+" if marks>=90 else "a" if marks>=75 else "b" if marks>=60 else "c" if marks>=50 else "fail" 
print(marks)
"""
"""
marks=int(input("enter the no"))
print("grade","a+" if marks>=90 else "a" if marks>=75 else "b" if marks>=60 else "c" if marks>=50 else "fail" )
"""
#question==3
"""
3. Employee Bonus Distribution System
A company provides bonuses based on years of experience.
Experience >10 years → 30% bonus
Experience >5 years → 20% bonus
Otherwise → 10% bonus
Write a program to calculate the total salary after adding bonus using inline if.

"""
"""
s=int(input("enter the salary: "))
exp=int(input("enter the exp year: "))
print("bonus", s+(s*0.3) if exp>10 else s+(s*0.2) if exp>5  else s+(s*0.1) ) 
"""



#question==4
"""
Electricity Billing System
An electricity board calculates bills based on units consumed:
Up to 100 units → ₹5 per unit
101–300 units → ₹7 per unit
Above 300 units → ₹10 per unit
Write a program to compute total bill using inline if.
"""
"""
unit=int(input("enter the total unit:"))

a= unit*5 if unit<=100 else ((unit-100)*7)+500 if 101<=unit<=300 else ((unit-300)*10)+1900
print("total amount: ",a)

"""

#question==5
"""
Calendar System – Leap Year Checker
A digital calendar system needs to check whether a year is a leap year.
A year is a leap year if:

It is divisible by 400, OR
It is divisible by 4 but not by 100
Write a program using inline if to display whether the year is a leap year or not.

"""
"""
year=int(input("enter the year: "))

y= "leap year" if year%400==0 or year%4==0 and year%100!=0 else "not leap year"
print("year is =", y)

"""

#question==6
"""
Data Validation System – Character Identifier
A system needs to validate user input characters.
If the input is:
Alphabet → display "Alphabet"
Digit → display "Digit"
Otherwise → display "Special Character"
Write a program using inline if to classify the character.
"""
"""
char=input("enter your input")
a= "Alphabet" if char is str else "Digit" if char is int else "special character"
print(a)
"""









































