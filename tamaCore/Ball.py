from Tamagotchi import *

class Ball(Tamagotchi):
    """Define a Ball """
    def __init__(self):
        Tamagotchi.__init__(self)
        self.change()
    #def___init__(self)
    def change(self):
        """what change for a Ball """
        self.name = "Ball"
        self.specie = "Ball"
    #END_def
    def evolve(self):
        """Change an animal on another when age raise 4"""
        if (self.get_stat("age") > 4):
            self.__class__ = Cat
            self.change()

    #def evolve(self):

class Cat(Tamagotchi):
    """Define a cat """
    def __init__():
        """initialize all the stat of a tamagotchi"""
        Tamagotchi.__init__(self)
        self.change()
    #def___init__(self)

    def change(self):
        """what change for a Cat """
        self.name = "Cat"
        self.specie = "Cat"
    #END_def
