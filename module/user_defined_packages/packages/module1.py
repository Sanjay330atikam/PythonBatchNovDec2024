import sys

"""
sys.dont_write_bytecode = True
This will helps to dont give byte code 
This will not only effect this scripts but subsqeuent imports also

├── packages
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   └── module1.cpython-312.pyc
│   ├── module1.py
│   ├── module2.py
│   └── module3.py
└── usage_package.py

module 1 byte code is created but not for module 2 beacuse of
morder in __init__.py file module1 is first and next goes to module2
and remaining all have byte code files.!!!
"""

def Hello_World():
    print("Hello FROM Module1!-----!!!!!!")


if __name__ == "__main__": 
       Hello_World()
else:
     print(
          f"""
          {__name__ =}
          {__package__ =}
        """

       )