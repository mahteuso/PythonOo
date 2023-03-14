url = 'https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'


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
