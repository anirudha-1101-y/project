p=[]
def add():
    
    i=int(input("enter no of patient:"))
    for j in range(i):
       
        id=int(input("enter your id"))
        name=input("enter your name")
        age=int(input("enter patient age: "))
        gender=input("enter gender (male/female): ")
        disease=input("enter disease: ")
        mobile_number=int(input("enter your mobile no"))

        polo={"id":id,
              "name":name,
              "age":age,
              "gender":gender,
              "dissease":disease,
              "mobile":mobile_number}
        p.append(polo )
    print("information saved")

def display_pat():
    if len(p)==0:
        print("patient no found")
        print("pls add some detalis")
    else:
        for k in p:
            for j,i in k.items():
                print(j,"=",i)
            print()

def search():
    pid=int(input("enter your id"))
    if len(p)!=0:
     for i in p:
        if i["id"]==pid:
            print(i)
        
    else:
            print("id not found")
    
    






