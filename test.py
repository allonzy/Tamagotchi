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

clock = pygame.time.Clock()
tick_count = 0
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    args = [tama, screen]
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYUP:
            if(event.key == pygame.K_i):
                title = "ID_Card"
                done_event = False
                pygame.display.set_caption(title)
                function = tamaView.window.stats_scene
            #if(event.key == pygame.K_i):

            elif(event.key == pygame.K_m):
                title = "Tamagotchi"
                done_event = False
                pygame.display.set_caption(title)
                function = tamaView.window.main_scene
            #elif(event.key == pygame.K_m):

            elif(event.key == pygame.K_w):
                title = "Wash"
                done_event = False
                pygame.display.set_caption(title)
                function = tamaView.window.wash_scene
            #elif(event.key == pygame.K_w):

            elif(event.key == pygame.K_e):
                title = "Eat"
                done_event = False
                pygame.display.set_caption(title)
                function = tamaView.window.eat_scene
            #elif(event.key == pygame.K_e):

            elif(event.key == pygame.K_p):
                title = "Play"
                done_event = False
                pygame.display.set_caption(title)
                function = tamaView.window.play_scene
            #elif(event.key == pygame.K_p):

            elif(event.key == pygame.K_s):
                title = "Sleep"
                done_event = False
                pygame.display.set_caption(title)
                function = tamaView.window.sleep_scene
            #elif(event.key == pygame.K_s):

            elif(event.key == pygame.K_c):
                if(title == "Eat"):
                    args.append("Croquette")



        #elif event.type == pygame.KEYUP:

    action = function(args)
    if(len(args) > 2):
        args.pop();
    #if(len(args) > 2):

    pygame.display.flip()

    if(action is not None and not done_event):
        action()
        done_event = True
    #if(action is not None):

    # --- Game logic




    # --- Limit to tick_rate frames per second
    clock.tick(tick_rate)
    tick_count += 1
    if(tick_count == tick_rate):
        tama.pass_time(1)
        tick_count = 0



    if(tama.is_dead()):
        done = True
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
