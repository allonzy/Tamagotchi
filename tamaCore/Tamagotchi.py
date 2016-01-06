#!/usr/bin/env python
# coding=utf-8

from sickness import *
from aliment import *
import pickle
import time

class Tamagotchi():

    """The core class who describe a tamagotchi(the animal)

    ------------------------atribute----------------------------------
    ~ name: string

    ~ age: float

    ~ expectancy: float // Life time expetency

    ~ health: Dict(bollean) // a table of bolean with all the sick
                                    as key (or,if not sick only "Healthy")

    ~ stat_regen: Dict(degen) // a table of stat degen with a stat as key

    ~ stat_max: Dict(max) // a table of stat degen with a stat as key

    ~ stat: Dict(stat) // a table with a statname as key and a statvalue as value

    ~ stat('weight'): float //Tamagotchi actual weight

    ~ stat('cleanness'): float //Tamagotchi actual level of cleanness 0-X

    ~ stat('happyness'): float //Tamagotchi actual level of happyness 0-X

    ~ stat('satiety'): float //Tamagotchi actual level of food 0-X

    ~stat('energy'): float // Tamagotchi actual level of energy

    ~ statKey: dict //(age,expectancy,weight,cleanness,happyness,energy,hunger)

    ----------------------------Method-------------------------------

    ~get_sick(): void //return the list of actual sickness

    ~_init_stat_regen()

    + eat(string aliment): void

    + play(): void

    + wash(): void

    + heal(): void // automatic heal of sickness if stat is good

    + sick():void //automatic caught sickness if stat is bad

    + sleep(): void

    + die(): void

    ~ _get_sick (string sickness): void

    + watch_stats(): void

    + get_stat(string stat ): float/string(depend on the stat)

    +get_maxStat

    +set_maxStat

    +get_regenStat

    +set_regenStat

    + pass_time(int time): void

    + modify_stat(int stat[])

    + __repr__(): void

    + save ():void //save a game

    + load(): float // load a game and return the time since the last connection

    + get_stat(): dict[stat] = stat_value

    + evolve(): change an animal on another when the contition is good

    +evolveIn(name):change an animal on another with his name
   """

    def __init__(self):
        """initialize all the stat of a tamagotchi"""
        self.name = "Tamagotchi"
        self.specie = "none"
        self.sickness = dict.fromkeys(sickness_list.keys(),False)
        self.sickness["Healthy"] = True
        self.statKey = ('health','age','expectancy','weight',\
                        'cleanness','happyness','satiety','energy')
        self.stat_max = dict.fromkeys(self.statKey,100.0)
        self.stat_regen = dict.fromkeys(self.statKey,0.0)
        self._init_stat_regen()
        self.stat = dict.fromkeys(self.statKey,70.0)
        self.stat['age'] = 0
        self.stat['weight'] = 50
    #def___init__(self)

    def get_all_stat(self):
        """Get all the stat in a dictionnary"""
        return self.stat
    #def get_all_stats():

    def get_sick(self):
        """return all the statues of animal"""
        actual_sickness = dict()
        for key,value in self.sickness.items():
            if value == True:
                actual_sickness[key] = value
            #if value == True:
        #for key in self.sickness:
        return actual_sickness
    #def get_sick(self):

    def _init_stat_regen(self):
        """initialise the regen rate of stat"""
        for element in self.stat_regen.keys():
            self.stat_regen[element] = 0
        #for element in self.stat_regen:
        self.stat_regen['health'] = 0.33
        self.stat_regen['cleanness'] = -0.2
        self.stat_regen['energy'] = -0.2
        self.stat_regen['satiety'] = -0.5
        self.stat_regen['age'] = 2
    #def _init_stat_regen(self):

    def debuff(self):
        """get all the debuff from current sick"""
        self._init_stat_regen()
        if self.sickness["Healthy"] == False:
            for sick in self.sickness:
                if self.sickness[sick] == True:
                    debuff_list = sickness_list[sick][2]
                    for debuff_key in debuff_list:
                        self.stat_regen[debuff_key] += debuff_list[debuff_key]
                    #for debuff_key in debuff_list:
                #if self.sickness [sick] == True:
            #for sick in self.sickness:
        #if self.sickness["Healthy"] == False:
    #def debuff(self):


    def modify_stat(self,score):
        """
            Take a Dict of stat (weight,cleanness,happyness,energy,hunger),
            with modifier as value and "add" it to the stat
        """
        for key in score:
            self.set_stat(key, self.get_stat(key) + score[key])
        #def for key in score:
    #def_modify_stat(self,score)

    def get_stat(self,stat_name):
        """Return the value of a stat by its name //get_stat(stat_name)"""
        return self.stat[stat_name]
    #def get_stat(self,stat_name):

    def set_stat(self,stat_name,stat_value):
        """Set a stat to a given value"""
        self.stat[stat_name] = stat_value
        if self.stat[stat_name] <= 0:
            self.stat[stat_name] = 0
        #if self.stat[stat_name] < 0:
        elif self.stat[stat_name] > self.stat_max[stat_name]:
            self.stat[stat_name] = self.stat_max[stat_name]
        #elif self.stat[stat_name] > 100:
    #def set_stat(self,stat_name):

    def get_maxStat(self,stat_name):
        """Return the value of a stat by its name //get_stat(stat_name)"""
        return self.stat_max[stat_name]
    #def get_maxStat(self,stat_name):

    def set_maxStat(self,stat_name,stat_value):
        """Return the value of a stat by its name //get_stat(stat_name)"""
        self.stat_max[stat_name] = stat_value
    #def get_maxStat(self,stat_name):

    def get_regenStat(self,stat_name):
        """Return the value of a stat by its name //get_stat(stat_name)"""
        return self.stat_regen[stat_name]
    #def get_maxStat(self,stat_name):

    def set_regenStat(self,stat_name,stat_value):
        """Return the value of a stat by its name //get_stat(stat_name)"""
        self.stat_regen[stat_name] = stat_value
    #def get_maxStat(self,stat_name):

    def play(self, *args):
        """A method to make the tamagotchi play"""
        #score = miniGamePlay()
        score = {'energy': -5,'happyness': 10,"weight": -5}
        self.modify_stat(score);
    #def_play(self)

    def wash(self, *args):
        """A method to wash the tamagotchi,mainly increase his cleanness"""
        #score = miniGameWash()
        score = {'cleanness': 10,'happyness': -5}
        self.modify_stat(score);
    #def_wash(self)

    def is_dead(self):
        """return true if dead false else"""
        if self.get_stat("age") > self.get_maxStat("age"):#mort de viellesse
            return true
        return self.sickness ["Dead"]
        #if self.sickness ["Dead"]:
    #def is_dead(self):

    def heal(self):
        """Heal a sickness if stat is hight enought """
        for sickness in sickness_list:
            sickness_stat = sickness_list[sickness][0]
            sickness_stat_value = sickness_list[sickness][1]
            stat_value = self.get_stat(sickness_stat)
            if sickness_stat == "weight":
                if sickness_stat >= 50:#fatty
                    if stat_value <= sickness_stat_value - 5:
                        self.sickness[sickness] = False
                    #if stat_value > sickness_stat
                #if sickness_stat > 50:
                else:
                    if stat_value >= sickness_stat_value + 5:
                        self.sickness[sickness] = False
                    #if stat_value < sickness_stat:
                #else:
            #if sickness_stat == "weight":

            elif stat_value >= sickness_stat_value + 10:
                self.sickness[sickness] = False
            #elif sickness_stat < get_stat(sickness_stat):
        #for sickness in sickness_list:
        is_healthy = True
        for key in self.sickness:
            if key != "Healthy":
                if self.sickness[key] == True :
                    is_healthy = False
                    break
                #if self.sickness[key]:
            #if key != healthy:
        #for key in slef.sickness::
        self.sickness["Healthy"] = is_healthy
    #def health(self):

    def sick(self):
        """Caught sick if stat is low enough """
        for sickness in sickness_list:
            sickness_stat = sickness_list[sickness][0]
            sickness_stat_value = sickness_list[sickness][1]
            sickness_degen = sickness_list[sickness][2]
            stat_value = self.get_stat(sickness_stat)
            if sickness_stat == "weight":
                if sickness_stat_value >= 50:#fatty
                    if stat_value >= sickness_stat_value:
                        self.sickness[sickness] = True
                        #//!\\ actualyse the degen
                    #if stat_value > sickness_stat
                #if sickness_stat > 50:
                else:
                    if stat_value <= sickness_stat_value: #skinny
                        self.sickness[sickness] = True
                        #//!\\ actualyse the degen
                    #if stat_value < sickness_stat_value:
                #else:
            #if sickness_stat == "weight":
            elif stat_value <= sickness_stat_value:
                self.sickness[sickness] = True
                #//!\\ actualise the degen
            #elif stat_value < sickness_stat_value:
        #for sickness in sickness_list:
        is_healthy = True
        for key in self.sickness:
            if key != "Healthy":
                if self.sickness[key] == True :
                    is_healthy = False
                    break
                #if self.sickness[key]:
            #if key != healthy:
        #for key in slef.sickness::
        self.sickness["Healthy"] = is_healthy
    #def sick(self):

    def eat(self, *args):
        """Eat a given aliment to restore energy, health and increase weight """
        #//!\\ Modified the arguments to fit the use of the functions @KirikouLovelace
        aliment_name = args[0][0]
        aliment_satiety = aliment_list[aliment_name][0]
        aliment_happyness = aliment_list[aliment_name][1]
        aliment_weight = aliment_list[aliment_name][2]
        score = {"satiety": aliment_satiety,"happyness": aliment_happyness,"weight": aliment_weight}
        self.modify_stat(score)
    #def eat(self,aliment ):

    def sleep(self, *args):
        """A method to restore tamagotchi energy"""
        score = {"energy" : 2}
        self.modify_stat(score)
    #def_sleep(self):

    def pass_time(self,time):
        """Take a number and go forward in time in minute   """
        x = 0
        while x < time:
            for stat_name in self.stat_regen:
                new_stat = self.get_stat(stat_name) + self.stat_regen[stat_name]
                self.set_stat(stat_name,new_stat)
                #for stat_name in self.stat_regen:
            x += 1
            #while x < time:
        self.sick()
        self.heal()
        self.debuff()
        self.evolve()

    #END_def

    def die(self):
        """Test how it die and return a string"""
        pass
    #def die(self):
    def __repr__(self):
        """ Returns a string representing the current state of the Tamagotchi """
        stats = ""
        for key, value in self.stat.items():
            if(key != "expectancy"):
                stats += key + " " + str(value) + '\n'

        #for key, value in self.stat:
        return stats
    #def __repr__(self):
    def __str__(self):
        """ Returns a string containing the tamagotchi's stats"""
        return self.__repr__()
    #def __str__(self):
#class Tamagotchi:

    def save(self):
        """ Save the game """
        identity = dict.fromkeys(self.statKey)
        for key in identity:
            identity[key] = self.get_value(key)
        identity["Name"] = self.name
        identity["Time"] = time.time()

        with open('save', 'wb') as fichier:
            my_pickler = pickle.Pickler(fichier)
            my_pickler.dump(identity)
    #def save(self)

    def load_game(self):
        """ Load the game and return the time since the last connection """
        with open('save', 'rb') as fichier:
            my_depickler = pickle.Unpickler(fichier)
            identity = my_depickler.load()

            for key, value in identity.items():
                self.set_stat(key,value)
            old_time = identity["Time"]
            now_time = time.time()

            return (now_time - old_time)/60
    #def load_game
    def evolve(self):
        """Empty"""
    #def evolve(self):
    def change(self):
        """Empty"""
    #def change(self):

#class Tamagotchi:
