#!/usr/bin/env python
# coding=utf-8

import pygame

from window_stat import *

def afficher(tama):
    """Affiche les stats du tamagotchi"""
    pygame.init()

    screen = pygame.display.set_mode(size)

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
        stats = str(tama)

        # --- Drawing code should go here

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        # Select the font to use, size, bold, italics
        font = pygame.font.SysFont('Calibri', 25, True, False)
        # Render the text. "True" means anti-aliased text.
        # Black is the color. This creates an image of the
        # letters, but does not put it on the screen

        i = 0
        for line in stats.split('\n'):
            text = font.render(line, True, BLACK)
            screen.blit(text, [0, 0 + i])
            i += 30
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()

#def afficher(tama):
