from Tamagotchi import Tamagotchi

class Ball(Tamagotchi):
    """Define a Ball """
    def __init__(self):
        """initialize all the stat of a tamagotchi"""
        super(Tamagotchi,self).__init__()
        self.name = "Ball"
        self.specie = " Ball"
    #def___init__(self)

    def evolve(self):
        """Change an animal on another when age raise 4"""
        if (self.getStat(age) > 4):
            self.__class__ = Cat
    #def evolve(self):
