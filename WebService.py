#!flask/bin/python
from logic import Logic
from flask_cors import CORS, cross_origin
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
CORS(app)

@app.route('/Text', methods=['GET'])
def Text():
    return jsonify({
    "opening":'<br/>'.join(Logic.OpeningSpiel()),
    "numberOfHeroes":Logic.NumberOfHeroesText()
    })

@app.route('/Generate', methods=['POST'])
def Generate():
    content = request.get_json()
    heroes = Logic.GetHeroes(int(content['numberOfHeroes']))
    ship = Logic.GetShip()
    threat = Logic.GetThreat()
    return jsonify({
        "heroes": '<br/>'.join(heroes),
        "ship": '<br/>'.join(ship),
        "threat": threat
    })

if __name__ == '__main__':
    app.run(debug=True)
