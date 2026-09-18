"""
ASSIGNMENT 2: Employee Payroll Management System (Method Overriding + Menu Driven)
Scenario
An IT company has three categories of employees.
Create a base class Employee.
Common Details
Employee ID
Name
Department
Derived Classes
FullTimeEmployee
Monthly Salary
Bonus
Salary Formula
Salary = Monthly Salary + Bonus
PartTimeEmployee
Hourly Rate
Total Hours Worked
Salary Formula
Salary = Hourly Rate × Hours
ContractEmployee
Project Name
Contract Amount
Salary Formula
Salary = Contract Amount
Functional Requirements
========== Payroll System ==========

1. Add Full Time Employee
2. Add Part Time Employee
3. Add Contract Employee
4. Display Full Time Salary
5. Display Part Time Salary
6. Display Contract Salary
7. Exit
Sample Input
Choice : 2

Employee ID : 205
Name : Aman Verma
Department : Testing

Hourly Rate : 350
Hours Worked : 160
Sample Output
Employee Added Successfully

Employee ID : 205
Name : Aman Verma
Department : Testing

Hourly Rate : 350
Hours Worked : 160

Total Salary : ₹56000
"""
class Employee:
    def __init__(self,id,name,department,):
        self.id=id
        self.name=name
        self.department=department


class FullTimeEmployee(Employee):
    def __init__(self,id,name,department,monthly_slary,bonus):
        super().__init__(id,name,department)
        self.salary=monthly_slary
        self.bonus=bonus
    def calculate(self):
        self.calculate_s=self.salary+self.bonus
    def display(self):
        print("employee id               ",self.id)
        print("employee name             ",self.name)
        print("Department                ",self.department)
        print("employee m0onthly salary  ",self.salary)
        print("employee bonus            ",self.bonus)

        print("total salary               ",self.calculate_s)


class PartTimeEmployee(Employee):
    def __init__(self, id, name, department,hour,total_h):
        super().__init__(id, name, department)
        self.hour=hour
        self.total_h=total_h
    def claculate(self):
        self.total_salary=self.hour*self.total_h
    def display(self):
        print("employee id             ",self.id)
        print("employee name           ",self.name)
        print("Department              ",self.department)
        print("hourly rate             ",self.hour)
        print("hour worked             ",self.total_h)

        print("total slaary             ",self.total_salary)


class ContractEmployee(Employee):
    def __init__(self,id,name,department,project_name,contract_amount):
        super().__init__(id,name,department)
        self.project_name=project_name
        self.contract_amount=contract_amount
    def calculate(self):
        self.total_salary=self.contract_amount
    def display(self):
        print("employee id             ",self.id)
        print("employee name           ",self.name)
        print("Department              ",self.department)
        print("project name            ",self.project_name)
        print("contract amount         ",self.contract_amount)
        print("totall salary           ",self.total_salary)


while True:
    print("========== Payroll System ==========")

    print("1. Add Full Time Employee")
    print("2. Add Part Time Employee")
    print("3. Add Contract Employee")
    print("4. Display Full Time Salary")
    print("5. Display Part Time Salary")
    print("6. Display Contract Salary")
    print("7. Exit")

    ch=int(input("enter your choice: "))
    match ch:
        case 1:
            id=int(input("enter your id: "))
            name=input("enter your name: ")
            department=input('enter your department: ')
            monthly_slary=int(input("enter monthly salary: "))
            bonus=int(input("enter your bonus: "))

            full=FullTimeEmployee(id,name,department,monthly_slary,bonus)
            print("detail added successfull....")

        case 2:
            id=int(input("enter your id: "))
            name=input("enter your name: ")
            department=input('enter your department: ')
            hour=int(input("enter no of hour: "))
            total_h=int(input("enter total hour"))
            part=PartTimeEmployee(id,name,department,hour,total_h)
            print("detail added successfull..........")

        case 3:
            id=int(input("enter your id: "))
            name=input("enter your name: ")
            department=input('enter your department: ')
            project_name=input("enter project name: ")
            contract_amount=int(input("enter contract amount: "))
            contract=ContractEmployee(id,name,department,project_name,contract_amount)

        case 4:
            if full:
                full.calculate()
                full.display()
            else:
                print("not found.....")
        case 5:
            if part:
                part.claculate()
                part.display()
            else:
                print("not found......")
        case 6:
            if contract:
                contract.calculate()
                contract.display()
            else:
                print("not found....")
        case 7:
            print("exit")
            break






        




















