class cntx_mgr:

    def __init__(self,key):
        print("Inside constructor")
        print("exit constructor")
        self.key=key
        pass

    def func(self):
        print("inside function")
        print("exit function")

    def __enter__(self):
        print("enter block")
        return self.key
        pass

    def __exit__(self,exec_type,exec_value,exec_traceback):
        print("exit block")
        print(exec_type,exec_value,exec_traceback)
        return True
        pass


def test_contextmgr():
    with cntx_mgr(1) as obj:
        print("value of obj",obj)
        raise ValueError("hello")
        print("in body of eith statement")


from contextlib import contextmanager

@contextmanager
def cntxMgr():
    print("entered context manager")
    try:
        yield 10
        return
    finally:
        print("exit called")# generaotr is resumed with that exception
        #raise StopIteration("from methid")


def cmgrtest():
    with cntxMgr() as val:
        print("enterd block with val",val)
        raise ValueError("asd")


def blah(func):
    def f(*args,**kwargs):
        print("entering function "+func.__name__+ " with args: ",args,kwargs)
        r=func(*args,**kwargs)
        print("exiting function with ",r);
        return r;
    return f

@blah
def sum(a,b):
    return a+b

if __name__=="__main__":
    #test_contextmgr()
    #cmgrtest()
    print(sum(1,2))
    print(sum(a=2,b=3))



#instead of writing a new context manager we can use context manager. yield returns what enter would return