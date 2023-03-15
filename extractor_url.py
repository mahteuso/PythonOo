url = 'https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'

# getting the reference
first_mark = url.find('?')

# separating terms
firt_term = url[:first_mark]
final_term = url[first_mark + 1:]
print(firt_term)
print(f'{final_term}\n')

# getting the value of a parameters
second_mark = url.find('&')

# work with the url
enter_word = input("Enter a coin: ")
second_term = url[first_mark + 1: second_mark]
index_enter_word = url.find(enter_word)
third_mark = url.find('&', index_enter_word)
index_redeen_value = index_enter_word + (len(enter_word) + 1)

if third_mark == -1:
    third_term = url[second_mark + 1:]
    print(third_term)
    redeen_value_two = url[index_redeen_value:]
    print(redeen_value_two)

else:
    print(f'{second_term}')
    redden_value_one = url[index_redeen_value: second_mark]
    print(f'{redden_value_one}\n')

'''
# getting the reference
question_mark = url.find('?')

# separating terms
url_base = url[:question_mark]
print(url_base)
url_parameters = url[question_mark+1:]
print(url_parameters)

# getting the value of a parameter
search_parameter = input('Enter a parameter: ')
index_search_parameter = url.find(search_parameter)
index_word = index_search_parameter + (len(search_parameter) + 1)
search_word = url[index_word:]
new_mark = url.find('&', index_word)

if new_mark == -1:
    parameter_two = url[index_search_parameter:]
    print(f'\n{parameter_two}')
    print(search_word)
else:
    parameter_one = url[question_mark + 1:new_mark]
    parameter_dolar = url[index_word:new_mark]
    print(f'\n{parameter_one}')
    print(parameter_dolar)
'''
