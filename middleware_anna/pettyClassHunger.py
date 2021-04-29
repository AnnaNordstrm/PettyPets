import time
from deltatime import delta_time
from get_time import *
"""
Parameters:
name - The name of the animal
birth - A function that saves the time of birth
"""
class Pet :
    def __init__ (self, name, birth):
        self.name = name
        self.birth = birth
        self.foodLevel = 40
        self.lastFed = birth


    """
    Purpose: Takes in if user tries to feed the pet.
    Parameters:
    tryFeed: Boolean
    Returns: an updated self.foodLevel
    """
    def food_level(self, tryFeed):
        deltatime = delta_time(Lemmy.lastFed)[0]
        self.foodLevel = self.foodLevel-(0.05*deltatime)
        if self.foodLevel >= 70 & tryFeed:
            feed = False
            mood = 'happy'
        elif self.foodLevel > 0 & tryFeed:
            self.foodLevel = self.foodLevel + 30
            feed = True
            mood = 'happy'
        elif self.foodLevel < 30:
            mood = 'angry'
        elif self.foodLevel < 0:
            mood = 'dead'

        #return [self.foodLevel, mood, feed]
        return self.foodLevel


    def age():
        pass

#_______________________________________________________________________________
Lemmy = Pet("Lemmy", current_time())

print(Lemmy.foodLevel)

Lemmy.food_level(True)

print(Lemmy.foodLevel)

time.sleep(65)
print ("what about now?")
Lemmy.food_level(True)
print(Lemmy.foodLevel)
