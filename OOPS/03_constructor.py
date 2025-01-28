"""
Constructor: This is method which can be automatically called

"""

from pprint import pp

class Person(object):

    my_class_var = 111

    def __init__ (self):
        # __ on both side means it is default constructor
        #__ on both side means that word has purpose
        # only one constructor in program
        print("New instance is born! Adding default features")
        self.inst_var = 222


    def instance_method(self):
        return"This is instance method"
    
p1 = Person()
print(p1)

# Making a Call
print(Person.instance_method(p1))#indirectly
print(p1.instance_method())
assert Person.instance_method(p1) == p1.instance_method()

for each_attribute in dir(p1):
    print(each_attribute)
# p1 already has __int__ we cant give exciplity beacuse it causes code duplication we cant use __int__ of dir(p1)
print()

print(f"p1.__dict__     :{p1.__dict__}")
# p1.__dict__ means it will created dictornay for instance of p1variables
print(f"vars(p1)    :{vars(p1)}")
# assert vars(p1) == p1.__dict__
# pprint(p1.__dict__)
# pprint(vars(p1))
print()

# print("vars(Person):")
# print(vars(Person))
# print()