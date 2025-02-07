"""
Purpose: No limits for Inheritance levels
"""

class level1():
    def level1_method(self):
        print("Level1")



class level2(level1):
    def level2_method(self):
        print("Level2")


class level3(level2):
    def level3_method(self):
        print("Level3")


class level4(level3):
    def level4_method(self):
        print("Level4")


class level5(level4):
    def level5_method(self):
        print("Level5")

object = level5()
object.level1_method()
object.level2_method()
object.level3_method()
object.level4_method()
object.level5_method()