class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
    #     # your code here
        self.balance = self.balance + amount
        print(self.balance)
        return self

    def withdraw(self, amount):
    #     # your code here
        self.balance-=amount
        # print(self.balance)
        return self

    def display_account_info(self):
    #     # your code here
        print(self.balance)
        return self

    def yield_interest(self):
    #     # your code here
        self.balance = self.balance + (self.balance*self.int_rate)
        # print(self.balance)
        return self

# #NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
#     @classmethod
#     def all_instances(cls):
#         # print(cls.deposit())
#         # print(cls.withdraw)
#         for account in cls.all_instances:
#             account.display_account_info()

account1=BankAccount(.01,100)
account2=BankAccount(.03,1000)

# account1.deposit(100).deposit(100).deposit(100).display_account_info()
# account2.deposit(100).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()
account1.deposit(100)

# BankAccount.all_instances()