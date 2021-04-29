
from flask import Flask, request, render_template, jsonify
from middleware import join_args, food_level, delta_time, current_time
#from deltatime import delta_time

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def join():
    #text1 = request.form['text1']
    #text2 = request.form['text2']

    hunger = food_level(True, delta_time(2104272200), 50)
    result = {
        "result": hunger
 
    }
    print(hunger)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
