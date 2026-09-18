d=[]
def addd():
    e=int(input("enter no of dr"))
    for i in range(e):
        did=int(input("enter dr id"))
        dname=input("entre dr name")
        spe=input("enter specialization")
        exp=int(input("enter experience"))
        cof=int(input("enter consultantant fees "))

        dic={"id":did,
            "dr_name":dname,
            "dr_specialization":spe,
            "experience":exp,
            "consultant fess":cof

        }
        d.append(dic)
        print("information saved successfully !")


def display_d():
    if len(d)!=0:
       for i in d:
           for j,k in i.items():
              print(j,"=",k)
    else:
        print("pls enter details first")
    

s=[]
def show_appointments():
    e=int(input("enter no of appintment"))
    for i in range(e):
       aid=int(input("enter id"))
       pid=int(input("enter patient id"))
       did=int(input("enter dr id"))
       appd=int(input("enter date (dd/mm/yyyy)"))
       appt=int(input("enter time"))

       sd={
        "Appointment ID":aid,
        "Patient ID":pid,
        "Doctor ID":did,
        "Appointment Date":appd,
        "Appointment time":appt

        }
       s.append(sd)
    print("Appointment booked")



def show():
    if len(s)!=0:
       for i in s:
        for k,v in i.items():
            print(k,"=",v)
    else:
       print("pls take appointment first")







