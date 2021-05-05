from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# app.route "/" används för startsidan för tillfället (ska användas till att logga in egentligen)
# def sign_in

@app.route('/')
def home():
    return render_template('home_isabelle.html')

# Skapa app.route "/sign_up" för att skapa konto
# def sign_up

# Skapa app.route "/home" för startsidan
# def home

# Skapa app.route "/jokes" för skämtsidan
# def jokes

# Skapa app.route "/about" för information om projektet
# def about

# Skapa app.route "/sign_out" för utloggningssidan
# def sign_out

if __name__ == '__main__':
    app.run(debug=True)
