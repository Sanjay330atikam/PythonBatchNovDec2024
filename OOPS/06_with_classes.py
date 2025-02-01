

class Account():
    def __init__(self,name):
        self.balance = 0
        self.account_holder = name

    def depoist(self,amount):
        self.balance = self.balance + amount

    def with_drawl(self,amount):
        self.balance = self.balance - amount

    def display_balance(self):
        return f"Account balance for {self.account_holder} is {self.balance}"
    
if __name__ == "__main__":
  Ram = Account("Ram")
  print(vars(Ram))
  print("\nIntially",Ram.display_balance())

  Ram.depoist(100)
  print("After Deposit = ",Ram.display_balance())

  Ram.with_drawl(10)
  print("After With_drawl = ",Ram.display_balance())
  print("----------------------")
  print()

  Deep = Account("Deep")
  print(vars(Deep))
  print("\nIntially",Deep.display_balance())

  Deep.depoist(100)
  print("After Deposit = ",Deep.display_balance())

  Deep.with_drawl(10)
  print("After With_drawl = ",Deep.display_balance())
  print("----------------------")


# if we give deposut and with_drwals amount 
#   Deep = Account("Deep")
#   print(Deep.depoist(100))
#   print(Deep.with_drawl(10))
#   print(Deep.display_balance())
#   print(vars(Deep))