"""
Purpose:Constructor with passing arguments
"""
# Class defination
class Animal:
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(self.name  + 'walks.')

    def roars(self):
        print(self.name  + 'roars.')

# Animal()#calling class
# Animal.__init__() missing 1 required positional argument: 'name'

duck = Animal('Duck ')
print(duck)
# <__main__.Animal object at 0x71d1f846b950>

# To retrive the instance variables
print(vars(duck))
print(f"duck.name   :{duck.name}")

#calling instance method
duck.walk()

lion = Animal('Indian Lion ')
print(lion)
# <__main__.Animal object at 0x7ad01be67d40>

print(vars(lion))
print(f"lion.name  :{lion.name}")

lion.roars()