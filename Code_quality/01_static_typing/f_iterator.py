"""
Purpose: static typing with mypy
"""
from typing import Iterator

# Using Dynamic Typing
def fib(n):
    a,b = 0, 1
    while a<n:
     yield a
     a, b =b, a+b 

# static Typing
def fib1(n: int) -> Iterator[int]:
   a,b = 0, 1
   while a<n:
     yield a
     a, b =b, a+b 

if __name__ == "__main__":
   print(list(fib(10)))
   print(list(fib1(10)))

"""
 $ python -m mypy f_iterator.py
Success: no issues found in 1 source file
"""