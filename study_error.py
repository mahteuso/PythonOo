"""Studying error propagation"""

def to_divide(dividend, diviser):
    if not (isinstance(dividend, int) and isinstance(diviser, int)):
        raise ValueError('The to_divide() method only accepts integers')
    try:
        aux = dividend / diviser
    except:
        print(f"Was not possible divider {dividend} by {diviser}")
        raise
    return aux

def test_divide(diviser):

    result = to_divide(10, diviser)
    print(f'The result of dividing 10 by {diviser} is {result}')


if __name__ == '__main__':

    try:
        test_divide(2.5)
    except ZeroDivisionError as E:
        print("Error dividing by zero")
    print('Program closed')

