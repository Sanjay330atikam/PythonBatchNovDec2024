"""
Purpose: static typing with mypy
"""

# Method1 : Tradtional approach
def hello():
    print(f"Hello World")

hello()

# Method2 : Adding Typing
def hello1() -> None:
    print(f"Hello World")

hello1()

"""
 $ python -m mypy b_example.py
Success: no issues found in 1 source file
"""