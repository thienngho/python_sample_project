import json
from json2html import *
from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route('/sport')
def sport():
    with open('data/sport.json') as json_file:
        data = json.load(json_file)

    return json2html.convert(json = data['sport'])

@app.route('/truck')
def truck():
    with open('data/truck.json') as json_file:
        data = json.load(json_file)

    return json2html.convert(json = data['truck'])

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
