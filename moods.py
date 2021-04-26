import animation

def mood(emotion, isHungry=False, isSleepy=False, isLonely=False):
    """
    Purpose: If at least one of the pet's needs (sleep, food, social interaction) is
    not fullfilled, the pet will become angry. Else, it will be happy. These two emotions
    will be displayed through animations by animation.py.
    Paramters: 
    emotion - a string describing the current emotion.
    isHungry - a boolean value. If it's hungry, it's True, else it's False.
    isSleepy - same as above except for sleepiness.
    isLonely - same as above except for loneliness.
    Returns: ? not sure what it should return, if anything at all.
    """
    if isHungry == True:
        #if it was happy to begin with but now is hungry, change the mood.
        if emotion == "happy":
            emotion = "angry"
            animation.regular(emotion, new_mood = True)
        #in case the pet is already angry, we don't need to start the
        #angry animation over again.
        elif emotion == "angry":
            pass

    elif isSleepy == True:
            if emotion == "happy":
                emotion = "angry"
                animation.regular(emotion, new_mood = True)
            elif emotion == "angry":
                pass
    
    elif isLonely == True:
        if emotion == "happy":
            emotion = "angry"
            animation.regular(emotion, new_mood = True)
        emotion = "angry"
    
    else: #if its needs are fulfilled
        if emotion == "angry":
            emotion = "happy"
            animation.regular(emotion, new_mood = True)
        elif emotion == "happy": #if it was already happy to begin with
            pass
