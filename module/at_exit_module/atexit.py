"""
 atexit: This is function which is executed at the end of the function without callling it
 Calls function when program is clsoing down.
"""
import atexit

def hello():
    print('Hello World')

def add(n1,n2):
    print("add-function")
    return n1+n2

def alldone():
    print("alldone()")

print("Registring")
atexit.register(alldone)
print("Registered")

if __name__ == '__main__':
    hello()

    res = add(10,24)
    print(f"{res=}")
