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

    def print_out(self):
        print(f'{self._name} - {self.year} - likes: {self._likes}')
class Film(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration


    def print_out(self):
        print(f'{self._name} - {self.year} - {self.duration}min - {self.likes} likes')


class Sitcom(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons


    def print_out(self):
        print(f'{self._name} - {self.year} - {self.seasons} seasons - {self.likes} likes')



avangers = Film('Avangers - infinity war', 2018, 160.0)
the_it_crowd = Sitcom('The it crowd', 2006, 4)

avangers.new_likes()
avangers.new_likes()
avangers.new_likes()
the_it_crowd.new_likes()
the_it_crowd.new_likes()
the_it_crowd.new_likes()
the_it_crowd.new_likes()

set_list = [avangers, the_it_crowd]

for program in set_list:
    program.print_out()