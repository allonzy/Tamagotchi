from Tamagotchi import *
from SpeciesList import *

class Ball(Tamagotchi):
    """initialize a Ball """
    def __init__(self):
        Tamagotchi.__init__(self)
        self.change()
    #def___init__(self)
    def change(self):
        """what changes for a Ball """
        self.name = "Ball"
        self.specie = "Ball"

    #END_def
    def evolve(self):
        """Change an animal on another when time has come"""
        if self.get_stat("age") > 6:
            cleanness = self.get_stat("cleanness")
            happyness = self.get_stat("happyness")
            satiety = self.get_stat("satiety")
            if max(cleanness,happyness,satiety) == cleanness :
                self.__class__ = Fish
            elif max(cleanness,happyness,satiety) == happyness :
                self.__class__ = Cat
            else:
                self.__class__ = Pingu
            self.change()

    #def evolve(self):
