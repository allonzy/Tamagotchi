#!/usr/bin/env python
# coding=utf-8


from tamaCore.Tamagotchi import Tamagotchi
import tamaView.window

tama = Tamagotchi()

while True :
    tamaView.window.afficher_stats(tama)

    tama.pass_time(1000)
    tama.sick()
