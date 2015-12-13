#!/usr/bin/env python
# coding=utf-8

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
                pygame.display.set_caption(title)
                function = tamaView.window.stats_scene
            #if(event.key == pygame.K_i):

            elif(event.key == pygame.K_m):
                    title = "Tamagotchi"
                    pygame.display.set_caption(title)
                    function = tamaView.window.main_scene
            #elif(event.key == pygame.K_m):

            elif(event.key == pygame.K_w):
                title = "Wash"
                pygame.display.set_caption(title)
                function = tamaView.window.wash_scene
            #elif(event.key == pygame.K_w):

            elif(event.key == pygame.K_e):
                title = "Eat"
                pygame.display.set_caption(title)
                function = tamaView.window.eat_scene
            #elif(event.key == pygame.K_e):

            elif(event.key == pygame.K_p):
                title = "Play"
                pygame.display.set_caption(title)
                function = tamaView.window.play_scene
            #elif(event.key == pygame.K_p):

            elif(event.key == pygame.K_s):
                title = "Sleep"
                pygame.display.set_caption(title)
                function = tamaView.window.sleep_scene
            #elif(event.key == pygame.K_s):

            elif(event.key == pygame.K_c):
                if(title == "Eat"):
                    args.append("Croquette")



        #elif event.type == pygame.KEYUP:

    # --- Game logic should go here

    function(args)
    pygame.display.flip()



    # --- Limit to tick_rate frames per second
    clock.tick(tick_rate)
    tick_count += 1
    if(tick_count == 60):
        tama.pass_time(1)
        tick_count = 0


    if(tama.is_dead()):
        done = True
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
