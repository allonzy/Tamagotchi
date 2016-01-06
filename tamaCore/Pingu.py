from Tamagotchi import *
from SpeciesList import *

class Pingu(Tamagotchi):
    """Define a Pingu """
    def __init__():
        """initialize all the stat of a tamagotchi"""
        Tamagotchi.__init__(self)
        self.change()
    #def___init__(self)

    def change(self):
        """what change for a Pingu """
        self.name = "Pingu"
        self.specie = "Pingu"
        self.set_maxStat("health", 130)
        self.set_maxStat("Age", 80)
    #END_def
