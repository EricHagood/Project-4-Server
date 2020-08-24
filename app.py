from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_login import LoginManager
from decouple import config


import models
from resources.locations import location
import os
DEBUG = True
# PORT = config('PORT')
PORT = int(os.environ.get("PORT", 8000))
if 'ON_HEROKU' in os.environ:
    print('\non heroku')
    models.initialize()


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




CORS(location, origins=['http://localhost:3000', 'https://infinite-oasis-43571.herokuapp.com/'], supports_credentials=True)
app.register_blueprint(location, url_prefix='/api/v1/locations')

#Runs the app
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)