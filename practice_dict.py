"""
a={1:"ani",2:"virat",3:"yadav"}
print(a.keys())
print(a.values())
print(a.items())
"""
"""
n=int(input("enter your dict"))
d={}
for i in range(n):
    k=input("enter str: ")
    v=int(input("enter value"))
    d[k]=v
print(d)
"""
"""
d={1:"ani",2:"yadav",3:"meduu"}
d[4]="virat"
print(d)
"""
"""
d={1:"a",2:"b",2:"c",4:"d"}          in this previos value will be replce
print(d) 
"""
"""
d={1:"ani",2:"yadav",3:"medu"}
print(d.pop(1))
print(d.popitem())
del d
"""
"""
d={1:"ani",2:"yadav",3:"medu"}
for k,v in d.items():
    print(k,"=",v)
"""
"""
d={i:i*i for i in range(1,11)}
print(d)
"""
"""
d={i: i*i if i%2==0 else  i*i*i for i in range(1,11)}
print(d)
"""
"""
w={"deepika","thapaji","anirudha","mayank","aman"}
d={i:len(i) for i in w}
print(d)
"""
"""
k=["name","city","age"]
v=["ani","indore",30]
d={k[i]:v[i] for i in range(len(k))}
print(d)
"""
"""
stu={
    101:{"name":"virat","age":30},
    102:{"name":"anmol","age":35}

}
stu[103]={"name":"mohan","age":25}
for k,v in stu.items():
    print("id==",k)
    for k1,v1 in v.items():
        print(k1,"==",v1)
        
"""
"""
n=int(input("enter dict"))
d={}
for i in range(n):
    k=int(input("Enter keys"))
    v=input("enter values")
    d[k]=v
print(d)
sum=sum(d.keys())
print(sum)
"""
"""
words=input("enter your words")
d={}
for x in words:
    d[x]=d.get(x,0)+1
print(d)
for k,v in d.items():
    print(k,"occure",v,"times")
    """
#vowel find
"""
words=input("enter your words: ")
v={"a","e","i","o","u"}
d={}
for i in words:
    if i in v:
        d[i]=d.get(i,0)+1
print(d)
for k,v in sorted(d.items()):
    print(k,"occure",v,"times")
"""
"""
login=["deepika","rasmika","deepika","virat","anirudha"]
d={}
for i in login:
    d[i]=d.get(i,0)+1
print("is used to try login",d)
"""
"""
words=["deepika","rashmik","virat","rudra","ani","aru"]
d={}
for i in words:
    l=len(i)
    if l not in d:
        d[l]=[]
    d[l].append(i)
print(d)
"""
