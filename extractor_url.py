url = 'https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'

# getting the reference
question_mark = url.find('?')
new_mark = url.find('&')

# separating terms
url_base = url[:question_mark]
print(url_base)
url_parameters = url[question_mark+1:]
print(url_parameters)

# getting the value of a parameter
search_parameter = 'moedaOrigem'
index_search_parameter = url.find(search_parameter)

index_word = index_search_parameter + (len(search_parameter) + 1)
search_word = url[index_word:]

parameter_one = url[question_mark+1:new_mark]
parameter_two = url[new_mark+1:]
print(f'\n{parameter_two}')
print(search_word)


new_search = 'moedaDestino'
index_new_search = url.find('moedaDestino')

len_new_search = index_new_search + (len(new_search) + 1)
parameter_dolar = url[len_new_search:new_mark]
print(f'\n{parameter_one}')
print(parameter_dolar)


