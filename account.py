"""
Create constructor method
"""


class Account:

    def __init__(self, number, user, balance, limit):
        self.number = number
        self.user = user
        self.balance = balance
        self.limit = limit

    def extract(self):
        print(f"{self.user} your balance is ${self.balance}\n"
              f"and your limit is ${self.limit}")

    def cash(self, value):
        new_limit = self.limit
        limit_original = self.limit
        if value >= self.balance:
            new_value = value - self.balance
            self.balance = 0
            if new_value <= self.limit:
                self.limit -= new_value
                new_limit = self.limit
            else:
                print("You limit is lower, try another value!")
        else:
            self.balance -= value
        return limit_original, new_limit

    def deposit(self, value):
        new_value = value
        while True:
            if self.limit < 1000:
                while self.limit < 1000:
                    self.limit += 1
                    new_value -= 1
            else:
                while new_value > 0:
                    self.balance += 1
                    new_value -= 1
                break
