t=[]
def bill():
    pid=int(input("enter patient id"))
    cc=int(input("enter consultant charge"))
    mc=int(input("enter medicine cost"))
    tc=int(input("enter test charge"))
    

    total=cc+mc+tc


    tax={
        "patient_id":pid,
        "consultantant charge":cc,
        "medicine charge":mc,
        "test charge":tc
    }
    t.append(tax)
    for i in t:
        for k,v in i.items():
           print(k,"-",v)


    print("TOTAL AMOUNT",total)
















