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
height = 600
width = 800
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
# "Croquette" : ("Main", [5, 350, 50, 50]),
# "Banana" : ("Main", [5, 410, 50, 50])
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
BODYSDEFAULT_POS_X = 300
BODYSDEFAULT_POS_Y = 300

BODYSLIMITS = {
"X_MAX_LIM" : BODYSDEFAULT_POS_X + 200,
"X_MIN_LIM" : BODYSDEFAULT_POS_X,
"Y_MAX_LIM" : BODYSDEFAULT_POS_Y - 100,
}

X_SPEED = 2
Y_SPEED = -2

bodysposition = [BODYSDEFAULT_POS_X, BODYSDEFAULT_POS_Y]
bodysmovers = [X_SPEED, Y_SPEED]
