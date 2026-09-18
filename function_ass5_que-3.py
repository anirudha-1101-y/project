"""
ASSIGNMENT 3: Online Shopping System (Hierarchical Inheritance)
Scenario
An e-commerce company sells multiple categories of products.
Create a base class Product.
Common Details
Product ID
Product Name
Price
Derived Classes
Electronics
Brand
Warranty
Clothing
Size
Fabric Type
Grocery
Expiry Date
Weight
Functional Requirements
========== Online Shopping ==========
1. Add Electronics Product
2. Add Clothing Product
3. Add Grocery Product
4. Display Electronics
5. Display Clothing
6. Display Grocery
7. Exit
Sample Input
Choice : 1

Product ID : 501
Product Name : Laptop
Price : 65000

Brand : Dell
Warranty : 2 Years
Sample Output
Electronics Product

Product ID : 501
Product Name : Laptop
Brand : Dell
Warranty : 2 Years
Price : ₹65000
"""
class Product:
    def __init__(self,p_id,name,price):
        self.p_id=p_id
        self.name=name
        self.price=price
class Electronics(Product):
    def __init__(self,p_id,name,price,brand,warrenty):
        super().__init__(p_id,name,price)
        self.brand=brand
        self.warrenty=warrenty
    def display(self):
        print("Product id         :",self.p_id)
        print("Product name       :",self.name)
        print("Brand              :",self.brand)
        print("Warrenty           :",self.warrenty)
        print("Product price      :",self.price)


class Clothing(Product):
    def __init__(self,p_id,name,price,size,ftype):
        super().__init__(p_id,name,price)
        self.size=size
        self.ftype=ftype
    def display(self):
        print("Product id         :",self.p_id)
        print("Product name       :",self.name)
        print("size               :",self.size)
        print("Febric type        :",self.ftype)
        print("Product price      :",self.price)



class Grocery(Product):
    def __init__(self,p_id,name,price,exp,weight):
        super().__init__(p_id,name,price)
        self.exp=exp
        self.weight=weight
    def display(self):
        print("Product id         :",self.p_id)
        print("Product name       :",self.name)
        print("Expiry date        :",self.exp)
        print("Total weight       :",self.weight)
        print("Product price      :",self.price)
electro=None
cloth=None
gro=None

while True:
    print("========== Online Shopping ==========")
    print("1. Add Electronics Product")
    print("2. Add Clothing Product")
    print("3. Add Grocery Product")
    print("4. Display Electronics")
    print("5. Display Clothing")
    print("6. Display Grocery")
    print("7. Exit")

    ch=int(input("enter your choice : "))
    match ch:
        case 1:
            id=int(input("enter product id: "))
            name=input("enter product name: ")
            price=int(input("enter price: "))
            brand=input("enter product brand :")
            warr=int(input("enter warrenty(year) :"))

            electro=Electronics(id,name,price,brand,warr)
            print("detail added successfully ...............")

        case 2:
            id=int(input("enter product id: "))
            name=input("enter product name: ")
            price=int(input("enter price: "))
            size=input("enter cloth size (l/m/s/xl/xxl):")
            ftype=input("enter febric type: ")

            cloth=Clothing(id,name,price,size,ftype)

            print("detail added successfully..........")

        case 3:
            id=int(input("enter product id: "))
            name=input("enter product name: ")
            price=int(input("enter price: "))
            exp=input("enter expiry date(dd/mm/yyyy): ")
            weight=int(input("enter total weight: "))

            gro=Grocery(id,name,price,exp,weight)

            print("detail added successfully ............")
        case 4:
            if electro:
                electro.display()
            else:
                print("not found ")
        case 5:
            if cloth:
                cloth.display()
            else:
                print("not found")
        case 6:
            if gro:
                gro.display()
            else:
                print("not found ")
        case 7:
            print("exit")
            break