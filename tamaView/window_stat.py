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
"Back" : ("Other", [5, height - 60, 50, 50])
}
