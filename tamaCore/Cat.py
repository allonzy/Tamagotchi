from tamaCore.Tamagotchi import Tamagotchi

class Cat(Tamagotchi):
	"""Define a cat """
	 def __init__(self):
        """initialize all the stat of a tamagotchi"""
		super(Tamagotchi,self).__init__()
		self.specie = " Cat"
		self.name = "Cat"
    #def___init__(self)