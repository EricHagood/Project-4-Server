from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager

import models
from resources.locations import location

DEBUG = True
PORT = 8000



#Initializing an instance of the flask class
app = Flask(__name__)

@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


CORS(location, origins=['http://localhost:3000'], supports_credentials=True)


app.register_blueprint(location, url_prefix='/api/v1/locations')

#Runs the app
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)