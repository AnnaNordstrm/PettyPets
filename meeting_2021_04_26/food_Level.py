
def food_level(tryFeed, deltatime, foodLevel):
#Takes in if user tries to feed the pet, time in mins since last feeding and its foodlevel.
#It returns

    foodLevel = foodLevel-(0.05*deltatime)
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
