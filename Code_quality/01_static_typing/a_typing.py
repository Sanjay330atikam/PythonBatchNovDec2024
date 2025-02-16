"""
Purpose:static Typing in python
   Typing is module we are import 
   but in these. we must do
        pip install mypy

    execution : python -m mypy a_typing.py
"""

import typing

for each_attr in dir(typing):
    print(each_attr)


"""
python -m mypy a_typing.py
output
Success: no issues found in 1 source file

"""