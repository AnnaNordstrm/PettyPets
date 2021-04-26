
from flask import Flask, request, render_template, jsonify
from middleware import join_args
from datetime import datetime

belly = 5
lastfeedingtime = datetime.now()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def join():
    global belly
    global lastfeedingtime
    text1 = request.form['text1']
    #text2 = request.form['text2']
    deltatime = datetime.now() - lastfeedingtime
    if deltatime!= 0:
        if int(text1):
            lastfeedingtime = datetime.now()

    belly = belly + int(text1)
    
    result = {
        "result": join_args(text1, belly)
    }
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)


"""
line 35 in home.html:
            Last: <input type="text" id="text2"><br/>

"""
