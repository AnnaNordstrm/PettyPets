import time
from datetime import datetime
import json
from random import randint

class Pet:
   #  Class for the pet
   def __init__(self):
      self.name = "Lemmy"
      self.sleepLevel = 20
      self.sleep = False
      self.lastSlept = current_time()
      self.timeOfBirth = current_time()
      self.foodLevel = 30
      self.lastFed = current_time()
      self.mood = "angry"
      self.feed = False


   def food_level(self, tryFeed):
    """
    Purpose: To make the object hungrier with time, and if right conditions: feeds the pet +30
    Parameters:
    tryFeed: Boolean, takes in whether user tries to feed the pet.
    Returns: an updated self, mood and feed
    """
    deltatime = delta_time(self.lastFed)[0]
    self.foodLevel = self.foodLevel - (0.05 * deltatime)

    if self.foodLevel >= 70 and tryFeed:
        self.feed = False
        self.mood = 'happy'
    elif self.foodLevel > 0 and tryFeed:
        self.foodLevel += 30
        self.feed = True
        self.mood = 'happy'
    elif self.foodLevel < 30 and self.foodLevel > 0:
        self.mood = 'angry'
    elif self.foodLevel <= 0:
        self.mood = 'dead'

    def pet_level(self):
        pass

   """
   ALLT DET HÄR ÄR EN GAMMAL VERSION AV SLEEP_LEVEL. PROBLEMET MED DEN VAR ATT GIFARNA INTE HADE SPELATS UPP PGA DENNA FUNKTION.
   DÄRFÖR ANVÄNDS EN BETYDLIGT ENKLARE SLEEP_LEVEL JUST NEDANFÖR.

   def sleep_level(self, trySleep):
      deltatime = delta_time(self.lastFed)[0]
      self.sleep = False

      self.sleepLevel = self.sleepLevel - (0.035 * int(deltatime))
      if trySleep:
         if self.sleepLevel < 50:
            print(self.sleepLevel, ", less than 50")
            self.sleep = True
         else:
            self.sleep = False
      if self.sleepLevel < 0:

         self.sleep = True

      if self.sleep:
         while self.sleepLevel < 100:
            #self.sleepLevel = self.sleepLevel + 0.24 * int(deltatime)
            self.sleepLevel = 100 #just nu maxas sleepLevel direkt då den får sova. Ska ändras?
            self.sleep = False     
      print(self.sleepLevel,", at the end of the function")
      #return sleepLevel, sleep
   """

   def sleep_level(self, trySleep):
      deltatime = delta_time(self.lastFed)[0]
      self.sleep = False

      self.sleepLevel = self.sleepLevel - (0.035 * int(deltatime))
      
      if trySleep:
         if self.sleepLevel < 50:
            self.sleep = True
            self.sleepLevel = 10
         else:
            self.sleep = False
      if self.sleepLevel < 0:
         self.sleep = True

      """
      if self.sleep:
         while self.sleepLevel < 100:
            #self.sleepLevel = self.sleepLevel + 0.24 * int(deltatime)
            self.sleepLevel = 100 #just nu maxas sleepLevel direkt då den får sova. Ska ändras?
            self.sleep = False     
      print(self.sleepLevel,", at the end of the function")
      #return sleepLevel, sleep
      """


"""
def joke_provider():

   Purpose: Pick a joke from punchline.dat and buildup.dat.
   Returns: A list consisting of two strings, in which
   the first item is the buildup, the second is the punchline.


   # first, pick out a random buildup:
   with open('buildup.dat') as buildups:
      buildup_data = buildups.read()

   buildup_js = json.loads(buildup_data)  # this creates a dictionary of what is read in the dat-file.
   randNr = str(randint(1, len(buildup_js)))
   buildup = buildup_js[randNr]  # picks out a random joke from the dictionary.

   # pick up the corresponding punchline:
   with open('punchline.dat') as punchlines:
      punchline_data = punchlines.read()

   punchline_js = json.loads(punchline_data)
   punchline = punchline_js[randNr]

   return [buildup, punchline]

# print(joke_provider())
"""
def joke_provider():
    """
    Purpose: Pick a joke from punchline.dat and buildup.dat.
    Returns: A list consisting of two strings, in which
    the first item is the buildup, the second is the punchline.
    """

    with open('buildup2.txt') as buildups:
        lines = buildups.readlines()
        list=[]
        for i in lines:
            list.append(i)

    with open('punchline2.txt') as punchline:
        lines = punchline.readlines()
        list1 = []
        for i in lines:
            list1.append(i)

    place = int(randint(0, len(list)-1))
    buildup = list[place]
    punchline = list1[place]

    return [buildup, punchline]


def delta_time (last_update):
   # Takes the last feeding time, time now and returns the difference in minutes

    last_feeding_time = current_time()
    now = str(current_time())
    last = str(last_update)
    temp_now = []
    temp_last = []

    for i in range(5):                                  # lagrar tidsenheterna i lista
        m = 2*i
        temp_last.insert(i, int(last[m]+last[m+1]))
        temp_now.insert(i, int((now[m]+now[m+1])))

    time_koefficients = [525948.766, 43829.0639, 1440, 60, 1]           # allt blir i sekunder
    deltatime = 0

    for i in range(5):
        deltatime = deltatime + (temp_now[i]-temp_last[i])*time_koefficients[i]

    return deltatime, last_feeding_time

from datetime import datetime

def current_time():
   # Gives current date on the form YYMMDDHHMM

    time = str(datetime.now())          # Sets the variable time to current time in form of a string
    list_remove = (' ', ':', '-', '.')   # List of characters that will be removed from time
    time = time[2:]                     # Removes the first two numbers of the year
    for i in list_remove:
        time = time.replace(i,'')          # Removes items in list_remove

    time = round(int(time) / 100000000)     # Turns time to an integer and removes anything lower than seconds

    return time

def jokestorer(build_up, punchline):

   with open('buildup2.txt','a') as buildups:
      buildups.write("\n" + build_up)



   with open('punchline2.txt', 'a') as punchlines:
      punchlines.write("\n" + punchline)



pet = [Pet()]
pet[0].sleep_level(True)


