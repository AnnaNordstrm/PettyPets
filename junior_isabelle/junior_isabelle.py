from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# app.route "/" används för startsidan för tillfället (ska användas till att logga in egentligen)
@app.route('/')
def home():
    return render_template('home_isabelle.html')

# Skapa app.route "/sign_up" för att skapa konto

# Skapa app.route "/home" för startsidan

# Skapa app.route "/jokes" för skämtsidan

# Skapa app.route "/about" för information om projektet

# Skapa app.route "/sign_out" för utloggningssidan

if __name__ == '__main__':
    app.run(debug=True)
