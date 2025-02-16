"""
Purpose: Literals
    To restrict a specific value only
    literal means constant value
"""

from dataclasses import dataclass
from typing import Literal

@dataclass
class Person:
    name : str
    Age : int
    Married : bool

print(f"{Person("Sam",45,True)}")
print(f"{Person("Joned",47,False)}")


@dataclass
class Person2:
    name: Literal["Jones","Bones"]
    Age: Literal[23,45,67]
    Married: bool

print(f"{Person2("Jones",45,True)}")
print(f"{Person2("Jones",23,False)}")
print(f"{Person2("Bones",67,False)}")