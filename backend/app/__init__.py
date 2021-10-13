from flask import Flask
from flask_mongoengine import MongoEngine
from app.resource.resource import animal

database = MongoEngine()


def create_app():
    app = Flask(__name__)
    app.secret_key = "SECRET_KEY"
    #app.config["APPLICATION_ROOT"] = "/api"
    app.config['MONGODB_SETTINGS'] = {
        'db': 'local',
        'host': 'mongodb://localhost/local'
    }
    app.register_blueprint(animal)

    return app


def init_database(app):
    database.init_app(app)


if __name__ == '__main__':
    app = Flask(__name__)
    app.run(debug=True)
