url = 'https://bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real'

parameter = input('Enter a parameter: ')
# URL sanitation
url = url.strip()

# URL validation
if url == '':
    raise ValueError('The url is empty')

# Separating url parameters
first_point = url.find('?')
first_term = url[: first_point]

# getting url parameters
second_point = url.find('&')
index_of_parameter = url.find(parameter)
final_position_parameter = index_of_parameter + (len(parameter) + 1)
last_reference = url.find("&", final_position_parameter)

# getting values of parameters
if last_reference == -1:
    print(url[index_of_parameter:final_position_parameter])
    print(url[final_position_parameter:])
else:
    third_point = url.find('&', final_position_parameter)
    print(url[index_of_parameter:final_position_parameter])
    print(url[final_position_parameter: third_point])


