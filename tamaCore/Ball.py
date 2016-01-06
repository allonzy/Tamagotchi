from Tamagotchi import Tamagotchi

class Ball(Tamagotchi):
    """Define a Ball """
    def __init__(self):
        """initialize all the stat of a tamagotchi"""
        Tamagotchi.__init__(self)
        self.name = "Ball"
        self.specie = "Ball"
    #def___init__(self)

    def evolve(self):
        """Change an animal on another when age raise 4"""
        if (self.get_stat("age") > 4):
            self.__class__ = Cat
    #def evolve(self):
