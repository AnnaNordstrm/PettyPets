from flask import Flask, request, render_template, jsonify
from middleware_main import joke_provider, delta_time, current_time
import time
from datetime import datetime
import json
from random import randint
# from joker import joker
from joke_provider import jokeProvider

app = Flask(__name__)

class Pet:
   #  Class for the pet
   def __init__(self):
      self.name = "Lemmy"
      self.timeOfBirth = current_time()
      self.foodLevel = 30
      self.lastFed = current_time()
      self.mood = "angry"
      self.feed = False


   def food_level(self, tryFeed):
    """
    Purpose: To make the object hungrier with time, and if right conditions: feeds the pet +30
    Parameters:
    tryFeed: Boolean, takes in whether user tries to feed the pet.
    Returns: an updated self, mood and feed
    """
    deltatime = delta_time(self.lastFed)[0]
    self.foodLevel = self.foodLevel - (0.05 * deltatime)

    if self.foodLevel >= 70 and tryFeed:
        self.feed = False
        self.mood = 'happy'
    elif self.foodLevel > 0 and tryFeed:
        self.foodLevel += 30
        self.feed = True
        self.mood = 'happy'
    elif self.foodLevel < 30 and self.foodLevel > 0:
        self.mood = 'angry'
    elif self.foodLevel <= 0:
        self.mood = 'dead'

    def pet_level(self):
        pass

    def sleep_level(self):
        pass



pets = [Pet()]

@app.route('/', methods=['GET','POST'])
def sign_in():
    return render_template('sign_in_main.html')

@app.route('/sign-up', methods=['GET','POST'])
def sign_up():
    return render_template('sign_up_main.html')

@app.route('/namer', methods=['GET','POST'])
def namer():
    pets[0].name = (request.form.get("key"))
    return render_template('home_main.html', name=pets[0].name)

@app.route('/home', methods=['GET','POST'])
def home():
    return render_template('home_main.html', name=pets[0].name)   #/home splittras till 2 routs, eftersom att vi inte vill att koden i /home_1 körs varje gång


@app.route('/home_1', methods=['GET','POST'])
# ska kallas från javascript
def home_1():
    button_check = request.form['user_action'] #kontrollerar om användare tryckt på knapp och kollar i så fall vilken
    # Ändrade till att jokeProvider används //Ebba
    joke = jokeProvider()
    if int(button_check) == 1:
        pets[0].food_level(True)
    else:
        pets[0].food_level(False)
    result = {
        "Mood": pets[0].mood,
        "Feed": pets[0].feed,
        "Joke": joke
        # i o m att jokeProvider används är koden nedanför bortkommenterad // Ebba
        #"buildup": joke["buildup"],
        # "punchline": joke["punchline"]
        #returneras True eller False beroende på om den äter eller inte
        # behöver implementera sleep och pet.
        }
    return jsonify(status = result)




@app.route('/jokes', methods=['GET','POST'])
def jokes():
    build_up = request.form.get("build_up", False)
    punch_line = request.form.get("punch_line", False)
    print(build_up, punch_line)
    return render_template('jokes_main.html')

@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('about_main.html')

@app.route('/sign-out', methods=['GET','POST'])
def sign_out():
    return render_template('sign_in_main.html')

if __name__ == '__main__':
    app.run(debug=True)



"""
ANNAS GAMLA /home
@app.route('/home', methods=['GET','POST'])
def home():
    # text1 = request.form['text1']
    # print(text1)
    # if int(text1) == 1:
    #     pets[0] = Pet()
    #     result = {"message": "pet is created in a list!"}
    # if int(text1) == 2:
         pets[0].food_level(True)
         result = {
             "Mood": pets[0].mood,
         }
    # elif int(text1) == 3:
    #     result = {
    #         "Mood": pets[0].mood,
    #     }
    return render_template('home_main.html', jsonify(esult=result))
    # return jsonify(esult=result))
"""