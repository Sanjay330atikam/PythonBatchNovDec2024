"""
Script to demonstarte the functionality of python code
"""
Greetings = "GoodMorning ==!!!!=="

def Hello_World():
    print("Hello -----!!!!!!")


if __name__ == "__main__": 
       Hello_World()
else:
     print(
          f"""
          {__name__ =}
          {__package__ =}
        """

       )






"""
After generating the byte code and if we made any changes in the original script
then it will regnerate in python intercative mode wile importing.

After doing the changes in myscript the chnages reflect only once the 
python intercative code is closed

And if we open again intercative mode of python for importing then we can 
see changes this is concern in interactive modes.
# This can be solved by using importlib.reload(myscript)
"""