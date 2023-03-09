"""Studying error propagation"""


def to_divide(dividend, divider):
    try:
        aux = dividend / divider
        return aux
    except:
        print(f"Was not possible divide {dividend} by {divider}")
        raise


def test_division(divider):
    result = to_divide(10, divider)
    print(f'The result of dividing 10 by {divider} is {result}')


try:
    test_division(0)
except ZeroDivisionError as E:
    print("Divide by zero error")
except Exception as E:
    print("Generic treatment")
print('Closed program')
