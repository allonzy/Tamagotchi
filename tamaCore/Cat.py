from Tamagotchi import *
from SpeciesList import *

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
        self.set_maxStat("health", 120)
        self.set_maxStat("Age", 100)
        self.picture = pygame.image.load("tamaCore/" + self.specie + "/images/body.png")

    #END_def
