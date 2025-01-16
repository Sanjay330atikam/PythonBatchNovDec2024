import sys
# sys.dont_write_bytecode=false
# Helps to stop the creation of python byte code


import os

print(os.listdir())

import myscript
print(dir(myscript))
# The underscores which are inside "" is meatadata
print(f"""
    {myscript.Greetings}
    {myscript.__doc__ =}
    {myscript.__name__ =}
    {myscript.Hello_World =}
    {myscript.Hello_World.__doc__ =}
    """
)
print(callable(myscript.Hello_World))
myscript.Hello_World()