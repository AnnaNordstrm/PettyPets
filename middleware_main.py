# CLASSES AND FUNCTIONS IN THE PROGRAM

# Class for the pet

class Pet:
   def __init__(self):
      self.name = "Lemmy"
      self.timeOfBirth = current_time()
      self.foodLevel = 30
      self.lastFed = current_time()
      self.mood = "angry"
      self.feed = False

   """
   Purpose: To make the object hungrier with time, and if right conditions: feeds the pet +30
   Parameters:
   tryFeed: Boolean, takes in whether user tries to feed the pet.
   Returns: an updated self, mood and feed
   """

   def food_level(self, tryFeed):

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


pets = [Pet()]

# Function for jokes

def joke_provider():
   """
   Purpose: Pick a joke from punchline.dat and buildup.dat.
   Returns: A list consisting of two strings, in which
   the first item is the buildup, the second is the punchline.
   """
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
