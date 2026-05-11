print("===== Movie Ticket Booking System =====")
print("----------movie selection----------")
print("1.crime & thriller")
print("2.comedy")
print("3.action")
print("4.exit")
p=500
g=300

while True:
    ch=int(input("enter your choice:"))
    match ch:
        case 1:
            print("option")
            print("1.Drishyam")
            print("2.raat akeli ")
            print("3.joseph ")
            movie=int(input("enter your movie:"))
            match movie:
                case 1:
                    print("drishyam")
                    se=input("seat= premium/gold=").lower()
                    t=int(input("enter no of ticket:"))
                    if se=="premium":
                        b=p*t
                        print("total price=",b)
                    else:
                        b=g*t
                        print("total price=",b)
                    print("your total bill =",b)
                 
           
                case 2:
                    print("raat akeli h")
                    se=input("seat= premium/gold=").lower()
                    t=int(input("enter no of ticket:"))
                    if se=="premium":
                        b=p*t

                        print("total price=",b)
                    else:
                        b=g*t
                        print("total price=",b)
                    print("your total bill =",b)
                case 3:
                    print("joseph")
                    se=input("seat= premium/gold=").lower()
                    t=int(input("enter no of ticket:"))
                    if se=="premium":
                        b=p*t
                        print("total price=",b)
                    else:
                        b=g*t
                        print("total price=",b)
                    print("your total bill =",b)
                case _:
                     print("invalid")
                     

        case 2:
            print("option")
            print("1.dragon")
            print("2.Bhoot bangla ")
            print("3.sitaare jameen par ")
            movie=int(input("enter your movie:"))
            match movie:
                case 1:
                    print("dragon")
                    se=input("seat= premium/gold=").lower()
                    t=int(input("enter no of ticket:"))
                  
                    if se=="premium":
                        b=p*t

                        print("price=",b)
                    else:
                        b=g*t
                        print("price=",b)
                    print("your total bill =",b)
                 
           
                case 2:
                    print("bhoot bangla")
                    se=input("seat= premium/gold=").lower()
                    t=int(input("enter no of ticket:"))
                    if se=="premium":
                        b=p*t
                        print("price=",b)
                    else:
                        b=g*t
                        print("price=",b)
                    print("your total bill =",b)
                case 3:
                    print("sitaare jameen par")
                    se=input("seat= premium/gold=").lower()
                    t=int(input("enter no of ticket:"))
                    if se=="premium":
                        b=p*t
                        print("price=",b)
                    else:
                        b=g*t
                        print("price=",b)
                    print("your total bill =",b)
                case _:
                     print("invalid")

        case 3:
            print("option")
            print("1.DHURANDHAR")
            print("2.KILL ")
            print("3.PATHAAN ")
            movie=int(input("enter your movie:"))
            match movie:
                case 1:
                    print("DHURANDHAR")
                    se=input("seat= premium/gold=").lower()
                    t=int(input("enter no of ticket:"))
                  
                    if se=="premium":
  
                        b=p*t
                        print("price=",b)
                    else:
                        b=g*t
                        print("price=",b)
                    print("your total bill =",b)
                 
           
                case 2:
                    print("KILL")
                    se=input("seat= premium/gold=").lower()
                    t=int(input("enter no of ticket:"))
                    if se=="premium":
                        b=p*t
                        print("price=",b)
                    else:
                        b=g*t
                        print("price=",b)
                    print("your total bill =",b)
                case 3:
                    print("PATHAAN")
                    se=input("seat= premium/gold=").lower()
                    t=int(input("enter no of ticket:"))
                    if se=="premium":
                        b=p*t
                        print("price=",b)
                    else:
                        b=g*t
                        print("price=",b)
                    print("your total bill =",b)
                case _:
                     print("invalid")
        case 4:
             print("exiting ")
        case _:
            print("invalid")
            break


