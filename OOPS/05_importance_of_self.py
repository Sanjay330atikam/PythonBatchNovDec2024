"""
Purpose: Importance of Self
        -- Self is a placeholder for the intsance created from the class
        -- Self is not a keyword
"""

class Car:
    Company_name = "TATA"#class variable
    
    def __init__(self,name,price):
        print("\nNew car instance is created")
        self.name = name
        self.Price = price

    def Display_name(self):
        return self.name
    
    def Price(self):# I added price as an additional argument and called it displayed it
        return self.Price
    
if __name__ =='__main__':
    tata_nano = Car("Tata_Nano","6,0000")
    print(tata_nano.Display_name())
    print(vars(tata_nano))
    

    tata_Tiago = Car("Tata_Tiago","15,0000")
    print(tata_Tiago.Display_name())
    print(vars(tata_Tiago))