class ParameterUrl:
    def __init__(self, url):
        self.url = url.strip()
        self.url_validation()

    def url_validation(self):
        if self.url == '':
            raise ValueError('The url is empty')

    def separation_url(self):
        first_point = self.url.find('?')
        first_term = self.url[:first_point]
        return first_term

    def get_values_parameters(self, parameter):
        index_of_parameter = self.url.find(parameter)
        final_position_parameter = index_of_parameter + (len(parameter) + 1)
        last_reference = self.url.find('&', index_of_parameter)

        if last_reference == -1:
            print(self.url[index_of_parameter:final_position_parameter])
            print(self.url[final_position_parameter:])
        else:
            third_point = self.url.find('&', final_position_parameter)
            print(self.url[index_of_parameter:final_position_parameter])
            print(self.url[final_position_parameter: third_point])


url = ParameterUrl('https://bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real')
parameter = input('Enter a parameter: ')
url.get_values_parameters(parameter)







