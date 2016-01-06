from Tamagotchi import *
from SpeciesList import *

class Fish(Tamagotchi):
    """Define a Fish """
    def __init__():
        """initialize all the stat of a tamagotchi"""
        Tamagotchi.__init__(self)
        self.change()
    #def___init__(self)

    def change(self):
        """what change for a Fish """
        self.name = "Fish"
        self.specie = "Fish"
        self.set_maxStat("health", 100)
        self.set_maxStat("Age", 50)
    #END_def
