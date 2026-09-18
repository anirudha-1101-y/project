"""
Assignment 1: Shape Area Calculation

Create a parent class Shape with a method calculateArea() that prints "Area calculation not defined for Shape."

Create subclasses:

Circle that overrides calculateArea() to calculate and print the area of a circle.

Rectangle that overrides calculateArea() to calculate and print the area of a rectangle.

Write a Main class to demonstrate polymorphism using an array of Shape objects.
"""
"""
class Shape:
    def calculateArea(self):
        print("Area calculation not defined for Shape.")
class Circle(Shape):
    def __init__(self,r):
        self.area=3.14*r**2
    def calculateArea(self):
        print("Area of Circle =",self.area)
class Rectangle(Shape):
    def __init__(self,l,b):
        self.area=l*b
    def calculateArea(self):
        print("Area of Rectangle =",self.area)

shapes=[Circle(4),Rectangle(4,5)]
for shape in shapes:
    shape.calculateArea()

"""
"""
2.

Create a parent class Animal with a method makeSound() that prints "Some generic sound."

Create subclasses:

Dog that overrides makeSound() to print "Woof Woof."

Cat that overrides makeSound() to print "Meow Meow."

In the Main class, use polymorphism to call makeSound() on different Animal objects.

"""
"""
class Animal:
    def makesound(self):
        print("Some generic sound.")
class Dog(Animal):
    def makesound(self):
        print("Woof Woof")
class Cat(Animal):
    def makesound(self):
        print("Meow Meow")

sounds=[Animal(),Dog(),Cat()]
for sound in sounds:
    sound.makesound
"""
"""
Assignment 3.

Create a parent class Bank with a method getInterestRate() that returns 0.

Create subclasses:

SBI that overrides getInterestRate() to return 5.

ICICI that overrides getInterestRate() to return 6.

Axis that overrides getInterestRate() to return 7.

In the Main class, demonstrate method overriding by calling getInterestRate() on different bank objects.
"""
"""
class Bank:
    def getInterestRate(self):
        return 0
class SBI(Bank):
    def getInterestRate(self):
        return 5
class ICICI(Bank):
    def getInterestRate(self):
        return 6
class Axis(Bank):
    def getInterestRate(self):
        return 7

interests=[Bank(),SBI(),ICICI(),Axis()]

for i in interests:
    print(type(i).__name__,i.getInterestRate())
"""
"""
Assignment 4:

Create a parent class Vehicle with a method speed() that prints "Speed varies for different vehicles."

Create subclasses:

Car that overrides speed() to print "The car speed is 120 km/h."

Bike that overrides speed() to print "The bike speed is 80 km/h."

Use polymorphism to display the speed of different vehicles in the Main class.
"""
"""
class Vehicle:
    def speed(self):
        print("Speed varies for different vehicles.")
class Car(Vehicle):
    def speed(self):
        print("The car speed is 120 km/h.")
class Bike(Vehicle):
    def speed(self):
        print("The bike speed is 80 km/h.")

vehicles=[Vehicle(),Car(),Bike()]

for vehicle in vehicles:
    vehicle.speed()
"""
"""
Assignment 5:

Create a parent class Employee with a method calculateSalary() that prints "Base salary calculation for Employee."

Create subclasses:

Manager that overrides calculateSalary() to add a bonus to the base salary.

Developer that overrides calculateSalary() to calculate salary based on hours worked.

Demonstrate the overridden method in the Main class by creating an array of Employee objects and
 calling calculateSalary() on each.
"""
"""
class Employee:
    def calculateSalary(self):
        print("Base salary calculation for Employee.")

class Manager(Employee):
    def __init__(self, salary, bonus):
        self.salary = salary
        self.bonus = bonus

    def calculateSalary(self):
        print("Manager Salary =", self.salary + self.bonus)

class Developer(Employee):
    def __init__(self, rate, hours):
        self.rate = rate
        self.hours = hours

    def calculateSalary(self):
        print("Developer Salary =", self.rate * self.hours)

employees = [Employee(),Manager(50000, 10000),Developer(500, 160)]
for emp in employees:
    emp.calculateSalary()
"""
"""
1.
Problem Statement

Teena's retail store has implemented a Loyalty Points System to reward customers based on their spending. The program includes 
two classes:
 Customer and PremiumCustomer.

For regular customers: Loyalty points = amount spent / 10
For premium customers: Loyalty points = 2 * (amount spent / 10)
Calculate and display the loyal points received by the customers using an overridden method calculateLoyaltyPoints.

Input format :

The first line of input consists of an integer representing the amount spent by the customer.

The second line consists of premium customer status (a string) - "yes" if the customer is a premium customer, "no" if they are not.

Output format :

The output displays the loyalty points earned based on the amount spent.


Refer to the sample output for formatting specifications.
Code constraints :

1 ≤ amount ≤ 10,000
Sample test cases :

Input 1 :
50
yes
Output 1 :
10

Input 2 :
40
no
Output 2 :
4
"""
"""
class Customer:
    def __init__(self, amount):
        self.amount = amount

    def calculateLoyaltyPoints(self):
        return self.amount // 10


class PremiumCustomer(Customer):
    def calculateLoyaltyPoints(self):
        return 2 * (self.amount // 10)


amount = int(input())
customer_t = input().lower()

if customer_t == "yes":
    c = PremiumCustomer(amount)
else:
    c = Customer(amount)

print(c.calculateLoyaltyPoints())
"""
"""

2.

Problem Statement


Rithish is developing a straightforward pizza ordering system. To achieve this, he needs a Pizza class with a constructor for the base price and topping cost, along 
with a calculatePrice method overriding. He also wants a DiscountedPizza class that inherits from Pizza, applying a 10% discount for more than three toppings.
The program prompts the user for inputs, creates instances of both classes, calculates regular and discounted prices, and displays them formatted appropriately.
Example 1
Input:
9.5
1.25
3
Output: 

Price without discount: Rs.13.25

Price with discount: Rs.13.25

Explanation:

Rithish orders a pizza with a base price of Rs. 9.5, a topping cost of Rs. 1.25, and selects 3 toppings. The price is calculated as 9.5 + (1.25 * 3) = 13.25. The regular and discounted prices are both Rs. 13.25, as no discount has been applied.

Example 2


Input:

11.0

2.0

7

Output: 

Price without discount: Rs.25.00

Price with discount: Rs.22.50

Explanation:

Rithish orders another pizza with a higher base price of Rs. 11.0, a topping cost of Rs. 2.0, and chooses 7 toppings. 

Regular Price: 11.0 + (2.0 * 7) = Rs. 25.00.

Discounted Price: The discounted price is calculated as 90% of the regular price, i.e., 0.9 * 25.00 = Rs.22.50. 

Input format :

The first line of input consists of a double value, representing the base price of the pizza.

The second line consists of a double value, representing the cost per topping.

The third line consists of an integer, representing the number of toppings chosen for the pizza.

Output format :

The first line of output prints the price without discount, rounded off to two decimal places.

The second line prints the price with the discount, rounded off to two decimal places.


Refer to the sample output for formatting specifications.

Code constraints :

The base price and the cost per topping should be greater than zero.

1 ≤ number of toppings ≤ 10

Sample test cases :

Input 1 :

9.5

1.25

3

Output 1 :

Price without discount: Rs.13.25

Price with discount: Rs.13.25

Input 2 :

11.0

2.0

7

Output 2 :

Price without discount: Rs.25.00

Price with discount: Rs.2
"""
"""
class Pizza:
    def __init__(self, base_p, top_c, quantity):
        self.baseprice = base_p
        self.toppingcost = top_c
        self.quantity = quantity

    def calculatePrice(self):
        return self.baseprice + (self.toppingcost * self.quantity)


class DiscountedPizza(Pizza):
    def calculatePrice(self):
        price = super().calculatePrice()

        print(f"Price without discount: Rs.{price:.2f}")

        if self.quantity > 3:
            price *= 0.90

        print(f"Price with discount: Rs.{price:.2f}")


bp = float(input())
top = float(input())
q = int(input())

pizza = DiscountedPizza(bp, top, q)
pizza.calculatePrice()
"""
"""
3.
Ravi's fitness club has introduced a Rewards System to motivate members based on 
their workout hours. The program includes two classes: Member and PremiumMember.

For regular members:

Rewards Points = hours worked out × 2
For premium members:

Rewards Points = hours worked out × 4

Calculate and display the rewards points earned by the members using an overridden method calculateRewardsPoints.
Input format:
The first line of input consists of an integer representing the total hours worked out by the member.

The second line consists of premium member status (a string) - "yes" if the member is a premium member, "no" if they are not.
Output format:
The output displays the rewards points earned based on the hours worked out.
Code constraints:

1 ≤ hours ≤ 100

5  
yes
output
20
"""
"""
class Member:
    def __init__(self, working_h):
        self.w_hour = working_h

    def calculateRewardsPoints(self):
        return self.w_hour * 2


class PremiumMember(Member):
    def calculateRewardsPoints(self):
        return self.w_hour * 4


working_hour = int(input())
customer_type = input().lower()

if customer_type == "yes":
    member = PremiumMember(working_hour)
else:
    member = Member(working_hour)

print(member.calculateRewardsPoints())

"""
