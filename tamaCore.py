
class Tamagotchi:
    """The core class who describe a tamagotchi(the animal)

    ------------------------atribute----------------------------------
    ~ name: string

    ~ age: float

    ~ expectancy: float // Life time expetency

    ~ health: Dict(bollean) // a table of bolean with all the sick
                                    as key (or,if not sick only "healthy")

    ~ stat_degen: Dict(degen) // a table of stat degen with a stat as key

    ~ stat_max: Dict(max) // a table of stat degen with a stat as key

    ~ stat: Dict(stat) // a table with a statname as key and a statvalue as value

    ~ stat('weight'): float //Tamagotchi actual weight

    ~ stat('cleanness'): float //Tamagotchi actual level of cleanness 0-X

    ~ stat('happyness'): float //Tamagotchi actual level of happyness 0-X

    ~ stat('exercise'): float //Tamagotchi actual level of exercise 0-X

    ~ stat('satiety'): float //Tamagotchi actual level of food 0-X

    ~ stat('statKey'): dict //(age,expectancy,weight,cleanness,happyness,exercise,hunger)

    ----------------------------Method-------------------------------

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


   """

    def __init__(self):
        """initialise all the stat of a tamagotchi"""
        self.name = "Tamagotchi"
        self.sickness = dict.fromkeys(sickness_list.keys(),False) # /!\ need to be initialisate
        self.sickness["healthy"] = True
        self.statKey = ('age','expectancy','weight',\
                        'cleanness','happyness','exercise','hunger')
        self.stat_max = dict.fromkeys(statKey,100.0)
        self.stat_degen = dict.fromkeys(statKey,0.0)
        self.stat = dict.fromkeys(statKey,0.0)
    #def___init__(self)

    def modify_stat(self,score):
        """
            Take a Dict of stat (weight,cleanness,happyness,exercise,hunger),
            with modifier as value and "add" it to the stat
        """
        for key in score:
            self.stat[key] = score[key]
        #def for key in score:
    #def_modify_stat(self,score)

    def get_stat(self,stat_name):
        """Return the value of a stat by his name //get_stat(stat_name)"""
        return self.stat(stat_name)
    #def get_stat(self,stat_name):

    def play(self):
        """A method to make the tamagotchi play"""
        #score = miniGamePlay()
        score = {'weight': -2,'happyness': -5,'hunger': -3,'exercise': -5}
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
                if sickness_stat > stat_value - 10:
                    self.sickness[sickness_stat] = False
                #if sickness_stat < get_stat(sickness_stat)
            #if sickness_stat == "weight":

            if sickness_stat < stat_value + 10:
                self.sickness[sickness_stat] = False
            #if sickness_stat < get_stat(sickness_stat):
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
    #def heal(self,stat_name):

    def sleep(self):
        """A method to restore tamagotchi exercise"""
        score = {"exercise" : 10}
        self.modify_stat(score)
    #def_sleep(self)



#END_CLASS
