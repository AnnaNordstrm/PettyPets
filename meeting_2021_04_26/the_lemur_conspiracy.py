class Lemur:
    def  __init__(self, name):
        self.name = name
        self.age = 0
        self.poopyness = 40                                       # on a scale where 0 = good and 100 = bad.
        self.hunger = 40
        self.sleepyness = 0
        self.scritchyness = 40                                    # Is treated by petting the lemur
        self.loneliness = 40                                        # Is treated by telling jokes to the lemur
        self.mood = (self.poopyness + self.hunger + self.sleepyness + self.scritchyness + self.loneliness)//5    
        
    def setMood(self):
        self.mood = (self.poopyness + self.hunger + self.sleep + self.scritchyness + self.loneliness)//5    

    def poop (self):
        self.poopyness = 0
        
    def feed (self):
        self.hunger = 0
        
    def getSleep (self):
        self.sleepyness = 0    
        
    def scritches (self):
        self.scritchyness = 0
        
    def joke (self): 
        setup = input("Setup: ")
        punchline = input ("Punchline: ")
        self.loneliness = 0
        print(setup, punchline)
        return (setup,punchline)
    
"""
TODO: 
1.  En funktion som får djuret att säga ett skämt när dess "Mood" är bra (lågt)
2.  En Webb-knapp som initialiserar en ny instans
3.  En tidräknare som ser till att alla statusar går ner med tiden.
"""

jokebank = {}
joke = tester.joke()
jokebank.joke()




