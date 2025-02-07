"""
Purpose: functools.total_ordering
            - provide a way to  provide automatic comparssion fuctions
            - condition
            define atleast one comparssion function like
                    le, lt, gt or ge
            Defination of eq = is mandatory


Total Ordering - This will check in the background how to implent the other values

"""

import random
from functools import total_ordering

@total_ordering
class Number:
    def __init__(self,value):
        self.value = value
        
    def __lt__(self,other):
        return self.value < other.value
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __repr__(self) -> str:
        return f"{self.value}"
    
print(f"{Number(1) < Number(2)    =}")
print(f"{Number(10) > Number(20)    =}")
print(f"{Number(451) == Number(200)    =}")
print(f"{Number(1) <= Number(2)    =}")
print(f"{Number(23) >= Number(12)    =}")

values = []
for i in range(10,20):
    values.append(Number(i))

print(values)
print(sorted(values))