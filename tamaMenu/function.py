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
        set a difficulty:
        easy(slow time)
        medium(normal time)
        hard(fast time)
    """
    if(dif == "easy"):
        tick_difficulty = 1
    #if(dif == "easy"):
    if(dif == "medium"):
        tick_difficulty = 2
    #if(condition):
    if(dif == "hard"):
        tick_difficulty = 3
    #if(condition):
    if(dif == "insane"):
        tick_difficulty = 10
    #if(condition):
    return False, None, None
#def difficulty(dif)
def rule():
    """for the rule"""
    file fRule = open("rule.txt")
    rules = fRule.read()
    return False, None, None
#def rule():
