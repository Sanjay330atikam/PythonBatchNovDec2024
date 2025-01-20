"""
Purpose: Importing & using python script
"""

import calculator

#selective import: Multiple functions are there we are importing only one
from calculator import divison  

print(dir(calculator))

print(f"{calculator.addition(10,20) =}")
print()

print(f"{calculator.__doc__         =}")
print(f"{calculator.addition.__doc__ =}")
print(f"{divison.__doc__             =}")


help(calculator)
print()