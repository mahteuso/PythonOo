class Programs:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def __str__(self):
        return f'{self._name} - {self.year}'

    def __eq__(self, other):
        return self.name[:4] == other[:4]
class Movie(Programs):
    account_movies = 0
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration
        Movie.account_movies += 1

    def __str__(self):
        return f'{self.name} - {self.year} - {self.duration} - {Movie.account_movies}'
class Sitcom(Programs):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'{self.name} - {self.year} - {self.seasons}'

avatar = Movie('avatar', 2009, 162.0)
avangers = Movie('Avangers: infinity war', 2018, 160.0)
the_it_crowd = Sitcom('The it crowd', 2006, 4)
the_office = Sitcom("the office", 2005, 9)

set_list = [avatar, avangers, the_it_crowd, the_office]

search = input("Search: ").title()

for new in set_list:
    if new == search:
        print(new)

avatar.name = 'Avante'
