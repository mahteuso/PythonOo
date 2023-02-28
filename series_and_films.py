class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    def new_likes(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()


class Film(Program):
    def __init__(self, name, year, duration):
        self._name = name.title()
        self.year = year
        self.duration = duration
        self._likes = 0


class Sitcom(Program):
    def __init__(self, name, year, seasons):
        self._name = name.title()
        self.year = year
        self.seasons = seasons
        self._likes = 0


avangers = Film('Avangers - infinity war', 2018, 160.0)
the_it_crowd = Sitcom('The it crowd', 2006, 4)

avangers.new_likes()
avangers.new_likes()
avangers.new_likes()
the_it_crowd.new_likes()
the_it_crowd.new_likes()
the_it_crowd.new_likes()
print(f'Name: {avangers.name}, Year: {avangers.year}, Duration: {avangers.duration} min, Likes: {avangers.likes}')
print(
    f'Name: {the_it_crowd.name}, Year: {the_it_crowd.year}, Seasons: {the_it_crowd.seasons}, Likes: {the_it_crowd.likes}')
