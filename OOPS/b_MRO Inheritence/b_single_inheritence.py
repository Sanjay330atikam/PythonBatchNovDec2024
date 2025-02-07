"""
Purpose: One parent
         Two child

         ex: cars
                BMW
                Audi

"""

class Cars():
    def __init__(self,name,chs,eng):
        self.chs = chs
        self.car_name = name
        self.eng = eng
        print("\n Car Constructor - Intializing a Car %s " % self.car_name)

    def get_chasis(self):
        print("chasis for the car %s is : %d" % (self.car_name, self.chs)) 

    def get_enginee(self):
        print("enginee for th car %s %s"%(self.car_name,self.eng))   

    def hello(self):
        print("I am car Class")  

# super_car=Cars("bmw",123,1245)# Instantination
# print(vars(super_car))
# print(dir(super_car))

#  Car Constructor - Intializing a Car bmw 
# {'chs': 123, 'car_name': 'bmw', 'eng': 1245}
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'car_name', 'chs', 'eng', 'get_chasis', 'get_enginee', 'hello']


class BMW(Cars):
    def __init__(self, name, chs, eng,auto_gear="Non_available"):
        Cars.__init__(self,name, chs, eng)
        self.auto_gear=auto_gear
        print("BMW Constructor - Intialixing a car %s" % name)

    
    def show_auto_gear(self):
        print("Auto gear availiabilty is:  %s" % self.auto_gear)

    def hello(self):
        print("I am a BMW car ") 

class Audi(Cars):
    def __init__(self, name, chs, eng,auto_drive="Not available"):
        Cars.__init__(self,name, chs, eng)
        self.auto_drive = auto_drive
        print("Audi Constructor - Intialixing a car %s" % name)

    def show_auto_drive(self):
        print("Auto drive availiability is: %s " % self.auto_drive)

    def hello(self):
        print("I am Audi car")

car1 = BMW('BMW-X7',12333,6768,"Available")
print("\n Attributes of Car1",dir(car1))
print("\n Methods of Car1",dir(car1))
car1.get_chasis()
car1.get_enginee()
car1.show_auto_gear()
car1.hello()

car2 = Audi('Audi-Q7',8785,467,"Available")
print("\n Attributes of Cars2",dir(car2))
print("\n Methods of Car2",dir(car2))
car2.get_chasis()
car2.get_enginee()
car2.show_auto_drive()
car2.hello()

# Method resoultion Order(MR0)
print(Cars.__mro__)
# (<class '__main__.Cars'>, <class 'object'>)

print(BMW.__mro__)
# (<class '__main__.BMW'>, <class '__main__.Cars'>, <class 'object'>)

print(Audi.__mro__)
# (<class '__main__.Audi'>, <class '__main__.Cars'>, <class 'object'>)


print(f"{issubclass(Audi,Cars)  =}")
print(f"{issubclass(BMW,Cars)   =}")
print(f"{issubclass(BMW,Audi)   =}")
# issubclass(Audi,Cars)  =True
# issubclass(BMW,Cars)   =True
# issubclass(BMW,Audi)   =False