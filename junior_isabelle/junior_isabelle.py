from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home_isabelle.html')

if __name__ == '__main__':
    app.run(debug=True)
