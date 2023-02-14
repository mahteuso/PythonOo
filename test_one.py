"""
learning about functions and objects orientation
"""

def create_account(number, user, balance, limit):
    account = {'number': number, 'user': user, 'balance': balance, 'limit': limit}

def extract(account):
    print(f"You balance is: {account['balance']}")

def cash(account, value):
    if value > account['balance']:
        if value <= account['limit']:
            account['limit'] -= value
        else:
            print("You limit is out")
    else:
        account['balance'] -= value


def deposit(account, value):
