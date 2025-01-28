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