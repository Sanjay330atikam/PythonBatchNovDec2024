class Robot():
    populatiom = 0 # class variable counting the umber of robots

    def __init__(self,name):
        self.name = name
        print("\n(Intilizaing{})".format(self.name))
        Robot.populatiom += 1

    def __del__(self):# destructor is responsible for delteing the class instance , called when delteing the class instance
        print("\n{} is being destroyed".format(self.name))
        Robot.populatiom -=1
        if Robot.populatiom == 0:
            print("{} was the last one ".format(self.name))
        else:
            print("there are still {:d} robots working".format(self.populatiom))
        
    def say_hi(self):
        """
        Greetings by the robot 
        Yeah,they can do that.
        :return
        """
        print("Greetings, my masters call me {}".format(self.name))

    @classmethod # it is built in function and decorator also
    def how_many(cls):
        """
        print the current population
        :return
        """
        print("\t we have two {:d}robots.".format(cls.populatiom))

if __name__ == "__main__":
    chitti = Robot("chitti")
    chitti.say_hi()# for the ordinary instance method we are calling by the instnace we created
    Robot.how_many()# but for the Class method we are calling with respect to  Class name  

    robo =Robot("robo")
    robo.say_hi()
    Robot.how_many()

    del chitti
    # Delete an instance

    droid = Robot("R2-D2")
    droid.say_hi()
    Robot.how_many()
"""
    (Intilizaingchitti)
Greetings, my masters call me chitti
         we have two 1robots.

(Intilizaingrobo)
Greetings, my masters call me robo
         we have two 2robots.

chitti is being destroyed
there are still 1 robots working

(IntilizaingR2-D2)
Greetings, my masters call me R2-D2
         we have two 2robots.

robo is being destroyed
there are still 1 robots working

R2-D2 is being destroyed This is being delted becuase memory is been reallocated
R2-D2 was the last one 

"""