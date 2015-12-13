#!/usr/bin/env python
# coding=utf-8

import pygame

from window_stat import *

def afficher_stats(tama):
    """Affiche les stats du tamagotchi"""


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


        # --- Drawing code should go here

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        # Select the font to use, size, bold, italics
        font = pygame.font.SysFont('Calibri', 25, True, False)

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

        pygame.draw.line(screen, RED, [posX, posY], [posX + width, posY], 5)


        i = 0
        # for line in stats.split('\n'):
        #     text = font.render(line, True, BLACK)
        #     screen.blit(text, [posX, posY + i])
        #     i += 30
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to tick_rate frames per second
        clock.tick(tick_rate)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()

#def afficher(tama):
