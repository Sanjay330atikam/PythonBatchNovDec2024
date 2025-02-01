"""
Purpose: Understanding the class instantination
"""

#Class defination
# Class defination is a combination of vairables and functions
# functions means methods!!!---combination of variables and functions--!!!
class MyClassname:
    number = 786 #Class varibale

    def hello_world(self):#method self is argument 
        return "Hello World"

# Instantination
c1 = MyClassname()
print(f"c1:{c1  =}")
print(f"{id(c1) =}")
print(f"{dir(c1) =}")
print()

print(f"callable.number    :{callable(c1.number)}")#False beacuse number is varibale it doesnot have function call
print(f"c1.number           :{c1.number}")# accesig values directly

# you get value of any attribute by using getattr
print(f"getattr(c1,number)     :{getattr(c1,"number")}")

#checks hasattr will check whether whether particular object any kind of support 
# Hasattr will manly check whether particular attribute is present or not
print(f"hasattr(c1,number)  :{hasattr(c1,"number")}")
print(f"'number'in dir(c1)    :{'number'in dir(c1)}")

#Classe are mutuable objects
c1.number = 1000
print(f"getattr(c1,'number)     :{getattr(c1,'number')}")
print(f"{id(c1) =}")

setattr(c1,"number3",3333)
print(f"getattr(c1,number3)      :{getattr(c1,'number3')}")

c1.number4 =4444
print(f"getattr(c1,number4)      :{getattr(c1,'number4')}")
