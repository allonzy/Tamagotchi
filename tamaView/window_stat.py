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
height = 400
width = 600
size = (width, height)

#Set the title of the screen
title = "Tamagotchi"

#Set the default position of stuff
default_posX = 5
default_posY = 5

#Set the default tick rate
tick_rate = 60
tick_difficulty = 1

#Set the clickable zones on the screen
#title : context, [x, y, width, height]
MENU_BUTTON_X_SIZE = 359
MENU_BUTTON_Y_SIZE = 50


BUTTON_X_SIZE = 175
BUTTON_Y_SIZE = 50

FOOD_X_POSITION = 5
FOOD_Y_POSITION = height - 60
FOOD_X_SIZE = 50
FOOD_Y_SIZE = 50

clickable_zones = {
"ID Card" : ("All", [width - BUTTON_X_SIZE - 5, 5, BUTTON_X_SIZE, BUTTON_Y_SIZE]),
"Wash" : ("Main", [5, 5, BUTTON_X_SIZE, BUTTON_Y_SIZE]),
"Play" : ("Main", [5, 10 + BUTTON_Y_SIZE, BUTTON_X_SIZE, BUTTON_Y_SIZE]),
"Sleep" : ("Main", [5, 15 + 2*(BUTTON_Y_SIZE), BUTTON_X_SIZE, BUTTON_Y_SIZE]),
"Croquette" : ("Main", [FOOD_X_POSITION, FOOD_Y_POSITION, FOOD_X_SIZE, FOOD_Y_SIZE]),
"Banana" : ("Main", [FOOD_X_POSITION + FOOD_X_SIZE + 5, FOOD_Y_POSITION, FOOD_X_SIZE, FOOD_Y_SIZE]),
"Back" : ("Other", [5, height - 60, 50, 50]),
"New Game" : ("Menu", [5, 5, MENU_BUTTON_X_SIZE, MENU_BUTTON_Y_SIZE]),
"Continue" : ("Menu", [5, 10 + MENU_BUTTON_Y_SIZE, MENU_BUTTON_X_SIZE, MENU_BUTTON_Y_SIZE]),
"Rules" : ("Menu", [5, 15 + 2*(MENU_BUTTON_Y_SIZE), MENU_BUTTON_X_SIZE, MENU_BUTTON_Y_SIZE]),
"Easy" : ("Menu", [5, 20 + 3*(MENU_BUTTON_Y_SIZE), MENU_BUTTON_X_SIZE, MENU_BUTTON_Y_SIZE]),
"Medium" : ("Menu", [10 + MENU_BUTTON_X_SIZE, 20 + 3*(MENU_BUTTON_Y_SIZE), MENU_BUTTON_X_SIZE, MENU_BUTTON_Y_SIZE]),
"Hard" : ("Menu", [15 + 2*(MENU_BUTTON_X_SIZE), 20 + 3*(MENU_BUTTON_Y_SIZE), MENU_BUTTON_X_SIZE, MENU_BUTTON_Y_SIZE]),
"Insane" : ("Menu", [0, width - 4, 4, 4])
}

#Set the default values of the window
view = "Tamagotchi"
title = "Tamagotchi"
# The context of the window: Main or Other
# The secondary context is defined by the title of the screen
context = "Main"

clock = None

#Set the default values of the body's position
BODYSDEFAULT_POS_X = 200
BODYSDEFAULT_POS_Y = 200

BODYSLIMITS = {
"X_MAX_LIM" : BODYSDEFAULT_POS_X + 200,
"X_MIN_LIM" : BODYSDEFAULT_POS_X,
"Y_MAX_LIM" : BODYSDEFAULT_POS_Y - 100,
}

X_SPEED = 2
Y_SPEED = -2

bodysposition = [BODYSDEFAULT_POS_X, BODYSDEFAULT_POS_Y]
bodysmovers = [X_SPEED, Y_SPEED]

# This variable contains the rules
rules = None
