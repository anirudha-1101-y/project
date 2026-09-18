"""
ASSIGNMENT 1: Hospital Management System (Single Inheritance)
Scenario
A software company has been hired to develop a Hospital Management System. Every person associated with the hospital has some common details, but each category has its own unique information.
Create a base class Person containing:
Person ID
Name
Age
Mobile Number
Create the following derived classes:
Doctor
Specialization
Experience (Years)
Consultation Fee
Nurse
Department
Shift (Day/Night)
Salary
Patient
Disease
Ward Number
Bill Amount
Functional Requirements
Create a menu-driven application.
========== Hospital Management ==========
1. Add Doctor
2. Add Nurse
3. Add Patient
4. Display Doctor Details
5. Display Nurse Details
6. Display Patient Details
7. Exit
Sample Input
Enter Choice : 1

Enter Doctor ID : 101
Enter Name : Rahul Sharma
Enter Age : 45
Enter Mobile : 9876543210
Enter Specialization : Cardiologist
Enter Experience : 18
Enter Consultation Fee : 1500
Sample Output
Doctor Added Successfully

----------- Doctor Details -----------

Doctor ID          : 101
Name               : Rahul Sharma
Age                : 45
Mobile             : 9876543210
Specialization     : Cardiologist
Experience         : 18 Years
Consultation Fee   : ₹1500
"""
"""
class Person:
    def __init__(self,p_id,name,age,mobile):
        self.patient_id=p_id
        self.age=age
        self.name=name
        self.mobile=mobile
class Docter(Person):
    def __init__(self,p_id,name,age,mobile,spec,exp,fees):
        super().__init__(p_id,name,age,mobile)
        self.specialization=spec
        self.experience=exp
        self.fees=fees
    def display(self):
        print("----------------docter detail-------------")
        print("docter id",self.patient_id)
        print("docter name",self.name)
        print("docter age",self.age)
        print("mobile ",self.mobile)
        print("dr specialization",self.specialization)
        print("dr experiance",self.experience)
        print("dr fees",self.fees)
    
class Nurse(Person):
    def __init__(self,p_id,name,age,mobile,department,shift,salary):
        super().__init__(p_id,name,age,mobile)
        self.depatment=department
        self.shift=shift
        self.salary=salary
    def display(self):
        print("-----------Nurse detail------------")
        print("nurse id",self.patient_id)
        print("nurse name",self.name)
        print("nurse age",self.age)
        print("nurse mobile",self.mobile)
        print("nurse department",self.depatment)
        print("nurse shift",self.shift)
        print("nurse salary",self.salary)


class Patient(Person):
    def __init__(self,p_id,name,age,mobile,diesase,w_no,bill):
        super().__init__(p_id,name,age,mobile)
        self.disease=diesase
        self.wardt=w_no
        self.bill=bill
    def display(self):
        print("-----------Nurse detail------------")
        print("patient id",self.patient_id)
        print("patient name",self.name)
        print("patient age",self.age)
        print(" mobile",self.mobile)
        print("disease",self.disease)
        print("patient ward no",self.wardt)
        print("total bill",self.bill)

docter=None
nurse=None
patient=None

while True :
    print("========== Hospital Management ==========")
    print("1. Add Doctor")
    print("2. Add Nurse")
    print("3. Add Patient")
    print("4. Display Doctor Details")
    print("5. Display Nurse Details")
    print("6. Display Patient Details")
    print("7. Exit")



    ch=int(input("enter your choice"))

    match ch:
        case 1:
            print("ADD DOCTOR")
            p_id=int(input("enter doctor id: "))
            name=input("enter dr name: ")
            age=int(input("enter dr age"))
            mobile=int(input("enter mobile no"))
            spec=input("enter dr specilization: ")
            exp=int(input("enter experience (year)"))
            fees=int(input("enter dr fees"))

            docter=Docter(p_id,name,age,mobile,spec,exp,fees)
            print("dr detail saved successfully")

        case 2:
            print("ADD NURSE")
            p_id=int(input("enter doctor id: "))
            name=input("enter dr name: ")
            age=int(input("enter dr age"))
            mobile=int(input("enter mobile no"))
            department=input("enter nurse department")
            shift=input("enter shift (day/night)")
            salary=int(input("enter salary:"))


            nurse=Nurse(p_id,name,age,mobile,department,shift,salary)
            print("Nurse detail saved successfully")

        case 3:
            print("ADD  patient")
            p_id=int(input("enter doctor id: "))
            name=input("enter dr name: ")
            age=int(input("enter dr age"))
            mobile=int(input("enter mobile no"))
            disease=input("enter ptient diseASE")
            ward=int(input("enter ward number"))
            bill=int(input("enter total bill"))



            patient=Patient(p_id,name,age,mobile,disease,ward,bill)
            print("patient detail saved successfully")

        case 4:
            if docter:
                docter.display()
            else:
                print("no record found")
        case 5:
            if nurse:
                nurse.display()
            else:
                print("nurse not found")
        case 6:
            if patient:
                patient.display()
            else:
                print("patient not found ")
        case 7:
            print("exit")
            break


            """
