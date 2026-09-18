"""
1.

Handling Book Invalid Quantity Exception in Library Software

Mohan, a librarian is creating software to automate his work. As part of this, he needs to handle the exception if the purchased quantity is greater than the available quantity.
Create a class named "Book" with the following attributes
1. id - String
2. bookTitle - String
3. authorName - String
4. price - float
5. quantity - int
Create an Exception class called InvalidQuantityException and use it in the class called “Book”. Include a method called purchase(int quantity) taking the purchased quantity as a parameter and update the quantity available appropriately. Print suitable exception if the purchased quantity is more than the available quantity. Help Mohan to complete this task. Refer to sample input and output.
Input format :
The first line of the input consists of bookID as a String
The second line of the input consists of bookTitle as String
The third line of the input consists of authorName as String
The fourth line of the input consists of price as a float
The fifth line of the input consists of the quantity available as an integer
The sixth line of the input consists of the quantity purchased as an positive integer
Output format :
The output should display the quantity available if it has or else throws an exception
Refer to the sample output for reference.
Sample test cases :
Input 1 :
YCW2019
You can win
Shiv Khera
245
25
20
Output 1 :
Quantity Available : 5
Input 2 :
YCW2019
You can win
Shiv Khera
245
25
30
Output 2 :
InvalidQuantityException: Quantity not available
"""
#=====================================================
"""
class InvalidQuantityException(Exception):
    pass

class Book:
    def __init__(self,id,booktitle,authorname,price,quantity):
        self.id=id
        self.booktitle=booktitle
        self.authorname=authorname
        self.price=price
        self.quantity=quantity

    def purchase(self,quantity):
        if self.quantity<quantity:
            raise InvalidQuantityException("quantity not available")
        print(self.quantity)

id=int(input("enter bookid :"))
bk=input("enter book title: ")
an=input("enter author name: ")
price=int(input("enter price: "))
q=int(input("enter quantity: "))
try:
    b=Book(id,bk,an,price,q)
    qua=int(input("enter purcase quantity"))
    b.purchase(qua)

except InvalidQuantityException as e:
    print("invalid quantity ",e)
finally:
    print("done")
    """
"""
2.

Validating Email Address and Handling Custom Exceptions

Write a program to validate an email address and display appropriate exceptions if any errors are encountered.
Create 3 custom exception classes as below
1. DotException
2. AtTheRateException
3. DomainException
A typical email address should include a '.' character, '@' character, and a valid domain name. Valid domain names for practice include 'in', 'com', 'net', or 'biz'.
Input format :
The first line of input contains the email to be validated.
Output format :
Print 'Valid email address' if the email address provided meets the criteria, or 'Invalid email address' along with the appropriate exception message. Display 'Invalid Dot usage', 'Invalid @ usage', or 'Invalid Domain' messages based on the email ID provided.
Refer to the sample output for reference.
Sample test cases :
Input 1 :
sample@gmail.com
Output 1 :
Valid email address
Input 2 :
sample@gmail.com.
Output 2 :
DotException: Invalid Dot usage
Invalid email address
Input 3 :
sample@g@mail.com
Output 3 :
AtTheRateException: Invalid @ usage
Invalid email address
Input 4 :
sample@gmail.con
Output 4 :
DomainException: Invalid Domain
Invalid email address
"""
#==========================================
"""
class  DotException(Exception):
    pass
class AtTheRateException(Exception):
    pass
class  DomainException(Exception):
    pass

def Main(email):
    if email.count(".")!=1 or email.endswith("."):
        raise  DotException("invalid dot usage")
    if  email.count("@")!=1:
        raise AtTheRateException("invalid @ usage")
    if  not  email.endswith(('in', 'com', 'net','biz')):
        raise DomainException("invalid domain ")

email=input("enter your email")
try:
    Main(email)
except AtTheRateException as e:
    print("Error ",e)
except DotException as e:
    print("Error",e)
except DomainException as e:
    print("Error",e)

else:
    print("approve")
finally:
    print("done")

"""
"""

3.

Handling Driving License Registration Exceptions

Write a program to approve or display suitable exceptions whenever a person tries to register for a driving license.
Create a class named Main with the following attributes
1. name - String
2. userAge - int
3. mark - int
Minimum eligibility for obtaining a driving license:
1. Age should be above 18 years old.
2. A person should pass the road rules eligibility test (with above 80 marks) for a total mark of 100.
Create two exceptions InvalidAgeForDrivingLicenseException and InvalidMarkForDrivingLicenseException to handle the above scenarios.
Input format :
The first line consists of a name a String.
The second line consists of age as an integer.
The next line consists of marks obtained as integers.
Output format :
The output should display "Approved" if he meets the criteria or the appropriate exception.
Refer to the sample output for reference.
Sample test cases :
Input 1 :
Guru
33
95
Output 1 :
Approved
Input 2 :
Smith
2
95
Output 2 :
InvalidAgeForDrivingLicenseException: Age should be more than 18 years old
Input 3 :
Jack
-3
95
Output 3 :
InvalidAgeForDrivingLicenseException: Invalid age
Input 4 :
Scott
33
75
Output 4 :
InvalidMarkForDrivingLicenseException: Mark should be more than 80
Input 5 :
Mathew
33
-45
Output 5 :
InvalidMarkForDrivingLicenseException: Invalid mark
Input 6 :
Guru
33
195
Output 6 :
InvalidMarkForDrivingLicenseException: Invalid mark
"""
"""

class InvalidAgeForDrivingLicenseException(Exception):
    pass
class InvalidMarkForDrivingLicenseException(Exception):
    pass

class Main:
    def __init__(self,name,age,marks):
        self.marks=marks
        self.age=age
        self.name=name
    def eligibility(self):
        if self.age<0 or self.age>100:
            raise InvalidAgeForDrivingLicenseException("invalid age")
        if self.marks<0 or self.marks>100:
            raise  InvalidMarkForDrivingLicenseException("invalid marks")
        if 0<=self.marks<80:
            raise InvalidMarkForDrivingLicenseException("Marks should be more than 80")
        if 0<=self.age<=18:
            raise InvalidAgeForDrivingLicenseException("Age should be more than 18")
        print("Approved")
name=input("enter your name")
age=int(input("enter your age"))
marks=int(input("enter your marks"))
try:
    main=Main(name,age,marks)
    main.eligibility()
except InvalidMarkForDrivingLicenseException as e:
    print("InvalidMarkForDrivingLicenseException : ",e)
except InvalidAgeForDrivingLicenseException as e:
    print("InvalidAgeForDrivingLicenseException : ",e)
finally:
    print("Thankyou!")
    """
"""
QNo 4:
1. Bank Account Management
Objective: Create a program to manage bank accounts and handle exceptions for insufficient balance and negative deposit amounts.

Details:
Create a BankAccount class with fields for accountNumber, accountHolder, and balance.
Define two custom exceptions:
InsufficientBalanceException for withdrawal amounts exceeding the balance.
NegativeDepositException for deposits with negative amounts.
Include methods for deposit(double amount) and withdraw(double amount) that throw the respective exceptions.
In the main method, demonstrate various cases like successful transactions, insufficient balance, and invalid deposits.    
"""
#=========================
"""
class InsufficientBalanceException(Exception):
    pass
class NegativeDepositException(Exception):
    pass
class  BankAccount:
    def __init__(self,acc_no,acc_ho,bal):
        self.accno=acc_no
        self.acc_ho=acc_ho
        self.bal=bal
    def deposite(self,amount):
        if amount<0:
            raise NegativeDepositException("deposite mount can not be negative")
        self.bal=self.bal+amount
        print("deposite successfully.........")
        print("current balance :",self.bal)
    def withdraw(self,amount):
        if amount>self.bal:
            raise InsufficientBalanceException("Insufficient balance")
        self.bal=self.bal-amount
        print("withdraw successfully........")
        print("current balance :",self.bal)

acc_no=int(input("enter account no: "))
acc_ho=input("enter account holdername")
bal=int(input("enter balance : "))
bank=BankAccount(acc_no,acc_ho,bal)

try :
    amount=int(input("enter amount: "))
    bank.deposite(amount)
except  NegativeDepositException as e:
    print(" NegativeDepositException :",e)

try :
    amount=int(input("enter amount: "))
    bank.withdraw(amount)
except InsufficientBalanceException  as e:
    print(" NegativeDepositException :",e)

finally:
    print("thankyou ")
    """
"""

Question 3

Write a Python program that asks the user to enter:

Name
Age
Marks

Handle these exceptions:

ValueError → if age or marks are not valid numbers.
ZeroDivisionError → calculate the percentage using total marks 0 to demonstrate the exception.
Use try-except-else-finally.
If everything is valid, display the student's name, age, and percentage.
Code
"""
