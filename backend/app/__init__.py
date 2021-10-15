from flask import Flask
from flask_mongoengine import MongoEngine
from app.resource.resource import animal
from flask_cors import CORS
#from flask_marshmallow import Marshmallow

database = MongoEngine()
cors = CORS()


def create_app():
    app = Flask(__name__)
    app.secret_key = "SECRET_KEY"
    #app.config["APPLICATION_ROOT"] = "/api"
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
    database.init_app(app)


if __name__ == '__main__':
    app = Flask(__name__)
    app.run(debug=True)
