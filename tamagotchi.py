#!/usr/bin/env python
# coding=utf-8

from tamaView import window, window_stat
from tamaCore.Tamagotchi import Tamagotchi

def main():
    tama = tamaCore.Tamagotchi()

    tamaView.window.start()

    tick_count = 0

    done = False

    while(not done):
        #update Graphics
        updateScreen()

        #pass time
        tick_count += 1
        if(tick_count == window_stat.tick_rate):
            tama.pass_time(1)
            tick_count = 0
        #if(tick_count == tick_rate):

        #check if dead
        if(tama.is_dead()):
            done = True
        #if(tama.is_dead()):

#def main()

main()
