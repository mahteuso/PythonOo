"""
Create constructor method
"""


class Account:

    def __init__(self, number, user, balance, limit, original_limit):
        self.__number = number
        self.__user = user
        self.__balance = balance
        self.__limit = limit
        self.__original_limit = original_limit

    def extract(self):
        print(f"{self.__user} your balance is ${self.__balance}\n"
              f"and your limit is ${self.__original_limit}")

    def cash(self, value):
        new_limit = self.__limit
        limit_original = self.__limit
        if value >= self.__balance:
            new_value = value - self.__balance
            self.__balance = 0
            if new_value <= self.__limit:
                self.__limit -= new_value
                new_limit = self.__limit
            else:
                print("You limit is lower, try another value!")
        else:
            self.__balance -= value
        return limit_original, new_limit

    def deposit(self, value):
        new_value = value
        while True:
            if self.__limit < self.__original_limit:
                while self.__limit < self.__original_limit:
                    self.__limit += 1
                    new_value -= 1
            else:
                while new_value > 0:
                    self.__balance += 1
                    new_value -= 1
                break

    def transfer(self, value, destiny):
        self.cash(value)
        destiny.deposit(value)

    @property
    def balance(self):
        return self.__balance
    @property
    def limit(self):
        return self.__limit
    @property
    def user(self):
        return self.__user
    @limit.setter
    def limit(self, value):
        self.__original_limit = value
