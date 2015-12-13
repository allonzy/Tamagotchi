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

title = "ID Card"
pygame.display.set_caption(title)

done = False

clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    tamaView.window.afficher_stats(tama, screen)

    pygame.display.flip()

    # --- Limit to tick_rate frames per second
    clock.tick(tick_rate)
    tama.pass_time(1)
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
