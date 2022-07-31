from dht11.service.HumidityTemparetureService import startservice, stopservice
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


@app.route('/start/dht11/sensor', methods=['GET'])
def startsensor():
    startservice()
    return "Sensor has started"


@app.route('/stop/dht11/sensor', methods=['GET'])
def stopsensor():
    stopservice()


if __name__ == "__main__":
    app.run(debug=True)


