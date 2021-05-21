from random import randint
def joke_provider():
    """
    Purpose: Pick a joke from punchline.dat and buildup.dat.
    Returns: A list consisting of two strings, in which
    the first item is the buildup, the second is the punchline.
    """

    with open('buildup2') as buildups:
        lines = buildups.readlines()
        list=[]
        for i in lines:
            list.append(i)

    with open('punchline2') as punchline:
        lines = punchline.readlines()
        list1 = []
        for i in lines:
            list1.append(i)

    place = int(randint(0, len(list)-1))
    buildup = list[place]
    punchline = list1[place]

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


def jokestorer(build_up, punchline):
    # with open('buildup.dat') as buildups:
    #     buildup_data = buildups.readlines()
    # build_up = str(build_up)
    # punchline = str(punchline)
    # print(punchline)
    with open('buildup2','a') as buildups:
        buildups.write("\n" + build_up)



    with open('punchline2', 'a') as punchlines:
        punchlines.write("\n" + punchline)









