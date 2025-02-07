class Ordinary_class:
    def __init__(self):
        self.foo = None
        self.bar = None

o = Ordinary_class()
print(vars(o))

#Dynamically creating attributes
o.yyy = 12345 # attributes can be added to instance
setattr(o,"yy",1234)
print(vars(o))
print()

class Slotted_class:
    """
    When slot is present it will not allow you to create dynamic attributes
    """
    __slots__ = {"foo","bar"}

    def __init__(self):
        self.foo = None
        self.bar = None
        # You cannot access any attributes outside the class

c = Slotted_class
# print(vars(c))

# updating the existing values are possible
print(f"c.foo = {c.foo}")
c.foo = 123
print(f"c.foo = {c.foo}")

# we can't create new attribute