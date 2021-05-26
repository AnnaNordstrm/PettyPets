from flask import Flask, request, render_template, jsonify
from middleware_main import joke_provider, jokestorer, delta_time, current_time, Pet, user_store, user_load, save_progress
import time
from datetime import datetime
import json
from random import randint


app = Flask(__name__)

user_name = ''
password = ''
pets = None

@app.route('/', methods=['GET','POST'])
def sign_up():
    return render_template('sign_up_main.html')

@app.route('/namer', methods=['GET','POST']) #is used when signing up, thus creating a new pet
def namer():
    global user_name
    global password
    pet_name = (request.form.get("pet_name"))
    user_name = (request.form.get("username"))
    password = (request.form.get("password"))
    global pets 
    pets = user_store(pet_name, user_name, password)
    return render_template('home_main.html', pet_name=pet_name, username=user_name)

@app.route('/sign-in', methods=['GET','POST'])
def sign_in():
    return render_template('sign_in_main.html')

@app.route('/login', methods=['GET','POST'])
def login():
    global user_name #these have to be declared as globals just as in /namer, in case a user just logs in (and therefore skips /namer).
    global password
    global pets
    user_name = (request.form.get("username"))
    password = (request.form.get("password"))
    try:
        pets = user_load(user_name, password)
        return render_template('home_main.html',pet_name=pets.name, username=user_name) # andra argumentet brukade vara pet_name=pets[0].name
    except:
        return render_template('sign_in_main.html', message="Username or password was incorrect!")

@app.route('/home', methods=['GET','POST'])
def home():
    return render_template('home_main.html', pet_name=pets.name, username=user_name)   #/home splittras till 2 routs, eftersom att vi inte vill att koden i /home_1 körs varje gång

@app.route('/home_1', methods=['GET','POST'])
# ska kallas från javascript
def home_1():
    #pets = normal_load() #doesn't have to be used, but I'm keeping it just to be safe for now.
    button_check = request.form['user_action'] #kontrollerar om användare tryckt på knapp och kollar i så fall vilken
    joke = joke_provider()

    pets.feed = False                    # Nollställer feed så att den inte alltid förblir True. Annars kan djuret inte sova
    pets.sleep = False
    pets.petted = False

    if int(button_check) == 1:              # mat-knappen 
        pets.food_level(True)
        pets.sleep_level(False)         #borde man kankse se till så att alla levels uppdateras oavsett.
        pets.pet_level(False)
    elif int(button_check) == 2:            # sova-knappen
        pets.sleep_level(True)
        pets.food_level(False)
        pets.pet_level(False)
    elif int(button_check) == 3:            # sova-knappen
        pets.pet_level(True)
        pets.food_level(False)
        pets.sleep_level(False)
    else:
        pets.food_level(False)           # Ingen knapp: uppdaterar alla statusar utan att interagera med dem
        pets.pet_level(False)
        pets.sleep_level(False)

    result = {
        "Mood": pets.mood,
        "Feed": pets.feed,
        "Joke": joke,
        "Food_level": pets.foodLevel,
        "Sleep_level": pets.sleepLevel,
        "Sleep": pets.sleep,
        "pet": pets.petted,
        "button": button_check
        }
    pets.lastFed = current_time()
    pets.lastSlept = current_time()
    pets.lastPet = current_time()

    save_progress(user_name, pets.name, password, pets)

    return jsonify(result=result)

@app.route('/jokes', methods=['GET','POST'])
def jokes():
    build_up = request.form.get("build_up", False)
    punch_line = request.form.get("punch_line", False)
    if punch_line != False:
        jokestorer(build_up,punch_line)
    return render_template('jokes_main.html', pet_name=pets.name, username=user_name)

@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('about_main.html', username=user_name)

@app.route('/sign-out', methods=['GET','POST'])
def sign_out():
    save_progress(user_name, pets.name, password, pets)
    return render_template('sign_out_main.html')

if __name__ == '__main__':
    app.run(debug=True)

