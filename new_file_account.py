class CurrentAccount:
    list_account = []
    def __init__(self, code):
        self.code = code
        self.balance = 0
        CurrentAccount.list_account.append(self)

    def deposit(self, value):
        self.balance += value

    def __str__(self):
        return f"[>Code is C:{self.code} and Balance is ${self.balance}<]"

    def get_account(self):
        for c in CurrentAccount.list_account:
            print(c)


account_mateus = CurrentAccount(213)
account_mateus.deposit(300)
print(account_mateus)
account_Roger = CurrentAccount(4321)
account_Roger.deposit(1000)
print(account_Roger)
print(CurrentAccount.list_account)
for c in CurrentAccount.list_account:
    print(c)
