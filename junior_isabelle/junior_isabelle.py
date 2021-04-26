from flask import Flask, request, render_template, jsonify
from middleware_main import join_args

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home_main.html')

@app.route('/join', methods=['GET','POST'])
def join():
    text1 = request.form['text1']
    text2 = request.form['text2']
    result = {
        "result": join_args(text1,text2)
    }
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
