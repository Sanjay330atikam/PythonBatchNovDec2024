"""
Purpose: Importance of Self
        -- Self is a placeholder for the intsance created from the class
        -- Self is not a keyword
"""

class Car:
    Company_name = "TATA"#class variable
    
    def __init__(self,name):
        print("\nNew car instance is created")
        self.name = name

    def Display_name(self):
        return self.name
    
if __name__ =='__main':
    tata_nano = Car("Tata_Nano")
    print(tata_nano.Display_name())
    print(vars(tata_nano))