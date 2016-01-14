#!/usr/bin/env python
# coding=utf-8

import pygame
import math

from window_stat import *
import tamaMenu.function as menu

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

def start_scene(screen):
    """ Prints the menu screen """
    global clock
    global view
    global title
    global context

    menu(screen)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        elif(event.type == pygame.MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
            for button_title, button_items in clickable_zones.items():
                button_context, button = button_items
                if(button_context in ["Menu", title]):
                    if(isin(pos,button)):
                        view = button_title
                    #if(isin(pos,button)):
                #if(button_context in ["Menu", title]):
            #for button in clickable_zones.items():
        #elif(event.type == pygame.MOUSEBUTTONUP):
    #for event in pygame.event.get():



    #The default title is the button name
    title = view

    if(title == "New Game"):
        action = menu.new_game
        done = True
        #if(title == "New Game"):
    elif(title == "Continue"):
        action = menu.load
        done = True
        #elif(title == "Continue"):
    elif(title == "Rules"):
        action = menu.rules
        done = True
        #elif(title == "Rules"):
    else:
        action = None
        menu.difficulty(title)
        done = True
    #else (if(title == "New Game")):

    return done, action

#def start_scene(screen):

def menu(screen):
    """ Prints the buttons of the menu screen """
    context = "Main"
    title = "Menu"
    draw_background(screen, context, title)

    for button_title, button_zone in clickable_zones.items():
        context, zone = button_zone
        if(context == "Menu"):
            print "grinch ", button_title
            draw_button(screen, button_title)
        #if(context == "Menu"):
    #for button_title, button_context in clickable_zones.items():
    pygame.display.flip()
#def start_scene(screen):

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
                if(button_context in [context, title, "All"]):
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
    args_view.append(draw_background(screen, context, title))

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
    move(tama, screen)

    pygame.display.flip()


    return(action, args_action, done, done_event)
#def updateScreen(tama, screen, clock):

def draw_background(screen, context, title):
    """Prepares the screens basics: font, background..."""
    screen.fill(WHITE)

    font = pygame.font.SysFont('Calibri', 25, True, False)

    if(title != "Menu" and title != "ID Card"):
        draw_button(screen, "ID Card")

    if(context != "Main"):
        draw_button(screen, "Back")

    #if(context != "Main"):

    return font
#def draw_background(screen):

def main_scene(args):
    """ Creates the main window of the game """
    tama = args[0]
    screen = args[1]

    for button_title, button_zone in clickable_zones.items():
        button_context, button_zone = button_zone
        if(button_context in ["All", "Main"]):
            draw_button(screen, button_title)
    #for button_title, button_zone in clickable_zones.items():
    return None
#def main_window(screen)

def draw_button(screen, title):
    """
        Draws a button on a clickable zone

        Arguments: the screen and the title of the button to blit
    """
    context, zone = clickable_zones[title]
    pygame.draw.rect(screen, BLACK, zone, 2)
    image = pygame.image.load("tamaView/images/"+ title + ".png")
    screen.blit(image, [clickable_zones[title][1][0], clickable_zones[title][1][1]])
#def draw_button(screen, title):

def stats_scene(args):
    """ Prints Tamagotchi's stats """
    tama = args[0]
    screen = args[1]
    font = args[2]
    # --- Drawing code should go here

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
    screen.blit(text, [5, 5])

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
    return function
#def eat_scene(tama, scene):

def play_scene(args):
    """ Makes the Tamagotchi play """
    tama = args[0]
    screen = args[1]
    font = args[2]

    text = font.render(" YOU PLAYED WITH THE TAMAGOTCHI ", True, BLACK)
    screen.blit(text, [5, 5])

    return tama.play
#def play_scene(tama, scene):

def sleep_scene(args):
    """ Makes the Tamagotchi sleep"""
    tama = args[0]
    screen = args[1]
    font = args[2]

    text = font.render(" ZZZZZZZZZZZZZZZZZZZZZZZZ ", True, BLACK)
    screen.blit(text, [5, 5])

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
