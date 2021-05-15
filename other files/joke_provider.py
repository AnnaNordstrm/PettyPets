import json
from random import randint

def jokeProvider ():
    """
    Purpose: Pick a joke from punchline.dat and buildup.dat.
    Returns: A list consisting of two strings, in which
    the first item is the buildup, the second is the punchline. 
    """
    #first, pick out a random buildup:
    with open('buildup.dat') as buildups:
        buildup_data = buildups.read()
    
    buildup_js = json.loads(buildup_data) # this creates a dictionary of what is read in the dat-file.
    randNr = str(randint(1, len(buildup_js)))
    buildup = buildup_js[randNr] # picks out a random joke from the dictionary.

    #pick up the corresponding punchline:
    with open('punchline.dat') as punchlines:
        punchline_data = punchlines.read()

    punchline_js = json.loads(punchline_data)
    punchline = punchline_js[randNr]

    return [buildup, punchline]
    

# print(jokeProvider())
