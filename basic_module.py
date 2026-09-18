#math module used for mathmatmetical operation
"""
import math
print(math.sqrt(49))
print(math.pow(2,5))
print(math.factorial(9))
print(dir(math))

"""
#random function
import random
#print(dir(random))
"""
print(random.random())
print(random.uniform(10,20))
print(random.randrange(2,10,3))
"""
"""
a=["ani","mayank","rudra","daksh","aman"]
print(random.choice(a))
a=["ani","mayank","rudra","daksh","aman"]
print(random.choices(a,k=2))          
a=["ani","mayank","rudra","daksh","aman"]
print(random.sample(a,k=2))   #give unique value
"""
"""
c=[1,2,3,4,5]
random.shuffle(c)
print(c)
"""
"""
number=random.randint(1,5)
g=int(input("enter your no"))

if number==g:
    print("win")
else:
    print("try agin")
    """
"""
from datetime import date
today=date.today()
print(today)
print(today.day)
print(today.month)
"""
"""
from datetime import datetime
now=datetime.now()
print(now)
"""
"""
from datetime import datetime
now=datetime.now()
f=now.strftime("%y-%B-%d,%j,%w,%A")
print(f)
"""