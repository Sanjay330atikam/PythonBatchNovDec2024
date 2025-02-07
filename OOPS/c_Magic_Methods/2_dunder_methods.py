"""
Purpose: Usage of Dunder(magic or double  under score) methods
"""
class RationalNumber:
    """
    Rational Numbers with support of arthemtic operators
    >>> a = Rational Numbers(1,2)# doc test
    >>> b = Rational Numbers(1,3)#testing for the documentation
    >>> a+b
    5/6
    """

    def __init__(self,numerator,denominator=1):
        self.n = numerator
        self.d = denominator

    def __add__(self,other):
        if not isinstance(other,RationalNumber):
            other = RationalNumber(other)
            n = self.n * other.d + self.d * other.n
            d = self.d * other.d
            return RationalNumber(n,d)
        
    def __sub__(self,other):
        if not isinstance(other,RationalNumber):
            other = RationalNumber(other)
            n = self.n * other.d - self.d * other.n
            d = self.d * other.d
            return RationalNumber(n,d)
        
    def __str__(self):
        return "%s/%s" % (self.n,self.d)
        
        __repr__ = __str__

a = RationalNumber(1, 2)
b = RationalNumber(1, 3)
c = 29

print(isinstance(a,RationalNumber))
print(isinstance(b,RationalNumber))
print(isinstance(c,RationalNumber))
print(isinstance(c,int))
print()

print(a.__add__(b))
print(a+b)

print(a.__add__(c))
print(a+c)

print(a.__sub__(b))
print(a-b)

print(a.__sub__(c))
print(a+c)

print(a.__str__())
print(str(a))

print(b.__str__())
print(str(b))