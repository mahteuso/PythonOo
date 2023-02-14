"""
learning about functions and objects orientation
"""


def create_account(number, user, balance, limit):
    account = {"number": number, "user": user, "balance": balance, "limit": limit}
    return account


def extract(account):
    print(f"Your balance is: {account['balance']}\n"
          f"and your limite is {account['limit']}")


def cash(account, value):
    new_limit = account['limit']
    limit_original = account['limit']
    if value >= account['balance']:
        new_value = value - account['balance']
        account['balance'] = 0
        if new_value <= account['limit']:
            account['limit'] -= new_value
            new_limit = account['limit']
        else:
            print("You limit is lower, try another value!")
    else:
        account['balance'] -= value
    return limit_original, new_limit


def deposit(account, value, limit):
    limit_now = account['limit']
    new_value = value
    print(limit)
    while True:
        if limit_now < limit:
            account['limit'] += 1
            new_value -= 1
        else:
            while new_value > 0:
                account['balance'] += 1
                new_value -= 1
            break
