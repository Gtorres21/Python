class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        # print(self.balance)
        return self

    def withdraw(self, amount):
        self.balance-=amount
        # print(self.balance)
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance = self.balance + (self.balance*self.int_rate)
        # print(self.balance)
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {"checkings": BankAccount(int_rate=0.02, balance=0), "savings": BankAccount(int_rate=0.02, balance=0)}
    
    # other methods
    
    def make_deposit(self, amount):
        self.account["checkings"].deposit(amount)
        self.display_user_balance()
        return self

    def make_withdrawal(self, amount):
        self.account["checkings"].withdraw(amount)
        self.display_user_balance()
        return self

    def display_user_balance(self):
        (self.account["checkings"].display_account_info())
        return self

    def transfer_money(self, amount, other_user):
        self.make_withdrawal(amount) 
        other_user.make_deposit(amount)
        self.display_user_balance()
        other_user.display_user_balance()
        return self


user1=User("Giovanni","email@email.com")
user2=User("Antoine","email.email.com")
user1.make_deposit(100)
user2.make_deposit(100)
user1.transfer_money(50, user2)

# user1.display_user_balance()

# account1=BankAccount(.01,100)
# account2=BankAccount(.03,1000)

# account1.deposit(100).deposit(100).deposit(100).display_account_info()
# account2.deposit(100).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()

