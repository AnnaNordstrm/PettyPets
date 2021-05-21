from flask import Flask, request, render_template, jsonify
from middleware_main import joke_provider, delta_time, current_time, Pet
import time
from datetime import datetime
import json
from random import randint



app = Flask(__name__)


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
    joke = jokeProvider()

    pets[0].feed = False                    # Nollställer feed så att den inte alltid förblir True. Annars kan djuret inte sova
    pets[0].sleep =  False
    
    if int(button_check) == 1:              # mat-knappen 
        pets[0].food_level(True)
    elif int(button_check) == 2:            # sova-knappen
        pets[0].sleep_level(True)
    else:
        pets[0].food_level(False)           # Ingen knapp
    
    result = {
        "Mood": pets[0].mood,
        "Feed": pets[0].feed,
        "Joke": joke,
        "Food_level": pets[0].foodLevel,
        "Sleep_level": pets[0].sleepLevel,
        "Sleep": pets[0].sleep
        #
        #"buildup": joke["buildup"],
        #"punchline": joke["punchline"]
        #returneras True eller False beroende på om den äter eller inte
        # behöver implementera sleep och pet.
        }
    pets[0].lastFed = current_time()
    pets[0].lastSlept = current_time()
    return jsonify(result=result)




@app.route('/jokes', methods=['GET','POST'])
def jokes():
    build_up = request.form.get("build_up", False)
    punch_line = request.form.get("punch_line", False)
    if punch_line != False:
        jokestorer(build_up,punch_line)
    return render_template('jokes_main.html')

@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('about_main.html')

@app.route('/sign-out', methods=['GET','POST'])
def sign_out():
    return render_template('sign_in_main.html')

if __name__ == '__main__':
    app.run(debug=True)

