#!/usr/bin/env python
# coding=utf-8

import tamaView.window as window
from tamaView.window_stat import *
from tamaCore.Tamagotchi import Tamagotchi
from tamaCore.Ball import Ball
from tamaCore.Cat import Cat
def main():

    done_event = False
    tama = Ball()

    screen, clock = window.start()
    function = window.main_scene

    tick_count = 0

    done = False

    while(not done):
        #update Graphics
        action, args_action, done, done_event = window.updateScreen(tama, screen, done)
        # --- Game logic
        if(action is not None and not done_event):
            action(args_action)
            done_event = True
        #if(action is not None and not done_event):

        #pass time
        tick_count += 1
        if(tick_count == tick_rate):
            tama.pass_time(1)
            tick_count = 0
        #if(tick_count == tick_rate):

        #check if dead
        if(tama.is_dead()):
            done = True
        #if(tama.is_dead()):
    #while(not done):



#def main()

main()
window.quit()
