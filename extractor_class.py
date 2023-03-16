class ExtractorUrl:
    def __init__(self, url):
        self.url = self.sanitation_url(url)
        self.validation_url()

    def sanitation_url(self, url):
        return url.strip()

    def validation_url(self):
        if self.url == "":
            raise ValueError("The URL is empty")

    def __str__(self):
        return f'The first term is {self.get_url_parts()}'
    def get_url_parts(self):
        first_mark = self.url.find('?')
        first_term = self.url[:first_mark]
        print(first_term)
    def get_parameters_url(self):
        first_mark = self.url.find('?')
        final_term = self.url[first_mark + 1:]
        return final_term
    def get_value_parameter(self, enter_parameter):
        index_enter_parameter = self.url.find(enter_parameter)
        third_mark = self.url.find('&', index_enter_parameter)
        index_redeen_value = index_enter_parameter + (len(enter_parameter) + 1)
        if third_mark == -1:
            redeen_value_two = self.url[index_redeen_value:]
            print(redeen_value_two)

        else:

            redden_value_one = self.url[index_redeen_value: third_mark]
            print(redden_value_one)


extractor_url = ExtractorUrl("https://bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real")
enter_parameter = input("Enter a parameter: ")
extractor_url.get_value_parameter(enter_parameter)

