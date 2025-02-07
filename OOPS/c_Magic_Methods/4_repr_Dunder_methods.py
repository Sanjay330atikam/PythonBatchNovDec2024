""" Purpose: __repr__ method
"""

class TheProblem:
    def __init__(self,items):
        self.items = list(items)
    
    def __repr__(self):
        items = self.items
        return f"{items}"
    
    # def __str__(self):
    #     return "str is called"
    
    # __str__ == __repr__

p1 = TheProblem(range(50))
print(p1)
print()


import reprlib

class Solution:
    def __init__(self,items):
        self.items = list(items)
    
    def __repr__(self):
        items = reprlib.repr(self.items)
        return f"{items}"
    
p2 = Solution(range(50))
print(p2)
    

