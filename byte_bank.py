
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

def to_divide(dividend, divider):
    #print(divider.result)
    return dividend / divider


def test_divider(divider):
    try:
        result = to_divide(10, divider)
        print(result)
    except ZeroDivisionError:
        print("Erro na divisão por zero")
    except TypeError:
        print("entre apenas com números")

try:
    test_divider('a')
except AttributeError:
    print('Erro de atributo')
