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
print(f"c1.number           :{c1.number}") 
