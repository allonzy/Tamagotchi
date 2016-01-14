from tamaCore.Tamagotchi import Tamagotchi
from tamaCore.SpeciesList import *
def new_game():
    """Create a new game as a ball"""
    return True, None, Ball()
#def New_game()
def load():
    """load a tamagotchi and return it """
    return True, None, Tamagotchi.load_game()
#def load()
def difficulty(dif):
    """
        sets a difficulty:
        easy(slow time)
        medium(normal time)
        hard(fast time)
    """
    if(dif == "Easy"):
        tick_difficulty = 1
    #if(dif == "easy"):
    if(dif == "Medium"):
        tick_difficulty = 2
    #if(condition):
    if(dif == "Hard"):
        tick_difficulty = 3
    #if(condition):
    if(dif == "Insane"):
        tick_difficulty = 10
    #if(condition):
    return False, None, None
#def difficulty(dif)
def rules():
    """for the rules"""

    with open("rule.txt", 'r') as fRules:
        rules = fRule.read()
    #with open("rule.txt", 'r') as fRules:

    return False, None, None
#def rule():
