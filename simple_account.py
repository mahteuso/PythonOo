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


class InvestmentAccount(Account):
    def __init__(self, number):
        super().__init__(number)

    def cash(self):
        return self._balance


mateus = AccountCurrent(123)
roger = AccountSavings(321)
marco = InvestmentAccount(213)


for c in Account.list_account:
    c.deposit(1000)  # heritage
    c.cash()  # duck typing
    print(c)

for index, d in enumerate(Account.list_account):
    print(f'{index}: {d}')

for i in enumerate(Account.list_account):
    print(i)

users = [
    ("Roger", 45, 1979),
    ("Mateus", 42, 1981),
    ("Marco", 40, 1983)
]

for name, age, year in users:
    print(age)
from functools import total_ordering
@total_ordering
class Student:

    def __init__(self, name, number, age):
        self.name = name
        self.number = number
        self.age = age

    def __repr__(self):
        return repr((self.name, self.number, self.age))

    def __lt__(self, other):
        if self.age != other.age:
            return self.age < other.age
        return self.number < other.number


list_students = [
    Student("Marco", 213, 40),
    Student("Rogerio", 123, 47),
    Student("Mateus", 321, 42),
    Student("Rodrigo", 411, 40)

]
print('')
print("Using a function Sorted")
print(sorted(list_students))
print(sorted(list_students, reverse=True))

print('')
print('new ordination: rising list')

for index, students in enumerate(list_students):
   for i, next_student in enumerate(list_students):
       if students < next_student:
           temp = list_students[index]
           list_students[index] = list_students[i]
           list_students[i] = temp
print(list_students)

print('')
print('new ordination: downward list')

for index, students in enumerate(list_students):
   for i, next_student in enumerate(list_students):
       if students > next_student:
           temp = list_students[index]
           list_students[index] = list_students[i]
           list_students[i] = temp

print(list_students)

