#!/usr/bin/env python
# coding=utf-8

#//!\\ TODO: Decorateurs Pour Affichage et exec séparés
import pygame
import tamaView.window

from tamaView.window_stat import *

from tamaCore.Tamagotchi import Tamagotchi
import tamaView.window

tama = Tamagotchi()

pygame.init()

screen = pygame.display.set_mode(size)


view = "Tamagotchi"
pygame.display.set_caption(title)
function = tamaView.window.main_scene
done = False
done_event = False
# The context of the window: Main or Other
# The secondary context is defined by the title of the screen
context = "Main"
clock = pygame.time.Clock()
tick_count = 0
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
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
                    #//!\\ TODO: Context thing, there must be a way to make it eat
                    if(tamaView.window.isin(pos,button)):
                        view = button_title
                        done_event = False
                    #if(tamaView.window.isin(pos,button)):
                #if(button_context == context):
            #for button in  window_stat.clickable_zones:
        #elif(event.type == pygame.MOUSEBUTTONUP):
    #for event in pygame.event.get():

    #The default title is the button name
    title = view

    if(view == "ID Card"):
        context = "Other"
        function = tamaView.window.stats_scene
        #if(view == "ID Card"):

    elif(view == "Tamagotchi" or view == "Back"):
        title = "Tamagotchi"
        context = "Main"
        function = tamaView.window.main_scene
        #elif(view == "Tamagotchi" or view == "Back"):

    elif(view == "Wash"):
        context = "Other"
        function = tamaView.window.wash_scene
        #elif(view == "Wash"):

    elif(view == "Eat"):
        context = "Other"
        function = tamaView.window.eat_scene
        #elif(view == "Eat"):

    elif(view == "Play"):
        context = "Other"
        function = tamaView.window.play_scene
        #elif(view == "Play"):

    elif(view == "Sleep"):
        context = "Other"
        function = tamaView.window.sleep_scene
        #elif(view == "Sleep"):

    elif(view == "Croquette" or view == "Banana"):
        title = "Eat"
        context = "Other"
        args_action.append(view)
        args_view.append(view)
        function = tamaView.window.eat_scene
        #elif(title == "Croquette" or title == "Banana"):

    pygame.display.set_caption(title)

    action = function(args_view)

    pygame.display.flip()

    # --- Game logic
    if(action is not None and not done_event):
        print "grinch "
        action(args_action)
        done_event = True
    #if(action is not None and not done_event):


    # --- Limit to tick_rate frames per second
    clock.tick(tick_rate)
    tick_count += 1
    if(tick_count == tick_rate):
        tama.pass_time(1)
        tick_count = 0
    #if(tick_count == tick_rate):


    if(tama.is_dead()):
        done = True
#while not done:

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
