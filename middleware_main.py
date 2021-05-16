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








