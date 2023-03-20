class Account:
    list_account = []
    def __init__(self, code):
        self._code = code
        self._balance = 0
        Account.list_account.append(self)

    def deposit(self, value):
        self._balance += value

    def __str__(self):
        return f"[>Code is C:{self._code} and Balance is ${self._balance}<]"


class AccountCurrent(Account):
    def cash_month(self):
        self._balance -= 3


class AccountSavings(Account):
    def cash_month(self):
        self._balance *= 1.01
        self._balance -= 5


account_mateus = Account(213)
account_mateus.deposit(300)

account_Roger = Account(4321)
account_Roger.deposit(1000)


print(Account.list_account)

for c in Account.list_account:
    print(c)
