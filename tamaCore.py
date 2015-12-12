
class Tamagotchi(object):
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

        ~ stat('hunger'): float //Tamagotchi actual level of food 0-X

        ~ stat('statKey'): dict //(age,expectancy,weight,cleanness,happyness,exercise,hunger)

        ----------------------------Method-------------------------------

        + eat(string aliment): void

        + play(): void

        + wash(): void

        + heal(): void

        + sleep(): void

        + die(): void

        ~ _get_sick (string sickness): void

        + watch_stats(): void

        + _get_stat(string stat ): float/string(depend on the stat)

		+ pass_time(int time): void

		+ modify_stat(int stat[])

		+ __repr__(): void
    """
​
        def __init__(self):
            """initialise all the stat of a tamagotchi"""
            self.name = "Tamagotchi"
            self.health = {} # /!\ need to be initialisate
            self.health["healthy"] = true
            statKey = ('age','expectancy','weight','cleanness','happyness','exercise','hunger')
            self.stat_max = dict.fromkeys{statKey,0.0}
            self.stat_degen = dict.fromkeys{statKey,0.0}
            self.stat = dict.fromkeys(statKey,0.0)
        #END_def

        def modify_stat(score):
            """
                Take a table (weight,cleanness,happyness,exercise,hunger),
                and "add" it to the stat
            """
            for key in score
                self.stat[key] = score[key]
        #END_def

        def play():
            """A method to make the tamagotchi play"""
            #score = miniGamePlay()
            score = {'weight' = -2,'happyness' = -5,'hunger' = -3,'exercise' = -5}
            modify_stat(score);
        #END_def
        def wash():

            """a method to wash the tamagotchi,mainly increase his cleanness"""
            #score = miniGameWash()
            score = {'cleanness' = 10,'happyness' = -5}
            modify_stat(score);
        #END_def

        #def heal():
            #"""a method who remove all curable sickness"""
            #END_def

        def sleep():
            """A method to restore tamagotchi exercise"""
                score = {"exercise" = 10}
                modify_stat(score);
#END_CLASS
