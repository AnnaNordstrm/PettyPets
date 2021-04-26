
from flask import Flask, request, render_template, jsonify
from middleware import join_args

app = Flask(__name__)

def food_level(tryFeed, deltatime, foodLevel):
#Takes in if user tries to feed the pet, time in mins since last feeding and its foodlevel.
#It returns

    foodLevel = foodLevel-(0.05*deltatime)
    if foodLevel >= 70 & tryFeed:
        feed = False
        mood = 'happy'
    elif foodLevel > 0 & tryFeed:
        foodLevel = foodLevel + 30
        feed = True
        mood = 'happy'
    elif foodLevel < 30:
        mood = 'angry'
    elif foodLevel < 0:
        mood = 'dead'

    #return [foodLevel, mood, feed]
    return foodLevel

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def join():
    #text1 = request.form['text1']
    #text2 = request.form['text2']
    result = {
        #help
    }
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
