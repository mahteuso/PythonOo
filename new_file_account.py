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

    def __eq__(self, other):
        return self._code == other._code


mateus = Account(123)
mateus.deposit(1000)

marco = Account(123)
marco.deposit(1000)

print(marco == mateus)
