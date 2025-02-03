"""
Purpose: Multiple Inheritance
    two parents
    One child
"""
from pprint import pp

class A:
    def __init__(self):
      print("A-Base Class Constructor")
      super(A,self).__init__()
      print("<A>")
      self.x = 1
      self._x = 2
      self.__x = 3

class B:
   def __init__(self):
     print("B-Class Constructor")
     super(B,self).__init__()
     print("<B>")
     self.y = 4
     self._y = 5
     self.__y = 6

class C(A,B):
   def __init__(self):
      print("C-Dervied Class Constructor")
      #A.__init__(self)
      #B.__init__(self)
      #super(C,self)__init__
      super().__init__()
      print("<C>")
      self.z = 7
      self._z = 8
      self.__z = 9

d = C()
print(vars(d))


"""
C-Dervied Class Constructor
A-Base Class Constructor
B-Class Constructor
<B>
<A>
<C>
{'y': 4, 
'_y': 5, 
'_B__y': 6, 
'x': 1, 
'_x': 2, 
'_A__x': 3,
 'z': 7, 
'_z': 8, 
'_C__z': 9}
"""