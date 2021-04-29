import time
from deltatime import delta_time
from get_time import *

"""
Parameters:
name - The name of the pet
"""
class Pet :
    def __init__ (self, name):
        self.name = name
        self.timeOfBirth = current_time()
        self.foodLevel = 40
        self.lastFed = current_time()


    """
    Purpose: To make the object hungrier with time
    Parameters:
    tryFeed: Boolean, takes in whether user tries to feed the pet.
    Returns: an updated self.foodLevel
    """
    def food_level(self, tryFeed):                          #  Changes from refactoring: 
                                                            #         * deltatime is now defined within the method via class attribute self.lastfed
        deltatime = delta_time(Lemmy.lastFed)[0]            #         * foodLevel is now a class attribute
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


#______________________________Testkod_________________________________________________
Lemmy = Pet("Lemmy", current_time())

print("Lemmys hungernivå när han föds: ",Lemmy.foodLevel)

Lemmy.food_level(True)

print("Lemmys hungernivå när man kör food_level() för första gången: ",Lemmy.foodLevel)

time.sleep(65)

Lemmy.food_level(True)
print("Lemmys hungernivå efter en minut: "Lemmy.foodLevel)
