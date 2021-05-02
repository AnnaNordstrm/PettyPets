from random import randint


#_____________________________________________
buildUpsD = {}          # These dictionaries should probably be in the main program in our finished product
punchLinesD = {}
karmaPointsD = {}
#_____________________________________________



def jokeMaker (b,p):         #buildup, punchline, karma points
    """
    Purpose: Places each element of the joke in its datastorage place.
    Paramters: 
    b - the first, obligatory part of the userprovided joke input.
    p - the latter, optional part of the joke.
    Returns: None.
    """
    buildUpsD ["Buildup" + (str(len(buildUpsD)+1))] = b 
    punchLinesD ["Punchline" + (str(len(punchLinesD)+1))] = p 
    karmaPointsD ["Karma points" + (str(len(karmaPointsD)+1))] = 10 
                                            # Standardpoäng vid insättnig är just nu 10 


def jokeProvider ():
    """
    Purpose: Picks and gives out a random joke. 
    TODO: Should maybe be modified to pick more highly voted jokes more often
    Paramters: None
    Returns: A tuple consisting of two strings. 
    """
    randNr = randint(1, len(buildUpsD))
    buildUp = buildUpsD["Buildup" + str(randNr)]
    punchLine = punchLinesD["Punchline" + str(randNr)]
    karma = karmaPointsD["Karma points" + str(randNr)]

    return buildUp, punchLine

    
 #________________TESTCODE____________________________#

jokeMaker("Orange you glad", "to see me!")
jokeMaker("AA", "BB")


print(jokeProvider())
print(jokeProvider())