"""test an account"""
from pprint import pprint


class Customer:
    def __init__(self, name, cpf, profession):
        self.name = name
        self.cpf = cpf
        self.profession = profession


class CurrentAccount:
    total_accounts_created = 0
    transfer_rate = None

    def __init__(self, customer, agency, number):
        self.customer = customer
        self.agency = agency
        self.number = number
        CurrentAccount.total_accounts_created += 1
        CurrentAccount.transfer_rate = 30 / CurrentAccount.total_accounts_created

    def transfer(self, value, destiny):
        pass

    def cash(self, value):
        pass

    def balance(self):
        pass

    def deposity(self, value):
        pass
