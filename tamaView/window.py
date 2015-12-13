#!/usr/bin/env python
# coding=utf-8
#//!\\ TODO Fix EAT scene, divide functions into print and do
import pygame
import math

from window_stat import *

def main_scene(args):
    """ Creates the main window of the game """
    tama = args[0]
    screen = args[1]

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, [5, 5, 175, 50], 2)
    font_action = pygame.font.SysFont('Calibri', 25, True, False)
    text = font_action.render("WASH", True, GREEN)
    screen.blit(text, [10, 10])


    pygame.draw.rect(screen, BLACK, [5, 180, 175, 50], 2)
    font_action = pygame.font.SysFont('Calibri', 25, True, False)
    text = font_action.render("PLAY", True, GREEN)
    screen.blit(text, [10, 190])


    pygame.draw.rect(screen, BLACK, [5, 350, 175, 50], 2)
    font_action = pygame.font.SysFont('Calibri', 25, True, False)
    text = font_action.render("EAT", True, GREEN)
    screen.blit(text, [10, 360])


    pygame.draw.rect(screen, BLACK, [200, 5, 175, 50], 2)
    font_action = pygame.font.SysFont('Calibri', 25, True, False)
    text = font_action.render("SLEEP", True, GREEN)
    screen.blit(text, [210, 10])

    pygame.draw.rect(screen, BLACK, [200, 180, 175, 50], 2)
    font_action = pygame.font.SysFont('Calibri', 25, True, False)
    text = font_action.render("ID CARD", True, GREEN)
    screen.blit(text, [210, 190])


#def main_window(screen)

def stats_scene(args):
    """ Prints Tamagotchi's stats """
    tama = args[0]
    screen = args[1]

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

    pygame.draw.line(screen, RED, [0, posY], [width, posY], 5)

    posY += 5
    #Stats
    for stat, value in tama.get_all_stat().items():
        text = font.render(stat.upper() + ": " + str(math.trunc(value)), True, BLACK)
        screen.blit(text, [posX, posY])
        posY += 30

    #for stat, value in get_all_stats().items():

#def afficher(tama):

def wash_scene(args):
    """ Wash the Tamagotchi """
    tama = args[0]
    screen = args[1]

    screen.fill(WHITE)

    font = pygame.font.SysFont('Calibri', 25, True, False)

    text = font.render(" YOU WASHED THE TAMAGOTCHI ", True, BLACK)
    screen.blit(text, [5, 450])

    tama.wash()

#def wash_scene(tama, scene):

def eat_scene(args):
    """ Feed the Tamagotchi """
    tama = args[0]
    screen = args[1]

    screen.fill(WHITE)


    # if(len(args) > 2):
    #     font = pygame.font.SysFont('Calibri', 50, True, True)
    #     text = font.render(args[2].upper(), True, BLACK)
    #     screen.blit(text, [5, 450])
    #
    # else:
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(" CROQUETTE OR BANANA ?", True, BLACK)
    screen.blit(text, [5, 450])


#def eat_scene(tama, scene):

def play_scene(args):
    """ Makes the Tamagotchi play """
    tama = args[0]
    screen = args[1]
    screen.fill(WHITE)

    font = pygame.font.SysFont('Calibri', 25, True, False)

    text = font.render(" YOU PLAYED WITH THE TAMAGOTCHI ", True, BLACK)
    screen.blit(text, [5, 450])

    tama.play()
#def play_scene(tama, scene):


def sleep_scene(args):
    """ Makes the Tamagotchi sleep"""
    tama = args[0]
    screen = args[1]
    screen.fill(WHITE)

    font = pygame.font.SysFont('Calibri', 25, True, False)

    text = font.render(" ZZZZZZZZZZZZZZZZZZZZZZZZ ", True, BLACK)
    screen.blit(text, [5, 450])

    tama.sleep()
#def sleep_scene(tama, scene):
