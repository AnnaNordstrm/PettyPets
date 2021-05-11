from flask import Flask, request, render_template, jsonify
import time
from deltatime import delta_time
from get_time import *
import thread

app = Flask(__name__)



class Pet :
        def __init__ (self):
            self.name = "Lemmy"
            self.timeOfBirth = current_time()
            self.foodLevel = 20
            self.lastFedCheck = current_time()
            self.mood = "angry"
            self.feed = False

        
        """
        Purpose: To make the object hungrier with time, and if right conditions: feeds the pet +30
        Parameters:
        tryFeed: Boolean, takes in whether user tries to feed the pet.
        Returns: an updated self, mood and feed
        """
        def food_level(self, tryFeed):                          
                                                                
            deltatime = delta_time(self.lastFedCheck)[0]             
            self.foodLevel = self.foodLevel-(3*deltatime)    
                                                                
            if self.foodLevel >= 70 and tryFeed:                
                self.feed = False
                self.mood = 'happy'
                self.lastFedCheck = current_time()                                
            elif self.foodLevel > 0 and tryFeed:
                self.foodLevel += 30
                self.feed = True
                self.mood = 'happy'
                self.lastFedCheck = current_time()
            elif self.foodLevel < 30 and self.foodLevel > 0:
                self.mood = 'angry'
                self.lastFedCheck = current_time()
            elif self.foodLevel <= 0:           
                self.mood = 'dead'
                self.lastFedCheck = current_time()              


pets = Pet()

def function(arg):
    while arg:
        a = pets.food_level(False)
        print(pets.foodLevel)
        time.sleep(3)
    

@app.route('/')
def sign_in():
    return render_template('home.html')

@app.route('/sign_up')
def sign_up():
    pass


@app.route('/home', methods=['GET','POST'])    #TODO: skriva in att koden får använda get och post på alla andra routes
def home():                                    #      delete the return at the beginnig
    text1 = request.form['text1']
    print (text1)
    if int(text1) == 1:
        pets[0]=Pet()                       
        result = {"message" : "pet is created in a list!"}
    elif int(text1) == 2:
        pets[0].food_level(True)
        result = {
            "Mood" : pets[0].mood,
            }          
    elif int(text1) == 3:
        result = {
            "Mood" : pets[0].mood,
        }
    

    return jsonify(esult=result)


@app.route('/jokes')
def jokes():
    pass


@app.route('/about')
def about():
    pass

@app.route('/sign_out')
def sign_out():
    pass


if __name__ == '__main__':
    app.run(debug=True)
    thread = Thread(target=function, args=(True))
    thread.start()
    thread.join()

