"""
Purpose : __Call__ method importance 
"""

class Myclass:
    def __init__(self):
        print("Constructor is called")

    def __str__(self):
        return "This is instance of Myclass"
    
    def __call__(self, *args, **kwds):
        """ Used to make things call"""
        print("This is called")
        
m =Myclass()
print(m)

print(f"callable(m):{callable(m)}")
m()