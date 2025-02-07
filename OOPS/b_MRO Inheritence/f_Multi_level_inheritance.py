"""
Purpose: Multiple and Multi-level inheritance
"""

class A:
    def func(self): 
        print("A")
        super().func() # super means based on the MRO it will go to parent

class B(A):
    def func(self):# single - level ineritance
         print("B")
         super().func()# Super determines the current class parent and goes 

class C(A):
    def func(self): # single - level ineritance
        print("C")
        super().func()

class D(C,B):           #  Multiple ineritance
    def func(self):
        print("D")
        super().func()

class E(D,A):           #  Multiple ineritance
    def func(self):
        print("E")
        super().func()

print(D().func())

"""
D
C
B
A
Traceback (most recent call last):
  File "/workspaces/PythonBatchNovDec2024/OOPS/b_MRO Inheritence/f_Multi_level_inheritance.py", line 30, in <module>
    print(D().func())
          ^^^^^^^^^^
  File "/workspaces/PythonBatchNovDec2024/OOPS/b_MRO Inheritence/f_Multi_level_inheritance.py", line 23, in func
    super().func()
  File "/workspaces/PythonBatchNovDec2024/OOPS/b_MRO Inheritence/f_Multi_level_inheritance.py", line 18, in func
    super().func()
  File "/workspaces/PythonBatchNovDec2024/OOPS/b_MRO Inheritence/f_Multi_level_inheritance.py", line 13, in func
    super().func()
  File "/workspaces/PythonBatchNovDec2024/OOPS/b_MRO Inheritence/f_Multi_level_inheritance.py", line 8, in func
    super().func()
    ^^^^^^^^^^^^
AttributeError: 'super' object has no attribute 'func'
"""