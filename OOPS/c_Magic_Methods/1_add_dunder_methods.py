"""
Purpose: Dunder(double under score methods)
"""

num1 = 100
print(num1 + 22)
print(num1.__add__(22))
assert num1 + 22 == num1.__add__(22)
print()

class Person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    def __add__(self,other):
        return Person(self.name,other.surname)
    
    def __str__(self):
        return " ".join((self.name, self.surname)).title()
    
father = Person("fathername","fathersurname")
print(father)

mother = Person("Mothername","Mothersurname")
print()

print(father.__add__(mother))
print(father+mother)