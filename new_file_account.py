class Account:
    list_account = []
    def __init__(self, code):
        self.code = code
        self.balance = 0
        Account.list_account.append(self)

    def deposit(self, value):
        self.balance += value

    def __str__(self):
        return f"[>Code is C:{self.code} and Balance is ${self.balance}<]"


class AccountCurrent(Account):
    def cash_month(self):
        self.balance -= 3

class AccountSavings(Account):
    def cash_month(self):
        self.balance *= 1.01
        self.balance -= 5


account_mateus = Account(213)
account_mateus.deposit(300)
print(account_mateus)
account_Roger = Account(4321)
account_Roger.deposit(1000)
print(account_Roger)


print(Account.list_account)

for c in Account.list_account:
    print(c)
