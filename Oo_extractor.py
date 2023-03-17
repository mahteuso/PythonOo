import re
class ParameterUrl:
    def __init__(self, url, parameter):
        self.url = self.url_sanitation(url)
        self.parameter = parameter
        self.url_validation()


    def url_sanitation(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def url_validation(self):
        if self.url == '':
            raise ValueError('The url is empty')
        validation = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        if not validation.match(self.url):
            raise ValueError('This url is invalid!')


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

    def __str__(self):
        return self.separation_url()

    def __eq__(self, other):
        return self.url == other.url

#url = ParameterUrl('https://bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real')
parameter = input('Enter a parameter: ')
url = ParameterUrl('http://bytebank.com.br/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real', parameter)
url2 = ParameterUrl('http://bytebank.com.br/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real', parameter)
url.get_values_parameters(parameter)
print(url)
print(url.__eq__(url2))








