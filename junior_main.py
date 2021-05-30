from flask import Flask, request, render_template, jsonify
from middleware_main import joke_provider, jokestorer, current_time, user_store, user_load, save_progress



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
        return render_template('home_main.html',pet_name=pets.name, username=user_name)
    except:
        return render_template('sign_in_main.html', message="Username or password was incorrect!")

@app.route('/home', methods=['GET','POST'])
def home():
    return render_template('home_main.html', pet_name=pets.name, username=user_name) #home_main.html is split up into two routes, because we do not want the code in /home_1 to be run at all times

@app.route('/home_1', methods=['GET','POST'])
# this route is called through ajax in javascript.
def home_1():
    
    button_check = request.form['user_action'] #checks to see if an interaction button has been pressed by the user.
    joke = joke_provider()

    pets.feed = False                    
    pets.sleep = False
    pets.petted = False

    if int(button_check) == 1:              # if feed button has been pressed
        pets.food_level(True)
        pets.sleep_level(False)         
        pets.pet_level(False)
    elif int(button_check) == 2:            # if sleep button has been pressed
        pets.sleep_level(True)
        pets.food_level(False)
        pets.pet_level(False)
    elif int(button_check) == 3:            # if pet button has been pressed
        pets.pet_level(True)
        pets.food_level(False)
        pets.sleep_level(False)
    else:
        pets.food_level(False)           # No button has been pressed.
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

