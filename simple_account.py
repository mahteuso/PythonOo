from abc import ABCMeta, abstractmethod
class Account(metaclass=ABCMeta):
    list_account = []
    def __init__(self, number):
        self._number = number
        self._balance = 0
        Account.list_account.append(self)

    def __str__(self):
        return f'Number of account is {self._number} and your balance is {self._balance}'
    @abstractmethod
    def cash(self):
        pass

    def deposit(self, value):
        self._balance += value


class AccountCurrent(Account):

    def __init__(self, number):
        super().__init__(number)

    def cash(self):
        self._balance -= 5
        return self._balance


class AccountSavings(Account):
    def __init__(self, number):
        super().__init__(number)

    def cash(self):
        self._balance *= 1.01
        self._balance -= 5
        return self._balance


class NewAccount(Account):
    def __init__(self, number):
        super().__init__(number)

    def cash(self):
        return self._balance


mateus = AccountCurrent(123)
roger = AccountSavings(321)
marco = NewAccount(213)


for c in Account.list_account:
    c.deposit(1000) # heritage
    c.cash()  # duck typing
    print(c)


