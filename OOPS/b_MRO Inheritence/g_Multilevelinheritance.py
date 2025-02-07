"""
Purpose: Multiple and Multi-level inheritance
"""

class X:
    pass

class Y:
    pass

class Z(Y):
    pass

class M(Z,Y,X):
    pass

class N(M,Z,Y,X):
    pass

if __name__ == "__main__":
    print(N.mro())

"""
[<class '__main__.N'>, <class '__main__.M'>, <class '__main__.Z'>, <class '__main__.Y'>, <class '__main__.X'>, <class 'object'>]
"""