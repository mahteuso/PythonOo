
class Customer:
    def __init__(self, name, cpf, profession):
        self.name = name
        self.cpf = cpf
        self.profession = profession


class CurrentAccount:
    total_accounts_created = 0
    transfer_rate = None

    def __init__(self, customer, agency, number, balance, limit):
        self.customer = customer
        self.__set_agency(agency)
        self.__number = number
        self.__balance = balance
        self.__set_limit(limit)
        CurrentAccount.total_accounts_created += 1
        CurrentAccount.transfer_rate = 30 / CurrentAccount.total_accounts_created

    @property
    def limit(self):
        return self.__limit

    def __set_limit(self, value):
        if not isinstance(value, int):
            raise ValueError('The limit accepts only integers')
        if value <= 0:
            raise ValueError('The limit accepts only numbers greater than zero')
        self.__limit = value

    @property
    def balance(self):
        return self.__balance


    def __set_balance(self, value):
        if not isinstance(value, int):
            raise ValueError("The balance accepts only integers")
        if value <= 0:
            raise ValueError('The balance accepts only numbers greater than zero')
        self.__balance = value

    @property
    def agency(self):
        return self.__agency


    def __set_agency(self, value):
        if not (isinstance(value, int)):
            raise ValueError('Agency accepts only integers')
        if value <= 0:
            raise ValueError("Agency accepts only numbers greater than 0")
        self.__agency = value

    def transfer(self, value, destiny):
        pass

    def cash(self, value):
        pass

    def balance_out(self):
        pass

    def deposity(self, value):
        pass

account1 = CurrentAccount('Mateus', 32, 123, 50, 1000)
print(account1.agency)
account1.agency = 1



