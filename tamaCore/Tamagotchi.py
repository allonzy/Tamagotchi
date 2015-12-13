#!/usr/bin/env python
# coding=utf-8

#from sickness import *
#from aliment import *
import pickle
class Tamagotchi:

    """The core class who describe a tamagotchi(the animal)

    ------------------------atribute----------------------------------
    ~ name: string

    ~ age: float

    ~ expectancy: float // Life time expetency

    ~ health: Dict(bollean) // a table of bolean with all the sick
                                    as key (or,if not sick only "healthy")

    ~ stat_regen: Dict(degen) // a table of stat degen with a stat as key

    ~ stat_max: Dict(max) // a table of stat degen with a stat as key

    ~ stat: Dict(stat) // a table with a statname as key and a statvalue as value

    ~ stat('weight'): float //Tamagotchi actual weight

    ~ stat('cleanness'): float //Tamagotchi actual level of cleanness 0-X

    ~ stat('happyness'): float //Tamagotchi actual level of happyness 0-X

    ~ stat('satiety'): float //Tamagotchi actual level of food 0-X

    ~stat('energy'): float // Tamagotchi actual level of energy
    
    ~stat('age') : float // Tamagotchi actual age

    ~ statKey: dict //(age,expectancy,weight,cleanness,happyness,energy,hunger)

    ----------------------------Method-------------------------------

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

    + pass_time(int time): void

    + modify_stat(int stat[])

    + __repr__(): void
    
    + save() : void


   """

    def __init__(self):
        """initialize all the stat of a tamagotchi"""
        self.name = "Tamagotchi"
        #//!\\ TODO  self.sickness = dict.fromkeys(sickness_list.keys(),False)
        #//!\\ TODO  self.sickness["healthy"] = True
        self.statKey = ('health','age','expectancy','weight',\
                        'cleanness','happyness','satiety','energy')
        self.stat_max = dict.fromkeys(self.statKey,100.0)
        self.stat_regen = dict.fromkeys(self.statKey,0.0)
        self._init_stat_regen()
        self.stat = dict.fromkeys(self.statKey,70.0)
        self.stat['age'] = 0
        self.stat['weight'] = 50
    #def___init__(self)
    def _init_stat_regen(self):
        """initialise the degen rate of stat"""
        self.stat_regen['health'] = 0.33
        self.stat_regen['cleanness'] = -0.1
        self.stat_regen['energy'] = -0.1
    #def _init_stat_regen(self):

    def set_stat(self,stat_name,stat_value):
        """Set a stat to a given value"""
        self.stat[stat_name] -= stat_value
        if self.stat[stat_name] < 0:
            self.stat[stat_name] = 0
        #if self.stat[stat_name] < 0:
        elif self.stat[stat_name] > 100:
            self.stat[stat_name] = 100
        #elif self.stat[stat_name] > 100:
    #def set_stat(self,stat_name):

    def modify_stat(self,score):
        """
            Take a Dict of stat (weight,cleanness,happyness,exercise,hunger),
            with modifier as value and "add" it to the stat
        """
        for key in score:
            self.set_stat(key,score[key])
        #def for key in score:
    #def_modify_stat(self,score)

    def get_stat(self,stat_name):
        """Return the value of a stat by his name //get_stat(stat_name)"""
        return self.stat(stat_name)
    #def get_stat(self,stat_name):

    def play(self):
        """A method to make the tamagotchi play"""
        #score = miniGamePlay()
        score = {'exercise': -5,'happyness': 10,"weight": -5}
        self.modify_stat(score);
    #def_play(self)

    def wash(self):
        """A method to wash the tamagotchi,mainly increase his cleanness"""
        #score = miniGameWash()
        score = {'cleanness': 10,'happyness': -5}
        self.modify_stat(score);
    #def_wash(self)

    def heal(self):
        """Heal a sickness if stat is hight enought """
        for sickness in sickness_list:
            sickness_stat = sickness_list[sickness][0]
            stat_value = self.get_stat(sickness_stat)
            if sickness_stat == "weight":
                if sickness_stat > 50:#fatty
                    if stat_value < sickness_stat - 5:
                        self.sickness[sickness] = False
                    #if stat_value > sickness_stat
                #if sickness_stat > 50:
                else:
                    if stat_value > sickness_stat + 5:
                        self.sickness[sickness] = False
                    #if stat_value < sickness_stat:
                #else:
            #if sickness_stat == "weight":

            elif stat_value > sickness_stat + 10:
                self.sickness[sickness] = False
            #elif sickness_stat < get_stat(sickness_stat):
        #for sickness in sickness_list:
        is_healthy = True
        for key in slef.sickness:
            if key != healthy:
                if self.sickness[key] == False :
                    healthy = False
                    break
                #if self.sickness[key]:
            #if key != healthy:
        #for key in slef.sickness::
        self.sickness["healthy"] = is_healthy
    #def health(self):

    def sick(self):
        """Caught sick if stat is low enough """
        for sickness in sickness_list:
            sickness_stat = sickness_list[sickness][0]
            stat_value = self.get_stat(sickness_stat)
            if sickness_stat == "weight":
                if sickness_stat > 50:#fatty
                    if stat_value > sickness_stat:
                        self.sickness[sickness] = True
                    #if stat_value > sickness_stat
                #if sickness_stat > 50:
                else:
                    if stat_value < sickness_stat:
                        self.sickness[sickness] = True
                    #if stat_value < sickness_stat:
                #else:
            #if sickness_stat == "weight":
            elif stat_value < sickness_stat:
                self.sickness[sickness] = True
            #elif sickness_stat < get_stat(sickness_stat):
        #for sickness in sickness_list:
        is_healthy = True
        for key in slef.sickness:
            if key != healthy:
                if self.sickness[key] == False :
                    healthy = False
                    break
                #if self.sickness[key]:
            #if key != healthy:
        #for key in slef.sickness::
        self.sickness["healthy"] = is_healthy
    #def sick(self):

    def eat(self,aliment_name ):
        """Eat a given aliment to restore energy, health and increase weight """
        aliment_satiety, aliment_happyness, aliment_weight = aliment_list[aliment_name]
        score = {"satiety": aliment_satiety,"happyness": aliment_happyness,"weight": aliment_weight}
    #def eat(self,aliment ):

    def sleep(self):
        """A method to restore tamagotchi exercise"""
        score = {"energy" : 10}
        self.modify_stat(score)
    #def_sleep(self):

    def pass_time(self,time):
        """Take a number and go forward in time in minute   """
        for x in range(0,time):
            for stat_name in self.stat_regen:
                new_stat = self.get_stat(stat_name) + self.stat_regen[stat_name]
                self.set_stat(stat_name,new_stat)
                self.stat["age"] += 0.000046 #getting old
            #for x in range(0,time):
        #for stat_name
    #END_def
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
    
    def save(self):
        """ Save the game """
        identity = dict.fromkeys(self.statKey)
        for key in identity
           identity[key] = self.get_value(key)
        identity["Name"] = self.name
  
        with open('save', 'wb') as fichier:
            my_pickler = pickle.Pickler(fichier)
            my_pickler.dump(identity)
    #def save(self)
    
    def load_game(self):
        """ OBVIOUSLY """
        with open('save', 'rb') as fichier:
            my_depickler = pickle.Unpickler(fichier)
            identity = my_depickler.load()
            
            for key, value in identity.items():
                self.set_stat(key,value)
            
            
    #def load_game
    
#class Tamagotchi:
