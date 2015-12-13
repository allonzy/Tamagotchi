#!/usr/bin/env python
# coding=utf-8
"""sickness_list[stat]=(sickness_stat,sickness_statValue,sickness_degen)"""
sickness_list = {
"Hungry": ("satiety",20, {"health" = -0.2 } ),
"Very Hungry":("satiety",0, {"health" = -0.46 } ),
"Tired": ("energy",20, {"happyness" = -0.2 } ),
"Very Tired": ("energy",0, {"happyness" = -0.46 } ),
"Dirty": ("cleanness",20,{"happyness" = -0.2 } ),
"Very Dirty": ("cleanness",0,{"happyness" = -0.2 } )
"Depressive": ("happyness",20,{ "happyness": -0.5 ,"health": -0.5 } )
"Very Depressive":("happyness",0,{"happyness": -0.5,"health": -0.5})
}
