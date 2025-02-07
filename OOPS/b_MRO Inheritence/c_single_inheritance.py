"""
Purpose: Single-Inheritance Mechansim
"""

class Base():
    def __init__(self):
        self.__x = 1 # private
        self._y = 2 # proctected
        self.z   = 3 # public

    def display(self):
        print(f"{self.__x   =}{self._y  =}{self.z   =}")

b = Base()
b.display()
print(vars(b))

print("b.z",b.z)
print("b._y",b._y)
print("b._Base__x",b._Base__x)
print()

class Derived(Base):
    def __init__(self):
        # Base.__init__(self) 
        super().__init__() # supers is used to call constructor of parent class
        # super used when we have on parent class , we can call also by using class name
        self.__x = 4 # private
        self._y = 4 # proctected
        self.z   = 6 # public

c=Derived()
c.display()
print(vars(c))
# self.__x   =1self._y  =4self.z   =6
# {'_Base__x': 1, '_y': 4, 'z': 6, '_Derived__x': 4}
"""
NOTE: private values of parents class cannot be modified
        in child class 
        Ex: In above 1 value for x whixh is private is being same in child
            class although we gave 4 value for x in child class
"""