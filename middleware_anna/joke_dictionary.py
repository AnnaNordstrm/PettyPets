from random import randint

buildUpsD = {}
punchLinesD = {}
karmaPointsD = {}

def jokeMaker (b,p):         #buildup, punchline, karma points
    buildUpsD ["Buildup" + (str(len(buildUpsD)+1))] = b 
    punchLinesD ["Punchline" + (str(len(punchLinesD)+1))] = p 
    karmaPointsD ["Karma points" + (str(len(karmaPointsD)+1))] = 10 
                                            # Standardpoäng vid insättnig är ust nu 10 


def jokeProvider ():
    randNr = randint(1, len(buildUpsD))
    buildUp = buildUpsD["Buildup" + str(randNr)]
    punchLine = punchLinesD["Punchline" + str(randNr)]
    karma = karmaPointsD["Karma points" + str(randNr)]

    print(buildUp)
    print(punchLine)

jokeMaker("Orange you glad", "to see me")

jokeProvider()