from flask import Flask, jsonify, request
from os import environ

from flask_migrate import Migrate
from flask_script import Manager
from models import db

flaskr_api = Flask(__name__)

flaskr_api.config.from_object(environ.get('FHIR_ENV', 'config.Config'))

flaskr_api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(flaskr_api)
migrate = Migrate(flaskr_api, db)
manager = Manager(flaskr_api)

if __name__ == '__main__':
    flaskr_api.run(port=6000)
