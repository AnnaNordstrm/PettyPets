
from datetime import datetime

def food_level(tryFeed, deltatime, foodLevel):
#Takes in if user tries to feed the pet, time in mins since last feeding and its foodlevel.
#It returns

    foodLevel = foodLevel-(0.05*deltatime[0])
    if foodLevel >= 70 & tryFeed:
        feed = False
        mood = 'happy'
    elif foodLevel > 0 & tryFeed:
        foodLevel = foodLevel + 30
        feed = True
        mood = 'happy'
    elif foodLevel < 30:
        mood = 'angry'
    elif foodLevel < 0:
        mood = 'dead'

    #return [foodLevel, mood, feed]
    return foodLevel



def current_time():
    # Gives current date on the form YYMMDDHHMM
    time = str(datetime.now())   # Sets the variable time to current time in form of a string
    list_remove = (' ', ':', '-', '.')   # List of characters that will be removed from time
    time = time[2:]  # Removes the first two numbers of the year
    for i in list_remove:
        time = time.replace(i,'')  # Removes items in list_remove

    time = round(int(time) / 100000000)  # Turns time to an integer and removes anything lower than seconds

    return time




#from get_time import current_time

def delta_time(last_update):
    # Takes the last feeding time, time now and returns the difference in minutes
    last_feeding_time = current_time()
    now = str(current_time())
    last = str(last_update)
    temp_now = []
    temp_last = []

    for i in range(5):
        m = 2*i
        temp_last.insert(i, int(last[m]+last[m+1]))
        temp_now.insert(i, int((now[m]+now[m+1])))

    time_koefficients = [525948.766, 43829.0639, 1440, 60, 1]
    deltatime = 0

    for i in range(5):
        deltatime = deltatime + (temp_now[i]-temp_last[i])*time_koefficients[i]

    return deltatime, last_feeding_time





def join_args():
   combine = food_level(True, delta_time(2104261400), 40)
   return combine