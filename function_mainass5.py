"""
Assignment: Hospital Management System Using Python Packages and Modules

Problem Statement:

Develop a menu-driven Hospital Management System application in Python.

The application should be developed using proper packages and modules. 
Do not write the complete program in a single file. Divide the application
into different packages based on functionality.

Project Structure:

HospitalManagement/

    main.py

    patient/
        _init_.py
        patient_module.py

    doctor/
        _init_.py
        doctor_module.py

    appointment/
        _init_.py
        appointment_module.py

    billing/
        _init_.py
        billing_module.py


Requirements:

1. Patient Management Package

Create a package named "patient".

Create module:
patient_module.py


Implement the following functions:

a) add_patient()

Take patient details from user:

- Patient ID
- Patient Name
- Age
- Gender
- Disease
- Mobile Number


Store patient information using list and dictionary.


b) display_patients()

Display all registered patients.


c) search_patient()

Search patient details using Patient ID.


--------------------------------------------------


2. Doctor Management Package

Create a package named "doctor".

Create module:
doctor_module.py


Implement the following functions:


a) add_doctor()ṇṇ

Take doctor details:

- Doctor ID
- Doctor Name
- Specialization
- Experience
- Consultation Fees


Store doctor information using list and dictionary.


b) display_doctors()

Display all doctor details.


--------------------------------------------------


3. Appointment Management Package

Create a package named "appointment".

Create module:
appointment_module.py


Implement:


a) book_appointment()

Take appointment details:

- Appointment ID
- Patient ID
- Doctor ID
- Appointment Date
- Appointment Time


Store appointment information.


b) show_appointments()

Display all booked appointments.


--------------------------------------------------


4. Billing Package

Create a package named "billing".

Create module:
billing_module.py


Implement:


generate_bill()


Take:

- Patient ID
- Consultation Charges
- Medicine Cost
- Test Charges


Calculate total amount:

Total Bill = Consultation Charges + Medicine Cost + Test Charges


Display complete bill.


--------------------------------------------------


5. Main Application

Create main.py file.

Create a menu-driven program.


Menu:

========== Hospital Management System ==========

1. Add Patient

2. Display Patients

3. Search Patient

4. Add Doctor

5. Display Doctors

6. Book Appointment

7. Show Appointments

8. Generate Bill

9. Exit


According to user choice call the required functions from packages.


-------------------------------------------------
"""
import hospitalmanagement
from hospitalmanagement import patient_module,docter_module,billing_module
while True:
    print("========== Hospital Management System ==========")

    print("1. Add Patient")

    print("2. Display Patients")

    print("3. Search Patient")

    print("4. Add Doctor")

    print("5. Display Doctors")

    print("6. Book Appointment")

    print("7. Show Appointments")

    print("8. Generate Bill")

    print("9. Exit")

    ch=int(input("enter your choice: "))
    match ch:
        case 1:
            print("add patient")
            patient_module.add()
        case 2:
            print(patient_module.display_pat())
        case 3:
            patient_module.search()
        case 4:
            docter_module.addd()
        case 5:
            docter_module.display_d()
        case 6: 
            print("book appointment")
            docter_module.show_appointments()
        case 7:
            docter_module.show()
        case 8:
            billing_module.bill()
        case 9:
            print("EXIT")
            break
