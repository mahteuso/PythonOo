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

    def __str__(self):
        return f'{self._name} - {self.year} - likes: {self._likes}'


class Playlist:
    def __init__(self, name, program):
        self.name = name
        self._program = program

    def __getitem__(self, item):
        return self._program[item]

    @property
    def matrix(self):
        return self._program

    def __len__(self):
        return len(self._program)


class Film(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'{self._name} - {self.year} - {self.duration}min - {self.likes} likes'


class Sitcom(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'{self._name} - {self.year} - {self.seasons} seasons - {self.likes} likes'


avangers = Film('Avangers: infinity war', 2018, 160.0)
the_it_crowd = Sitcom('The it crowd', 2006, 4)
the_office = Sitcom("the office", 2005, 9)
avatar = Film('avatar', 2009, 162.0)
avatar.new_likes()
avatar.new_likes()
avatar.new_likes()
avatar.new_likes()
avatar.new_likes()
avatar.new_likes()
the_office.new_likes()
the_office.new_likes()
the_office.new_likes()
the_office.new_likes()
avangers.new_likes()
avangers.new_likes()
avangers.new_likes()
avangers.new_likes()
avangers.new_likes()
the_it_crowd.new_likes()
the_it_crowd.new_likes()
the_it_crowd.new_likes()
the_it_crowd.new_likes()

set_list = [avangers, the_it_crowd, the_office, avatar]
playlist_weekend = Playlist('Weekend', set_list)
new_movie = Film('Avangers : infinity war', 2018, 160.0)

search = input('Search: ').title()

print(new_movie in playlist_weekend)

for new in playlist_weekend:
    if new.name[0:4] == search[0:4]:
        print(new)
