from flask import Flask
from flask_mongoengine import MongoEngine
from app.resource.resource import animal
from flask_cors import CORS
from mongoengine import connect, disconnect
from app.containers import Container

# import dnspython
import pymongo
import os

#from flask_marshmallow import Marshmallow

database = MongoEngine()
cors = CORS()


def create_app():

    app = Flask(__name__)

    # adicionar o container para dependency injector.
    container = Container()
    container.wire(packages=[__name__])
    app.container = container

    app.secret_key = os.getenv('SECRET_KEY') if os.getenv(
        'SECRET_KEY') is not None else os.urandom(32)
    #app.config["APPLICATION_ROOT"] = "/api"

    if os.getenv("FLASK_ENV") == "production":
        assert os.getenv(
            "MONGO_URI_PRODUCTION") != None, f"MONGO_URI_PRODUCTION VAR NOT DEFINED"

        MONGO_URI_PRODUCTION = os.getenv("MONGO_URI_PRODUCTION")

        app.config['MONGODB_SETTINGS'] = {
            'connect': 'false',
            'host': MONGO_URI_PRODUCTION
        }
    else:
        app.config['MONGODB_SETTINGS'] = {
            'db': 'local',
            'host': 'mongodb://localhost/local',
            "alias": "default",
        }

    cors.init_app(app)
    return app


def registre_blueprints(app):
    app.register_blueprint(animal)


def init_database(app):
    if os.getenv("FLASK_ENV") == "test":
        connection = connect('mongoenginetest', host='mongomock://localhost')
    else:
        database.init_app(app)


if __name__ == '__main__':
    app = Flask(__name__)
    app.run(debug=True)
