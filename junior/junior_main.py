from flask import Flask, request, render_template, jsonify
import time
from deltatime import delta_time
from get_time import *

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def sign_in():
    return render_template('sign_in_main.html')

@app.route('/sign-up', methods=['GET','POST'])
def sign_up():
    return render_template('sign_up_main.html')

@app.route('/home', methods=['GET','POST'])
def home():
    text1 = request.form['text1']
    print(text1)
    if int(text1) == 1:
        pets[0] = Pet()
        result = {"message": "pet is created in a list!"}
    elif int(text1) == 2:
        pets[0].food_level(True)
        result = {
            "Mood": pets[0].mood,
        }
    elif int(text1) == 3:
        result = {
            "Mood": pets[0].mood,
        }
    return (render_template('home_main.html'), jsonify(esult=result))

@app.route('/jokes', methods=['GET','POST'])
def jokes():
    return render_template('jokes_main.html')

@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('about_main.html')

@app.route('/sign-out', methods=['GET','POST'])
def sign_out():
    return render_template('sign_out_main.html')

if __name__ == '__main__':
    app.run(debug=True)
