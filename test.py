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


title = "Tamagotchi"
pygame.display.set_caption(title)
function = tamaView.window.main_scene
done = False
done_event = False
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
                if(button_context == context):
                    if(tamaView.window.isin(pos,button)):
                        title = button_title
                    #if(tamaView.window.isin(pos,button)):
                #if(button_context == context):

            #for button in  window_stat.clickable_zones:
        #elif(event.type == pygame.MOUSEBUTTONUP):

    #for event in pygame.event.get():

    if(title == "ID Card"):
        context = "Other"
        done_event = False
        function = tamaView.window.stats_scene
        #if(title == "ID Card"):

    elif(title == "Tamagotchi" or title == "Back"):
        context = "Main"
        done_event = False
        function = tamaView.window.main_scene
        #elif(title == "Tamagotchi"):

    elif(title == "Wash"):
        context = "Other"
        done_event = False
        function = tamaView.window.wash_scene
        #elif(title == "Wash"):

    elif(title == "Eat"):
        context = "Other"
        done_event = False
        function = tamaView.window.eat_scene
        #elif(title == "Eat"):

    elif(title == "Play"):
        context = "Other"
        done_event = False
        function = tamaView.window.play_scene
        #elif(title == "Play"):

    elif(title == "Sleep"):
        context = "Other"
        done_event = False
        function = tamaView.window.sleep_scene
        #elif(title == "Sleep"):

    # elif(event.key == pygame.K_c):
    #     if(title == "Eat"):
    #         args_action.append("Croquette")
    #         args_view.append("Croquette")
    #
    # elif(event.key == pygame.K_b):
    #     if(title == "Eat"):
    #         args_action.append("Banana")
    #         args_view.append("Banana")
    # #elif(event.key == pygame.K_c):

    pygame.display.set_caption(title)

    action = function(args_view)


    pygame.display.flip()

    # --- Game logic
    if(action is not None and not done_event):
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
