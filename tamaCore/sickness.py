#!/usr/bin/env python
# coding=utf-8
"""sickness_list[stat]=(sickness_stat,sickness_statValue,sickness_degen)"""
sickness_list = dict()
sickness_list = {
<<<<<<< HEAD
"Healthy": ["health",100, {} ],
"Hungry": ["satiety",20, {"health" = -0.2 } ],
"Very Hungry":["satiety",0, {"health" = -0.46 } ],
"Tired": ["energy",20, {"happyness" = -0.2 } ],
"Very Tired": ["energy",0, {"happyness" = -0.46 } ],
"Dirty": ["cleanness",20,{"happyness" = -0.2 } ],
"Very Dirty": ["cleanness",0,{"happyness" = -0.2 } ],
"Depressive": ["happyness",20,{ "happyness": -0.5 ,"health": -0.5 } ],
"Very Depressive":["happyness",0,{"happyness": -0.5,"health": -0.5} ],
"Skinny":["weight",30,{"energy": -0.2}],
"Very skinny":["weight",10,{"energy": -0.46}],
"Fat":["weight",70,{"energy": -0.2}],
"Very fat":["weight",90,{"energy": -0.2}],
=======
"Healthy": ("health",100, {} ),
"Hungry": ("satiety",20, {"health" : -0.2 } ),
"Very Hungry":("satiety",0, {"health" : -0.46 } ),
"Tired": ("energy",20, {"happyness" : -0.2 } ),
"Very Tired": ("energy",0, {"happyness" : -0.46 } ),
"Dirty": ("cleanness",20,{"happyness" : -0.2 } ),
"Very Dirty": ("cleanness",0,{"happyness" : -0.2 } ),
"Depressive": ("happyness",20,{ "happyness": -0.5 ,"health": -0.5 } ),
"Very Depressive":("happyness",0,{"happyness": -0.5,"health": -0.5})

>>>>>>> e30ca7c840f439b02fff5db7bc5bf5fec0fa97d3
}
