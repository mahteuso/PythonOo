class Film:
    def __init__(self, name, year, duration):
        self.__name = name.title()
        self.year = year
        self.duration = duration
        self.__likes = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name.title()

    @property
    def likes(self):
        return self.__likes

    def new_likes(self):
        self.__likes += 1


class Sitcom:
    def __init__(self, name, year, seasons):
        self.__name = name.title()
        self.year = year
        self.seasons = seasons
        self.__likes = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name.title()

    def new_likes(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes


avangers = Film('Avangers - infinity war', 2018, 160.0)
the_it_crowd = Sitcom('The it crowd', 2006, 4)

avangers.new_likes()
avangers.new_likes()
avangers.new_likes()
the_it_crowd.new_likes()
the_it_crowd.new_likes()
the_it_crowd.new_likes()
print(f'Name: {avangers.name}, Year: {avangers.year}, Duration: {avangers.duration} min, Likes: {avangers.likes}')
print(f'Name: {the_it_crowd.name}, Year: {the_it_crowd.year}, Seasons: {the_it_crowd.seasons}, Likes: {the_it_crowd.likes}')