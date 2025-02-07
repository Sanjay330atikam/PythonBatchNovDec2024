"""
Purpose : Encapsulation in OOP
    Name Mangling
        _var : protected_variable
        __var : private variable
        __var__ : built in variable
    
"""

from pprint import pprint

class Car():
    a = "public class variable"
    _a = "protected class variable"
    __a = "private class variable"

    def __init__(self):
        self.b = "public Instance variable"
        self._b = "protected Instance variable"
        self.__b = "private Instance variable"

    def instance_method(self):
        print("public Instance Method")
    
    def _instance_method(self):
        print("Protected Instance Method")

    
    def __instance_method(self):
        print("Private Instance Method")

    def new_method(self):
        """
        With in class defination class variables/methods
        can be accessed directly
        """
        print(f"self.__b ", {self.__b})
        print(f"self.instance_method",{self.instance_method})
        print(f"Car.a:",{Car.a})

if __name__ == "__main__":
    print("\n-----Class Variable------")
    print(vars(Car))#vars can be accesed at class level #means vars will acess only clas varaibles
    {
        "a " : "public class variable",
       "_a" : "protected class variable",
      "_Car__a ": "private class variable"
    }
print("Car.a",Car.a)# acessing public varaible
print("Car._a",Car._a)# acesssing protected variable
print("_Car.__a",Car._Car__a)# accesing prvate class varibale is bit different
# - first defined with Class name(_Car) and then __a(private class varaibale)

print("\n--Instance Level")
#Instantation
c=Car()
print(vars(c))
print()

print(f"\nc.b    :{c.b}")
print(f"\nc._b   :{c._b}")
print(f"\nc._Car__b    :{c._Car__b}")
print()

c.instance_method()#public
c._instance_method()#protected
c._Car__instance_method()#private varibale can be accesed by prepend Class name in protected manner and append with private varibale
print()

c.new_method()