"""
Purpose: Composition
         In Composition we dont inherit from the base class 
         but establish the relationship between classes through the
         use of instance variables that are reference to other objects

        Compensation is used as an alternative to inheritnce
"""

class Rocket:
    def __init__(self,name,distance):
        self.name = name
        self.distance = distance

    def launch(self):
        return("%s has reached %s" % (self.name, self.distance))

# Instanation    
# R=Rocket('mangalyan',15999)
# print(vars(R))

class MarsRoverComp:
    def __init__(self,name,distance,maker):
        self.rocket = Rocket(name,distance)# Instead of inheritance 
        """
        Making an explict call of the instance variables
        that we need from parent and assugning
        instead of calling whole constructor.
        """
        self.maker = maker
    
    def get_maker(self):
        return("%s launched by %s" % (self.rocket.name, self.maker))

if __name__ == "__main__":
    print(MarsRoverComp.__mro__)

    m = MarsRoverComp("Mangalyan","TillMoon","ISRO")
    print(m.rocket)
    print(dir(m.rocket))
    print(f"rocket distance :{m.rocket.distance}")
    print(f"rocket name     :{m.rocket.name}")
    print(m.rocket.launch())

    print(f"m.get_maker     :{m.maker}")
    print(m.get_maker())

    """
   (<class '__main__.MarsRoverComp'>, <class 'object'>)
<__main__.Rocket object at 0x7031832444a0>
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'distance', 'launch', 'name']
rocket distance :TillMoon
rocket name     :Mangalyan
Mangalyan has reached TillMoon
m.get_maker     :ISRO
Mangalyan launched by ISRO
 """
        
