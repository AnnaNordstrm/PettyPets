import time
from deltatime import delta_time
from get_time import *
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("kaosIndex.html")

@app.route('/join', methods=['GET','POST'])
def join():

    class Pet :
        def __init__ (self, name):
            self.name = name
            self.timeOfBirth = current_time()
            self.foodLevel = 40
            self.lastFed = current_time()
            self.mood = "angry"
            self.feed = False


        """
        Purpose: To make the object hungrier with time, and if right conditions: feeds the pet +30
        Parameters:
        tryFeed: Boolean, takes in whether user tries to feed the pet.
        Returns: an updated self, mood and feed
        """
        def food_level(self, tryFeed):                          #  Changes from refactoring: 
                                                                #         * deltatime -> defined within the method via class attribute self.lastfed
            deltatime = delta_time(self.lastFed)[0]             #         * foodLevel -> class attribute
            self.foodLevel = self.foodLevel-(0.05*deltatime)    #         * mood -> class attribute
                                                                #         * feed -> class attribute
            if self.foodLevel >= 70 and tryFeed:                #         * & -> "and", othervise py wont understand
                self.feed = False
                self.mood = 'happy'                                
            elif self.foodLevel > 0 and tryFeed:
                self.foodLevel += 30
                self.feed = True
                self.mood = 'happy'
            elif self.foodLevel < 30 and self.foodLevel > 0:
                self.mood = 'angry'
            elif self.foodLevel <= 0:           # When foodLevel is going below zero, mood will always 
                self.mood = 'dead'              # become angry and pet will never be dead.
                                                # Solution: interval on line 33.

        def sleep_level():
            pass



    text1 = request.form['text1']           # Är det månne här som input från html kopplas till python?
    user = Pet(text1)                       # Skapar en instans av klassen Pet
    user.food_level(False)                  # Kör food_level 


    result = {
    "Mood" : user.mood
    }
    return jsonify(esult=result)
if __name__ == '__main__':
    app.run(debug=True)

