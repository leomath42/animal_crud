from flask import Flask
from flask_mongoengine import MongoEngine


def create_app():
    app = Flask(__name__)
    app.secret_key = "SECRET_KEY"
    app.config['MONGODB_SETTINGS'] = {
        'db': 'local',
        'host': 'mongodb://localhost/local',
        'connect': False
    }
    return app


def init_database(app):
    db = MongoEngine()
    db.init_app(app)


if __name__ == '__main__':
    app = Flask(__name__)
    app.run(debug=True)
