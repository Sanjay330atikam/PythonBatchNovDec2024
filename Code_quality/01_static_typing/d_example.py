"""
Purpose: static typing with mypy
"""

# Method1 : Tradtional approach
def hello(name):
    print(f"Hello{name}")

result = hello("Python")
print(result)

# Method2 : Adding Typing
def hello1(name: str) -> None:
    print(f"Hello{name}")

result = hello("Python")
print(result)

"""
 $ python -m mypy d_example.py
Success: no issues found in 1 source file
"""