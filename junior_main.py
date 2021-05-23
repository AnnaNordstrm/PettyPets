from flask import Flask, request, render_template, jsonify
from middleware_main import joke_provider, jokestorer, delta_time, current_time, Pet, user_store, user_load
import time
from datetime import datetime
import json
from random import randint
# from joker import joker


app = Flask(__name__)


pets = [Pet()]

@app.route('/', methods=['GET','POST'])
def sign_up():
    return render_template('sign_up_main.html')

@app.route('/namer', methods=['GET','POST'])
def namer():
    pets[0].pet_name = (request.form.get("pet_name"))
    pets[0].username = (request.form.get("username"))
    pets[0].password = (request.form.get("password"))
    user_store(pets[0].pet_name)
    return render_template('home_main.html', pet_name=pets[0].pet_name, username=pets[0].username)

@app.route('/sign-in', methods=['GET','POST'])
def sign_in():
    pets[0].username = (request.form.get("username"))
    pets[0].password = (request.form.get("password"))
    return render_template('sign_in_main.html')

@app.route('/login', methods=['GET','POST'])
def login():
    user_load()
    pets[0].username = (request.form.get("username"))
    pets[0].password = (request.form.get("password"))
    return render_template('home_main.html',pet_name=pets[0].pet_name, username=pets[0].username)

@app.route('/home', methods=['GET','POST'])
def home():
    return render_template('home_main.html', pet_name=pets[0].pet_name, username=pets[0].username)   #/home splittras till 2 routs, eftersom att vi inte vill att koden i /home_1 körs varje gång

@app.route('/home_1', methods=['GET','POST'])
# ska kallas från javascript
def home_1():
    button_check = request.form['user_action'] #kontrollerar om användare tryckt på knapp och kollar i så fall vilken
    joke = joke_provider()

    pets[0].feed = False                    # Nollställer feed så att den inte alltid förblir True. Annars kan djuret inte sova
    pets[0].sleep = False
    pets[0].petted = False

    if int(button_check) == 1:              # mat-knappen 
        pets[0].food_level(True)
        #pets[0].sleep_level(False)         #borde man kankse se till så att alla levels uppdateras oavsett.
        #pets[0].pet_level(False)
        print(pets[0].foodLevel)
    elif int(button_check) == 2:            # sova-knappen
        pets[0].sleep_level(True)
    elif int(button_check) == 3:            # sova-knappen
        pets[0].pet_level(True)
    else:
        pets[0].food_level(False)           # Ingen knapp: uppdaterar alla statusar utan att interagera med dem
        pets[0].pet_level(False)
        pets[0].sleep_level(False)

    result = {
        "Mood": pets[0].mood,
        "Feed": pets[0].feed,
        "Joke": joke,
        "Food_level": pets[0].foodLevel,
        "Sleep_level": pets[0].sleepLevel,
        "Sleep": pets[0].sleep,
        "pet": pets[0].petted,
        "button": button_check
        #
        #"buildup": joke["buildup"],
        #"punchline": joke["punchline"]
        #returneras True eller False beroende på om den äter eller inte
        # behöver implementera sleep och pet.
        }
    pets[0].lastFed = current_time()
    pets[0].lastSlept = current_time()
    pets[0].lastPet = current_time()
    return jsonify(result=result)

@app.route('/jokes', methods=['GET','POST'])
def jokes():
    build_up = request.form.get("build_up", False)
    punch_line = request.form.get("punch_line", False)
    if punch_line != False:
        jokestorer(build_up,punch_line)
    return render_template('jokes_main.html', pet_name=pets[0].pet_name, username=pets[0].username)

@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('about_main.html', username=pets[0].username)

@app.route('/sign-out', methods=['GET','POST'])
def sign_out():
    return render_template('sign_out_main.html')

if __name__ == '__main__':
    app.run(debug=True)

