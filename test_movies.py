class Programs:
    total_movies = 0
    def __init__(self, name, year):
        self.name = name.title()
        self.year = year
        self.like = 0
        Programs.total_movies += 1

    @property
    def total(self):
        return self.total_movies
    def __str__(self):
        return f'{self.name} - {self.year} - likes: {self.like} - {self.total_movies}'


    @property
    def likes(self):
        return self.like

    def set_likes(self):
        self.like += 1

    @property
    def names(self):
        return self.name

    @names.setter
    def names(self, new_name):
        self.name = new_name.title()

    def __eq__(self, other):
        return self.year == other.year


class Movies(Programs):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'{self.name} - {self.year} - {self.duration} - likes: {self.like}\n{Programs.total_movies}'


class Sitcom(Programs):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'{self.name} - {self.year} - {self.seasons} - likes: {self.like}\n{self.total_movies}'


# creating movies and Sitcons

avangers = Movies('Avangers: infinity war', 2018, 160.0)
the_it_crowd = Sitcom('The it crowd', 2006, 4)
the_office = Sitcom("the office", 2005, 9)
avatar = Movies('avatar', 2018, 162.0)

set_list = [avangers, the_it_crowd, the_office, avatar]

search = Movies('Avanger', 2018, 160.0)


#input("Serach: ").title()


for words in set_list:
    if words == search:
        print(words)
print()