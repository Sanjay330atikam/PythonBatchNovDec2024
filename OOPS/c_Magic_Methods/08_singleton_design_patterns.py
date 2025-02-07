"""
Purpose: Single Ton 
            If a class has one instance it should use the existing instance
            rathering the creating the new instance.
            At the same time if the instance is not there it will create one.
"""
class Singleton(Exception):# taking an exception to rasie an exception if its asked.
    __single__ = None # 1st time  assigning

    def __init__(self):
        if Singleton.__single__:  
            raise Singleton.__single__ # 2nd time is called rasing an exception
        Singleton.__singl__e=self

S = Singleton()
print(S)

try:
    d = Singleton()
except Exception as ex:
    print(ex)

# __new__(): baby_born     It is dealing with the creating of new instance # use onnly if needed
# __init__(): baby_named

class logger():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_logger"):
            cls._logger = super(logger,cls).__new__(cls, *args, **kwargs)
        return cls._logger
        
l1 = logger()
print(f"l1:{l1}")
print(vars(l1))

l2 = logger()
print(id(l1),id(l2))
assert l1 is l2