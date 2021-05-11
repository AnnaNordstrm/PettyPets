# Flask is a web application framework

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def sign_in():
    return render_template('sign_in_isabelle.html')

@app.route('/sign-up')
def sign_up():
    return render_template('sign_up_isabelle.html')

@app.route('/home')
def home():
    return render_template('home_isabelle.html')

@app.route('/jokes')
def jokes():
    return render_template('jokes_isabelle.html')

@app.route('/about')
def about():
    return render_template('about_isabelle.html')

@app.route('/sign-out')
def sign_out():
    return render_template('sign_out_isabelle.html')

if __name__ == '__main__':
    app.run(debug=True)
