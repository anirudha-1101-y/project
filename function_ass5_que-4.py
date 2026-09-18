"""
ASSIGNMENT 4: Banking Loan Management System (Multilevel Inheritance)
Scenario
A bank wants software for loan management.
Class Hierarchy
Person
     ↓
Customer
     ↓
LoanAccount
Person
Name
Age
Mobile Number
Customer
Customer ID
Account Number
LoanAccount
Loan Amount
Interest Rate
Loan Tenure
Functional Requirements
Add Customer Loan Details
Display Loan Details
Exit
Sample Input
Customer Name : Ajay Singh
Age : 36
Mobile : 9999999999

Customer ID : C101
Account Number : 100245785

Loan Amount : 500000
Interest Rate : 8.5
Loan Tenure : 5
Sample Output
----------- Loan Details -----------

Customer Name : Ajay Singh
Customer ID : C101
Account Number : 100245785

Loan Amount : ₹500000
Interest Rate : 8.5%
Loan Tenure : 5 Years
"""
class Person:
    def __init__(self,name,age,mobile):
        self.name=name
        self.age=age
        self.mobile=mobile
class Customer(Person):
    def __init__(self,name,age,mobile,id,acc_no):
        super().__init__(name,age,mobile)
        self.id=id
        self.acc_no=acc_no
class LoanAccount(Customer):
    def __init__(self,name,age,mobile,id,acc_no,loan_a,interest_r,loan_time):
        super().__init__(name,age,mobile,id,acc_no)
        self.loan_a=loan_a
        self.interest_r=interest_r
        self.loan_time=loan_time

    def display(self):
        
        print("=================DETAIL==============")
        print("Customer name           :",self.name)
        print("Customer age            :",self.age)
        print("Mobile                  :",self.mobile)
        print()
        print("Customer ID             : ",self.id)
        print("Customer account number : ",self.acc_no)
        print()

        print("Customer loan amount    : ",self.loan_a)
        print("Customer interest rate  : ",self.interest_r)
        print("Customer Loan Tenure    :",self.loan_time)
print()
while True:
    print("1.Add Customer Loan Details")
    print("2.Display Loan Details")
    print("3.Exit")

    ch=int(input("enter your choice :"))

    match ch:
        case 1:
            print("ADD detail ..........")
            name=input("enter customer name :")
            age=int(input("enter customer age :"))
            mobile=int(input("enter mobile number : "))
            id=int(input("enter customer id :"))
            acc_no=int(input("enter account number :"))
            loan_a=int(input("enter loan amount"))
            interest_r=int(input("enter interst rate :"))
            loan_time=int(input("enter loan duration :"))

            loan=LoanAccount(name,age,mobile,id,acc_no,loan_a,interest_r,loan_time)
            print("detail saved successfully ..............")

        case 2:
            loan.display()
        case 3:
            print("exit")
            break
    
    
        

