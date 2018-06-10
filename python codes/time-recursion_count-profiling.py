import time
from functools import wraps
import os



def time_count(skip_recursion=True):
    def wrapper(func):
        @wraps(func)
        def inner(*args,**kwargs):
            inner.a = inner.a + 1
            start = time.clock()
            r2 = func(*args,**kwargs)
            inner.a = inner.a - 1
            if(skip_recursion==True):
                if(inner.a==-1):
                    inner.t.append(time.clock() - start)
            else:
                inner.t.append(time.clock() - start)
            return r2
        inner.t = []
        inner.a = -1
        return inner
    return wrapper




def count_recur(skip_recursion=True):
    def wrapper(func):
        @wraps(func)
        def inner(*args,**kwargs):
            if (skip_recursion == False):
                inner.count[0] = inner.count[0] + 1
            else:
                if (inner.b == -1):
                    inner.count[0]=inner.count[0]+1
            inner.b=inner.b+1
            r1 = func(*args,**kwargs)
            inner.b=inner.b-1
            return r1
        inner.count = [0]
        inner.b = -1
        return inner
    return wrapper





@count_recur(skip_recursion=False)
@time_count(skip_recursion=False)
def fib(n):
    if n <= 0:
        raise ValueError("n <= 0")
    if n == 1 or n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)



print(fib(5))
print("time: "+str(fib.t))
print("count: "+str(fib.count))

"""
print(fib(2))
print(fib.t)
print(fib.count)

print("")

print(fib(3))
print(fib.t)
print(fib.count)

print("")

print(fib(4))
print(fib.t)
print(fib.count)

print("")

print(fib(5))
print(fib.t)
print(fib.count)





"""


@time_count(skip_recursion=True)
@count_recur(skip_recursion=True)
def fib2(n):
    if n <= 0:
        raise ValueError("n <= 0")
    if n == 1 or n == 2:
        return 1

    return fib2(n - 1) + fib2(n - 2)

print(fib2(5))
print("time: "+str(fib2.t))
print("count: "+str(fib2.count))
