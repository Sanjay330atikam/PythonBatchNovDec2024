"""
Purpose: Classes OOPS intoduction

Classes
    1. Old sytle classes - python 2
       class type  class object
    2. New style class - python 2 & 3

"""

# function Defintion
def hello():
    pass
# function call
hello()

# Class Defination
class Emptyclass():
    pass

# Class call-Process of calling class is called instantiation
#process of creating intsance from a class
Emptyclass()

e1 = Emptyclass()
print(f"{type(Emptyclass)   =}")
print(f"{Emptyclass     =}")

print(f"{type(e1)   =}")
print(f"e1:{e1  =}")

#Emptyclass implicits inherts from object
assert issubclass(Emptyclass,object) is True

class Emptyclass(object):
    pass

#Emptyclass implicits inherts from object
assert issubclass(Emptyclass,object) is True