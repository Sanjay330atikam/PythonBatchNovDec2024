"""
In python everything we store in objects, if two functions having same name
with different signatures whatever the latest functions will taken

METHOD OVERWRITTING - In python everything we store in objects, if two METHODS having same name
with different signatures whatever the latest METHODS will taken
"""
class MynewClass(object):
    """
    This is method overwritting
    """
    def my_function(self,name):
        print("Hello World One variable Case")

    def my_function(self,name,age):
        # self.name = name
        # self.age = age
        print("Hello World Two variable Case")
        # return("%s is %s"%(self.name, self.age))

m = MynewClass()
# m.my_function('Sanju')
# TypeError: MynewClass.my_function() missing 1 required positional argument: 'age'
m.my_function('Sanju',24)
# print(m.my_function('Sanju',24))



class MynewClass(object):
    """
    This is method overwritting
    """
    def my_function(self,name,age):
        print("Hello World Two variable Case")
        
    def my_function(self,name):
        print("Hello World One variable Case")

m2 = MynewClass()
m2.my_function('sanju')