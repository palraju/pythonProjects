from dht11.service.PingService import greeting
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


@app.route('/ping/app', methods=['GET'])
def ping():
    return "ping message";


if __name__ == "__main__":
    app.run(debug=True)
