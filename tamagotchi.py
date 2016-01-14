#!/usr/bin/env python
# coding=utf-8

import tamaView.window as window
from tamaView.window_stat import *
from tamaCore.Ball import Ball
def main():
    global tick_rate
    global tick_difficulty

    screen, clock = window.start()
    tama = None
    done = False
    function = window.start_scene

    # Menu
    while (not done):
        action = function(screen)

        if(action is not None):
            done, function, tama = action()
        #if(action is not None):
    #while (not done):

    tama = Ball()
    done_event = False
    function = window.main_scene

    tick_count = 0

    done = False

    # Game
    while(not done):
        #update Graphics
        action, args_action, done, done_event = window.updateScreen(tama, screen, done)
        # --- Game logic
        if(action is not None and not done_event):
            action(args_action)
            done_event = True
        #if(action is not None and not done_event):

        if(action == tama.eat):
            action(args_action)
            done_event = True

        #pass time
        tick_count += 1
        print "grinch ", tick_count, " ", tick_difficulty, " ", tick_rate
        if(tick_count >= tick_rate):
            tama.pass_time(tick_difficulty)
            tick_count = 0
        #if(tick_count == tick_rate):

        #check if dead
        if(tama.is_dead()):
            done = True
        #if(tama.is_dead()):
        clock.tick(tick_rate)
    #while(not done):



#def main()

main()
print "grinch I QUIT!"
window.quit()
print "grinch QUITTED"
