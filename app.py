from flask import Flask, escape, request, send_file

app = Flask(__name__)

@app.route('/')
def hello():
    return send_file('index.html')

@app.route('/BitesOfTheBay')
def bay_bites():
    return send_file('bay_bites.html')

