import time
from deltatime import delta_time
from get_time import *


class Pet :
    def __init__ (self, name):
        self.name = name
        self.timeOfBirth = current_time()
        self.foodLevel = 40
        self.lastFed = current_time()
        self.mood = 'angry'
        self.feed = True


    """
    Purpose: To make the object hungrier with time
    Parameters:
    tryFeed: Boolean, takes in whether user tries to feed the pet.
    Returns: an updated self, mood
    """
    def food_level(self, tryFeed):                          #  Changes from refactoring: 
                                                            #         * deltatime -> defined within the method via class attribute self.lastfed
        deltatime = delta_time(Lemmy.lastFed)[0]            #         * foodLevel -> class attribute
        self.foodLevel = self.foodLevel-(0.05*deltatime)    #         * mood -> class attribute
        if self.foodLevel >= 70 & tryFeed:
            self.feed = False
            self.mood = 'happy'
        elif self.foodLevel > 0 & tryFeed:
            self.foodLevel = self.foodLevel + 30
            self.feed = True
            self.mood = 'happy'
        elif self.foodLevel < 30:
            self.mood = 'angry'
        elif self.foodLevel < 0:           # When foodLevel is going below zero, mood becomes angry instead of dead
            self.mood = 'dead'             # Solution: intervals?
 
        #return [self.foodLevel, mood, feed]
        return self.foodLevel, self.mood


#______________________________Testkod_________________________________________________
Lemmy = Pet("Lemmy")

print("Lemmys hungernivå när han föds: ",Lemmy.foodLevel)

Lemmy.food_level(True)
print(Lemmy.mood)

print("Lemmys hungernivå när man kör food_level() för första gången: ",Lemmy.foodLevel)

time.sleep(65)

Lemmy.food_level(True)
print("Lemmys hungernivå efter en minut: ", Lemmy.foodLevel)