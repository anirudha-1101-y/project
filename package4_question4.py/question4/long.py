from functools import reduce
def long(n):
    f=reduce(lambda x,y:x if len(x)>len(y) else y,n)
    return f