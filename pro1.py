


total_exp=0
food=0
travel=0
study=0
other=0
budget=0
a=0
budget=int(input("enter your budget"))
print("============EXPENSE TRACKER================")
print("1 = Add expense")
print("2 = view total expense")
print("3 = view category wise expense")
print("4 = find remaining amount from budget")
print("5 = exit")

while True:
    ch=int(input("enter your choice:"))
    re=budget-total_exp
    match ch:
        case 1:
             a=int(input("enter amount:"))      #a=amount
             if a<=0:
                 print(" invalid amount please try again")
             elif re<a:
                 print("you expense limit is exceedes can't add this amount")
             
             else:

                 cat=input("enter category (food/travel/study/other):").lower()
                 total_exp=total_exp+a
                 if cat=="food":
                     food=food+a           #a=amount
                 
                 elif cat=="travel":
                     travel=travel+a
                 
                 elif cat=="study":
                     study=study+a
                 
                 else:
                     other=other+a
               

                 print("amount added successfully")
        case 2:
            print("total expense=:",total_exp)
            if budget>0:
                if total_exp>budget:
                    print("warning you exceed your budget limit")
                else:
                    print("you are within safe limit")
        case 3:
            te=food+study+travel+other
            print("----------expense---------")
            print("food",food)
            print("study",study)
            print("travel",travel)
            print("other",other)
            print("total expense:",te)
            print("------------------")
        case 4:
            print("budget",budget)
            
            if budget>=te:
                r=budget-te
                print("you do not cross budget limit")
            else:
                print("you cross your budget limit please control your self!")
         
        case 5:
            print("exiting thankyou!")
            break
        case _:
            print("invalid choice")
            break

   







             
                    
               
