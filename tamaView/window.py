#!/usr/bin/env python
# coding=utf-8

import pygame
from Block import *
import math

from window_stat import *

def start():
    """
        Starts the pygame engine and the screen
        Return : the screen to display
    """
    global clock
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(title)
    clock = pygame.time.Clock()

    return screen, clock
#def start():

def quit():
    """ Ferme la fenêtre et quitte le jeu """
    pygame.quit()
#def quit():
def updateScreen(tama, screen, done):
    """
        The main window event

        Arguments: The tamagotchi, the screen, and the quit boolean
        Return: the tamagotchi's action, the arguments of that action, and the
            quit boolean
    """

    global clock
    global view
    global title
    global context
    done_event = True
    action = None
    function = eat_scene


    args_view = [tama, screen]
    args_action = []

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        elif(event.type == pygame.MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
            for button_title, button_items in clickable_zones.items():
                button_context, button = button_items
                if(button_context in [context, title]):
                    if(isin(pos,button)):
                        view = button_title
                        done_event = False
                    #if(isin(pos,button)):
                #if(button_context == context):
            #for button in clickable_zones.items():
            #elif(event.type == pygame.MOUSEBUTTONUP):

        elif(event.type == pygame.MOUSEBUTTONUP):
            if(title == "Eat"):
                view = "Tamagotchi"


    #for event in pygame.event.get():



    #The default title is the button name
    title = view
    args_view.append(draw_background(screen, context))

    if(view == "ID Card"):
        context = "Other"
        function = stats_scene
        #if(view == "ID Card"):

    elif(view == "Tamagotchi" or view == "Back"):
        title = "Tamagotchi"
        context = "Main"
        function = main_scene
        #elif(view == "Tamagotchi" or view == "Back"):

    elif(view == "Wash"):
        context = "Other"
        function = wash_scene
        #elif(view == "Wash"):

    elif(view == "Play"):
        context = "Other"
        function = play_scene
        #elif(view == "Play"):

    elif(view == "Sleep"):
        context = "Other"
        function = sleep_scene
        #elif(view == "Sleep"):

    elif(view == "Croquette" or view == "Banana"):
        title = "Eat"
        context = "Main"
        args_action.append(view)
        args_view.append(view)
        args_view.append(title)
        function = eat_scene
        #elif(title == "Croquette" or title == "Banana"):

    pygame.display.set_caption(title)
    action = function(args_view)
    print "grinchMAINSCENE ", action
    move(tama, screen)

    pygame.display.flip()
    clock.tick(tick_rate)


    return(action, args_action, done, done_event)
#def updateScreen(tama, screen, clock):


def draw_background(screen, context):
    """Prepares the screens basics: font, background..."""
    screen.fill(WHITE)

    font = pygame.font.SysFont('Calibri', 25, True, False)

    if(context != "Main"):
        button_text, button_zone = clickable_zones["Back"]
        pygame.draw.rect(screen, BLACK, button_zone, 2)
        text = font.render("Back", True, GREEN)
        screen.blit(text, [button_zone[0] + 5, button_zone[1] + 5])
    #if(context != "Main"):

    return font
#def draw_background(screen):

def main_scene(args):
    """ Creates the main window of the game """
    tama = args[0]
    screen = args[1]

    image = draw_button(screen, "Wash", clickable_zones["Wash"])
    screen.blit(image, [clickable_zones["Wash"][1][0], clickable_zones["Wash"][1][1]])

    image = draw_button(screen, "Sleep", clickable_zones["Sleep"])
    screen.blit(image, [clickable_zones["Sleep"][1][0], clickable_zones["Sleep"][1][1]])

    image = draw_button(screen, "Banana", clickable_zones["Banana"])
    screen.blit(image, [clickable_zones["Banana"][1][0], clickable_zones["Banana"][1][1]])

    image = draw_button(screen, "Croquette", clickable_zones["Croquette"])
    screen.blit(image, [clickable_zones["Croquette"][1][0], clickable_zones["Croquette"][1][1]])

    image = draw_button(screen, "Play", clickable_zones["Play"])
    screen.blit(image, [clickable_zones["Play"][1][0], clickable_zones["Play"][1][1]])

    image = draw_button(screen, "ID Card", clickable_zones["ID Card"])
    screen.blit(image, [clickable_zones["ID Card"][1][0], clickable_zones["ID Card"][1][1]])

    return None

#def main_window(screen)

def draw_button(screen, title, click_zone):
    """
        Draws a button on a clickable zone

        Arguments: the screen and the font to use
        Return: the image to blit
    """
    context, zone = click_zone
    pygame.draw.rect(screen, BLACK, zone, 2)
    image = pygame.image.load("tamaView/images/"+ title + ".png")

    return image
#def draw_button(font_action):

def stats_scene(args):
    """ Prints Tamagotchi's stats """
    tama = args[0]
    screen = args[1]
    font = args[2]
    # --- Drawing code should go here

    font = draw_background(screen, "Other")

    posY = default_posY
    posX = default_posX

    # Name
    text = font.render("NAME: " + tama.name, True, BLACK)
    screen.blit(text, [posX, posY])
    posY += 30

    # Age
    text = font.render("AGE: " + str(tama.get_stat("age")), True, BLACK)
    screen.blit(text, [posX, posY])
    posY += 30

    # Weight
    text = font.render("WEIGHT: " + str(tama.get_stat("weight")), True, BLACK)
    screen.blit(text, [posX, posY])
    posY += 30

    # Status
    status = ""
    for element in tama.get_sick():
        status += element + " "
    #for element in tama.get_sick():

    text = font.render("STATUS: " + status, True, BLACK)
    screen.blit(text, [posX, posY])
    posY += 30

    pygame.draw.line(screen, RED, [0, posY], [width, posY], 5)

    posY += 5
    #Stats
    for stat, value in tama.get_all_stat().items():
        if(stat not in ["age", "expectancy"]):
            text = font.render(stat.upper() + ": " + str(math.trunc(value)), True, BLACK)
            screen.blit(text, [posX, posY])
            posY += 30
        #if(stat not in ["age", "expectancy"]):
    #for stat, value in get_all_stats().items():

    return None
#def afficher(tama):

def wash_scene(args):
    """ Wash the Tamagotchi """
    tama = args[0]
    screen = args[1]
    font = args[2]

    text = font.render(" YOU WASHED THE TAMAGOTCHI ", True, BLACK)
    screen.blit(text, [5, 450])

    return tama.wash

#def wash_scene(tama, scene):

def eat_scene(args):
    """ Feeds the Tamagotchi """
    global view
    tama = args[0]
    screen = args[1]
    font = args[2]
    screen_title = args[4]
    function = main_scene(args)

    if(screen_title == "Eat"):
        mouse = pygame.image.load("tamaView/images/" + args[3] + ".png")
        mouse_pos = pygame.mouse.get_pos()
        mouse_rect = mouse.get_rect()
        mouse_rect.x = mouse_pos[0]
        mouse_rect.y = mouse_pos[1]
        screen.blit(mouse, mouse_pos)

        tama_rect = tama.picture.get_rect()
        tama_rect.x = bodysposition[0]
        tama_rect.y = bodysposition[1]

        if(mouse_rect.colliderect(tama_rect)):
            function = tama.eat
            view = "Tamagotchi"

    #if(not done_event):
    print "grinchEATSCENE ", function
    return function
#def eat_scene(tama, scene):

def play_scene(args):
    """ Makes the Tamagotchi play """
    tama = args[0]
    screen = args[1]
    font = args[2]

    text = font.render(" YOU PLAYED WITH THE TAMAGOTCHI ", True, BLACK)
    screen.blit(text, [5, 450])

    return tama.play
#def play_scene(tama, scene):


def sleep_scene(args):
    """ Makes the Tamagotchi sleep"""
    tama = args[0]
    screen = args[1]
    font = args[2]

    text = font.render(" ZZZZZZZZZZZZZZZZZZZZZZZZ ", True, BLACK)
    screen.blit(text, [5, 450])

    return tama.sleep
#def sleep_scene(tama, scene):

def isin(pos, zone):
    """ Determines if pos is in the area determined by zone """
    i = zone[0] # Horizontal beginning
    j = zone[1] # Vertical beginning
    xlim = zone[2] # Width
    ylim = zone[3] # Height
    POSX, POSY = pos # Positions

    return(POSX >= i and POSX <= xlim + i \
            and POSY >= j and POSY <= ylim + j)

#def isin(pos, zone):

def move(tama, screen):
    """ Displays the tamagotchi's picture and make it move on the screen """
    global bodysposition
    global bodysmovers
    global X_SPEED
    global Y_SPEED

    screen.blit(tama.picture, bodysposition)
    bodysposition[0] += bodysmovers[0]
    bodysposition[1] += bodysmovers[1]


    if(bodysposition[0] >= BODYSLIMITS["X_MAX_LIM"] or bodysposition[0] <= BODYSLIMITS["X_MIN_LIM"]):
        bodysmovers[0] = -X_SPEED
        bodysmovers[1] = -Y_SPEED
        X_SPEED = -X_SPEED
        Y_SPEED = -Y_SPEED
    #if(bodysposition[0] >= BODYSLIMITS["X_MAX_LIM"]):

    if(bodysposition[1] <= BODYSLIMITS["Y_MAX_LIM"]):
        bodysmovers[1] = -Y_SPEED
        Y_SPEED = -Y_SPEED
    #if(bodysposition[1] <= BODYSLIMITS["Y_MAX_LIM"]):

#def move(tama):
