import time
from deltatime import delta_time
from get_time import *
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def join():
    
    class Pet :
        def __init__ (self, name):
            self.name = name
            self.timeOfBirth = current_time()
            self.foodLevel = 40
            self.lastFed = current_time()
            self.mood = 'angry'
            self.feed = False


        """
        Purpose: To make the object hungrier with time, and if right conditions: feeds the pet +30
        Parameters:
        tryFeed: Boolean, takes in whether user tries to feed the pet.
        Returns: an updated self, mood
        """
        def food_level(self, tryFeed):                          #  Changes from refactoring: 
                                                                #         * deltatime -> defined within the method via class attribute self.lastfed
            deltatime = delta_time(self.lastFed)[0]             #         * foodLevel -> class attribute
            self.foodLevel = self.foodLevel-(0.05*deltatime)    #         * mood -> class attribute
            if self.foodLevel >= 70 & tryFeed:                  #         * feed -> class attribute
                self.feed = False
                self.mood = 'happy'
            elif self.foodLevel > 0 & tryFeed:
                self.foodLevel = self.foodLevel + 30
                self.feed = True
                self.mood = 'happy'
            elif self.foodLevel < 30 and self.foodlevel > 0:
                self.mood = 'angry'
            elif self.foodLevel <= 0:           # When foodLevel is going below zero, mood will always 
                self.mood = 'dead'              # become angry and pet will never be dead.
                                                # Solution: interval on line 33.
    
            #return [self.foodLevel, mood, feed]
            return self.foodLevel, self.mood

    text1 = request.form['text1']
        #text2 = request.form['text2']
    anna = Pet(text1)
    ee = anna.food_level(True)
    """
        deltatime = datetime.now() - lastfeedingtime
        if deltatime!= 0:
            if int(text1):
                lastfeedingtime = datetime.now()

        belly = belly + int(text1)
        
        result = {
            "Result": join_args(text1, belly)
    """
    result = {
        "Result": text1+" is now this full : "+ str(ee[0])
            }
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)

