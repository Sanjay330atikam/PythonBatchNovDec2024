"""
Purpose: Calcultor application
 To create documentation for this script
 python -m pydoc -w calculator
"""

DOZEN = 12

def addition(n1,n2):
    """ 
       This function will add two arguments and returns 
         : para num1:
         : para num2:
         : return:
    """
    return n1+n2


def subtarction(n1,n2):
    """
    This function does subtraction opeartion for 
     n1,n2 values

    """
    return n1-n2


def multiplication(m1,m2):
    return m1*m2


def divison(d1,d2):
    return d1/d2


print(f"{__file__   =}")

if __name__ == "__main__":
 print("This scrit is executed directly")
 print(f"{addition(100,200)  =}")
 print(f"{subtarction(100,200)   =}")
 print(f"{multiplication(100,200)    =}")
 print(f"{divison(100,200)   =}")

else:
   print("This script is executed indirectly")
   print(f"{__name__    =}")