"""
Methods
1. Intsance Methods
2. Class Methods
3. Static Methods 
"""

class Myclass():
    my_var = "something"

    def display(self,x):#intsnace method taking self
        print("executing instance method display(%s,%s)"%(self,x))
        
    @classmethod
    def cmDisplay(cls,x):#class method taking cls tarcks changes to class level
        print("executing class method display(%s,%s)"%(cls,x))

    @staticmethod# neither use instance method or instance variables nor class method or class varibales
    def smDisplay(x):
        print("executing static method display(%s)"% x)
        # any function which is common utility like everyone uses bt it doesnot consume the values

if __name__ =="__main__":
    a = Myclass()

    a.display("Django")
    Myclass.display(a,"Django")

    a.cmDisplay("Django")
    Myclass.cmDisplay("Django")

    a.smDisplay("Django")
    Myclass.smDisplay("Django")