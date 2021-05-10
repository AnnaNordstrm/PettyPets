from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

class Pet :
        def __init__ (self):
            self.name = "Lemmy"
            self.timeOfBirth = current_time()
            self.foodLevel = 20
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




@app.route('/')
def sign_in():
    return render_template('home_isabelle.html')

@app.route('/sign_up')
def sign_up():
    return render_template('home_isabelle.html')

@app.route('/home')
def home():
    return render_template('home_isabelle.html')

    text1 = request.form['text1']
    
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
    return render_template('home_isabelle.html')

@app.route('/about')
def about():
    return render_template('home_isabelle.html')

@app.route('/sign_out')
def sign_out():
    return render_template('home_isabelle.html')

if __name__ == '__main__':
    app.run(debug=True)
