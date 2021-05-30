import time
from datetime import datetime
import json
from random import randint
import pickle

class Pet:
    #  Class for the pet
    def __init__(self):
        self.name = "Lemmy"
        self.sleepLevel = 20
        self.sleep = False
        self.lastSlept = current_time()
        self.timeOfBirth = current_time()
        self.foodLevel = 30
        self.petLevel = 7
        self.lastFed = current_time()
        self.mood = "angry"
        self.feed = False
        self.petted = False
        self.lastPet = current_time()

    def food_level(self, tryFeed):
        """
        Purpose: To make the object hungrier with time, and if right conditions: feeds the pet +30
        Parameters: 
        tryFeed: Boolean, takes in whether user tries to feed the pet.
        Returns: an updated self, mood and feed
        """
        deltatime = delta_time(self.lastFed)[0]
        self.foodLevel = self.foodLevel - (0.05 * deltatime)
        if not self.mood == "dead":
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


    def sleep_level(self, trySleep):
        if not self.mood == "dead": 
            deltatime = delta_time(self.lastFed)[0]
            self.sleep = False

            self.sleepLevel = self.sleepLevel - (0.035 * int(deltatime))

            if trySleep:
                if self.sleepLevel < 70:
                    self.sleep = True
                    self.sleepLevel = 50
                else:
                    self.sleep = False
            if self.sleepLevel < 30 and self.sleepLevel >0:
                self.mood = "angry"
        else:
            self.mood = "dead"


    def pet_level(self, tryPet):
        if not self.petLevel < 0:
#            self.mood = "dead"
            deltatime = delta_time(self.lastFed)[0]
            self.petLevel = self.petLevel - (0.05 * deltatime)
            if round(self.petLevel) == 100 and tryPet:
                self.petted = False
                self.mood = 'happy'
            elif tryPet and not self.mood == "dead":
                self.petLevel += 1
                self.petted = True
                self.mood = 'happy'
            if round(self.petLevel) < 3 and not self.mood == "dead":
                self.mood = 'angry'
        else:
            self.mood = "dead"


def joke_provider():
    """
    Purpose: Pick a joke from punchline2.txt and buildup2.txt.
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
    """
    Purpose: Takes the last update time, time now and returns the difference in minutes
    Parameters: last_update - a sequence of number, which tells the last time the pet's status has been updated.
    """

    last_feeding_time = current_time()
    now = str(current_time())
    last = str(last_update)
    temp_now = []
    temp_last = []

    for i in range(5):                                  # stores the time units in a list
        m = 2*i
        temp_last.insert(i, int(last[m]+last[m+1]))
        temp_now.insert(i, int((now[m]+now[m+1])))

    time_koefficients = [525948.766, 43829.0639, 1440, 60, 1]           # changes difference in time to minutes
    deltatime = 0

    for i in range(5):
        deltatime = deltatime + (temp_now[i]-temp_last[i])*time_koefficients[i]

    return deltatime, last_feeding_time

from datetime import datetime

def current_time():
    """
    Purpose: Gives current date on the form YYMMDDHHMM
    """

    time = str(datetime.now())          # Sets the variable time to current time in form of a string
    list_remove = (' ', ':', '-', '.')   # List of characters that will be removed from time
    time = time[2:]                     # Removes the first two numbers of the year
    for i in list_remove:
        time = time.replace(i,'')          # Removes items in list_remove

    time = round(int(time) / 100000000)     # Turns time to an integer and removes anything lower than seconds

    return time

def jokestorer(build_up, punchline):
    """
    Purpose: store a buildup and punchline provided by the user.
    Paramters: buildup- a string. punchline - a string.
    """
    with open('buildup2.txt','a') as buildups:
        buildups.write("\n" + build_up)

    with open('punchline2.txt', 'a') as punchlines:
        punchlines.write("\n" + punchline)


def user_store(pet_name, username, password):
    """
    Purpose: this function is called upon when creating a new account and pet at /namer.
    Returns: the newly created pet object to be used.
    """
    pet = Pet()
    pet.name = pet_name
    filehandler = open('pet_file.pickle', 'rb')
    petDictionary = {}
    petDictionary = pickle.load(filehandler)
    petDictionary[username] = [password, pet_name, pet]
    filehandler.close()

    filehandler = open('pet_file.pickle', 'wb')
    pickle.dump(petDictionary, filehandler)
    print(petDictionary[username])
    return pet


def user_load(username, password):
    """
    Purpose: checks to see if it's the correct login at /login. 
    Parameters: username - a string. password - a string.
    Returns: the pet associated with the account logged into.
    """
    print("user load is activated")
    filehandler = open('pet_file.pickle', 'rb')
    petDictionary = pickle.load(filehandler)
    print(petDictionary)
    if username in petDictionary:
        list_values = petDictionary[username]
        if list_values[0] == password:
            print("Correct login!")
            pet = list_values[2]
            print("Pet object", pet)
            return pet
        else:
            print("Wrong password!")
    else:
        print("Wrong username!")



def save_progress(username, pet_name, password, pet):
    """
    Purpose: save the current state of the pet, together with the account's 
    username, password and the pet's name, in pet_file.obj.
    Returns: -
    """
    
    filehandler = open('pet_file.pickle', 'rb')
    petDictionary = pickle.load(filehandler)
    petDictionary[username] = [password, pet_name, pet]
    filehandler.close()

    filehandler = open('pet_file.pickle', 'wb')

    pickle.dump(petDictionary, filehandler)
    print(petDictionary[username])
    return


