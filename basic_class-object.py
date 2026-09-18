"""
class Student:         #claas form
    def set(self):                 #member function
        self.id=101
        self.name="ani"
        self.add="indore"
    def display(self):             #memeber function
        print("name is",self.name)
        print("id is ",self.id)
        print("add is ",self.add)
s1=Student()                      #object called class 
s1.set()
s1.display()
"""
"""
class Student:
    def set(self,a,n,add):
        print("set is called")
        self.id=a
        self.name=n
        self.add=add
    def display(self):             #memeber function
        print("name is",self.name)
        print("id is ",self.id)
        print("add is ",self.add)

    
s1=Student()                      
s1.set(101,"ani","sendhwa")
s1.display()
"""
"""
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is",self.name,"age is",self.age)
s1=Student("ani",25)
s1.display()
"""
"""
class Add():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        self.c=self.a+self.b
    def display(self):
        return self.c
a1=Add(10,20)
a1.add()
print(a1.display())
"""
"""
class Add():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.c=self.a+self.b
    
       
    def display(self):
        
        return self.c
a1=Add(10,20)

print(a1.display())
"""
"""
class Student():
    def __init__(self,a,b,c):
        self.id=a
        self.name=b
        self.add=c
    def display(self):
        print("name is",self.name)
        print("id is ",self.id)
        print("add is ",self.add)
s1=Student(101,"deepika","indore")
s1.display()
"""
"""
import re
text="python is easy "
res=re.match(r"python",text)
print(res.group())
"""
"""
class Student:
    def __init__(self,id,name,marks):
        self.__id=id
        self.__name=name
        self.__marks=marks
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name=name

    @property
    def marks(self):
        return self.__marks
    
    @marks.setter
    def marks(self,marks):
        self.__marks=marks

    @name.deleter
    def name(self):
        del self.__name

    
    @marks.deleter
    def marks(self):
        del self.__marks

s=Student(101,"ani",89)
print(s.id)
print(s.name)
print(s.marks)
print()
print(s.id)
s.name="mayank"
s.marks=99
print(s.name)
print(s.marks)
del s.marks
print(s.name)
print(s.marks)        #delete marks 
"""
