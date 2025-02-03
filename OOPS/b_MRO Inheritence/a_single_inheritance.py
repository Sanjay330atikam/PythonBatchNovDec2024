"""
Inheritance - single inheritance
Parent-Child Class relation
Super-Sub Class relation
Purpose - MRO(Method Resolution order)
"""

class Account:
    """
    Parent or super class
    """

    def __init__(self):
       self.balance = 0

    def depoist(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance

# Instantination
# a = Account() 
# print(vars(a))
# print(dir(a))

class MinimumBalanceAccount(Account):
    # in this child class we are interheting the parent class which is Account
    # in this way inheritance is done
    """
    Child or sub class
    """

    def __init__(self):
       Account.__init__(self)#calling the constructor of parent class
       # in this we already defined blance amount and we are using it 
       # In case if we want to add anything new constructor in this child class
       # we can do that along that we must also add Parent Constructor

    def withdraw(self,amount):
        if self.balance - amount<100:
            print("Please maintain minimum balance. Transaction Failed !!!")
        else:
            Account.withdraw(self,amount)

a2 = MinimumBalanceAccount()
print(vars(a2))
print(dir(a2))

# MRO - means asking paticular variable what is route or path in which it take presedence
print(Account.__mro__)
# (<class '__main__.Account'>, <class 'object'>)

print(MinimumBalanceAccount.__mro__)
# (<class '__main__.MinimumBalanceAccount'>, <class '__main__.Account'>, <class 'object'>)

print(f"Initial Balance :{a2.balance}")
print(dir(a2))
print()

a2.depoist(1300)
print(f"After deposit(1300) :{a2.balance}")

a2.withdraw(500)
print(f"After withdrawl(500) :{a2.balance}")

a2.withdraw(1300)
print(f"After withdrawl(1300) :{a2.balance}")