"""
Purpose: static typing with mypy
"""

# Method1 : Tradtional approach
# empty data type given
def mirror(name):
    return str(name)

print(mirror(100))
print(mirror(123.45))
print(mirror(True))
print(mirror(None))

# Method2 : Adding Typing
# facilaiting Any data types
from typing import Any
def mirror2(name : Any) -> str:
    return str(name)

print(mirror2(100))
print(mirror2(123.45))
print(mirror2(True))
print(mirror2(None))

"""
 $ python -m mypy e_example.py
Success: no issues found in 1 source file
"""