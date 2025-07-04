"""Purpose: Static code Analysis using Pylint 
        pip install -U pylint

        python -m pylint script.py
     pylint returns what the errors in the code and help to solve and run it again
     to check all errors are solved or not
"""


a = 234
b = 123


c = a+b

print(c)

"""
int unformatted_0.py
************* Module unformatted_0
unformatted_0.py:20:0: C0304: Final newline missing (missing-final-newline)
unformatted_0.py:10:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
unformatted_0.py:10:9: C0321: More than one statement on a single line (multiple-statements)
unformatted_0.py:10:9: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
unformatted_0.py:15:0: C0103: Constant name "c" doesn't conform to UPPER_CASE naming style (invalid-name)

------------------------------------------------------------------
"""

