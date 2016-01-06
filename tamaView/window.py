#!/usr/bin/env python
# coding=utf-8
#//!\\ TODO Give the bitch a body and make it move!
import pygame
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
    global done_event

    args_view = [tama, screen]
    args_action = []

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        elif(event.type == pygame.MOUSEBUTTONUP):
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
    #for event in pygame.event.get():

    #The default title is the button name
    title = view

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

    elif(view == "Eat"):
        context = "Other"
        function = eat_scene
        #elif(view == "Eat"):

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
        context = "Other"
        args_action.append(view)
        args_view.append(view)
        function = eat_scene
        #elif(title == "Croquette" or title == "Banana"):

    pygame.display.set_caption(title)

    action = function(args_view)

    move(tama)

    pygame.display.flip()
    clock.tick(tick_rate)


    return(action, args_action, done)
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

    font_action = draw_background(screen, "Main")

    pygame.draw.rect(screen, BLACK, [5, 5, 175, 50], 2)
    text = font_action.render("WASH", True, GREEN)
    screen.blit(text, [10, 10])


    pygame.draw.rect(screen, BLACK, [5, 180, 175, 50], 2)
    text = font_action.render("PLAY", True, GREEN)
    screen.blit(text, [10, 190])


    pygame.draw.rect(screen, BLACK, [5, 350, 175, 50], 2)
    text = font_action.render("EAT", True, GREEN)
    screen.blit(text, [10, 360])


    pygame.draw.rect(screen, BLACK, [200, 5, 175, 50], 2)
    text = font_action.render("SLEEP", True, GREEN)
    screen.blit(text, [210, 10])

    pygame.draw.rect(screen, BLACK, [200, 180, 175, 50], 2)
    text = font_action.render("ID CARD", True, GREEN)
    screen.blit(text, [210, 190])

    return None

#def main_window(screen)

def stats_scene(args):
    """ Prints Tamagotchi's stats """
    tama = args[0]
    screen = args[1]

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

    font = draw_background(screen, "Other")

    text = font.render(" YOU WASHED THE TAMAGOTCHI ", True, BLACK)
    screen.blit(text, [5, 450])

    return tama.wash

#def wash_scene(tama, scene):

def eat_scene(args):
    """ Feeds the Tamagotchi """
    tama = args[0]
    screen = args[1]

    font = draw_background(screen, "Other")


    if(len(args) > 2):
        message = "YOU GAVE " + args[2].upper() + " TO THE TAMAGOTCHI"
        text = font.render(message, True, BLACK)
        screen.blit(text, [5, 450])
        function = tama.eat
        #if(len(args) > 2):

    else:
        # text = font.render(" CROQUETTE OR BANANA ?", True, BLACK)

        button_text, button_zone = clickable_zones["Croquette"]
        pygame.draw.rect(screen, BLACK, button_zone, 2)
        text = font.render("Croquette", True, GREEN)
        screen.blit(text, [button_zone[0] + width / 2 - 10, button_zone[1] + height / 4 - 10])

        button_text, button_zone = clickable_zones["Banana"]
        pygame.draw.rect(screen, BLACK, button_zone, 2)
        text = font.render("Banana", True, GREEN)
        screen.blit(text, [button_zone[0] + width / 2 - 10, button_zone[1] + height / 4 - 10])

        function = None
    #else(if(len(args) > 2):)

    return function
#def eat_scene(tama, scene):

def play_scene(args):
    """ Makes the Tamagotchi play """
    tama = args[0]
    screen = args[1]
    font = draw_background(screen, "Other")

    text = font.render(" YOU PLAYED WITH THE TAMAGOTCHI ", True, BLACK)
    screen.blit(text, [5, 450])

    return tama.play
#def play_scene(tama, scene):


def sleep_scene(args):
    """ Makes the Tamagotchi sleep"""
    tama = args[0]
    screen = args[1]
    font = draw_background(screen, "Other")

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

def move(tama):
    """ Displays the tamagotchi's picture """
    global bodysposition
    tamaClass = tama.get_stat("specie")

    image = pygame.image.load("tamaView/" + tamaClass + "/body.gif").convert()

    screen.blit(image, bodysposition)
#def move(tama):
