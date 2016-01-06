#!/usr/bin/env python
# coding=utf-8

""" Ce fichier contient les stats utiles à l'affichage de la fenetre principale """


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

PI = 3.141592653

# Set the height and width of the screen
height = 700
width = 1000
size = (width, height)

#Set the title of the screen
title = "Tamagotchi"

#Set the default position of stuff
default_posX = 5
default_posY = 5

#Set the default tick rate
tick_rate = 60

#Set the clickable zones on the screen
#title : context, [x, y, width, height]

clickable_zones = {
"Wash" : ("Main", [5, 5, 175, 50]),
"Play" : ("Main", [5, 180, 175, 50]),
"Eat" : ("Main", [5, 350, 175, 50]),
"Sleep" : ("Main", [200, 5, 175, 50]),
"ID Card" : ("Main", [200, 180, 175, 50]),
"Back" : ("Other", [5, height - 60, 50, 50]),
"Croquette" : ("Eat", [5, 5, width - 10, height / 2 - 10]),
"Banana" : ("Eat", [5, height / 2 + 5, width - 10, height / 2 - 10])
}

#Set the default values of the window
view = "Tamagotchi"
title = "Tamagotchi"
# The context of the window: Main or Other
# The secondary context is defined by the title of the screen
context = "Main"
done_event = False

clock = None

#Set the default values of the body's position
BODYSLIMITS = {
"X_MAX_LIM" : 700,
"X_MIN_LIM" : 500,
"Y_MAX_LIM" : 400,
"Y_MIN_LIM" : 500
}
bodysposition = [500, 500]
bodysmovers = [5, -5]
