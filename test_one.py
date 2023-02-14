"""
learning about functions and objects orientation
"""

def create_account(number, user, balance, limit):
    account = {'number': number, 'user': user, 'balance': balance, 'limit': limit}

def extract(account):
    print(f"You balance is: {account['balance']}")

def