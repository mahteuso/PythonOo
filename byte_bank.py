'''
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
'''

class Filme:
    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor
    def __str__(self):
        return f'{self.titulo} + ‘ - ‘ + {self.diretor}'

    def __eq__(self, outro_filme):
        return self.titulo == outro_filme.titulo

def pega_todos_os_filmes():

    meus_filmes = pega_todos_os_filmes()
    for filme in meus_filmes:
        print(filme)

def tenho_o_filme(filme_procurado):
    meus_filmes = pega_todos_os_filmes()
    for filme in meus_filmes:
        if filme_procurado == filme:
            return True
    return False

filme_procurado = Filme('A Teoria de Tudo', 'James Marsh')

if tenho_o_filme(filme_procurado):
    print('Tenho o filme!')
else:
    print('Não tenho')