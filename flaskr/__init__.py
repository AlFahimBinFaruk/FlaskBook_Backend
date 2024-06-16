import os
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson import json_util
import json

mongo = PyMongo()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY"),
        MONGO_URI=os.environ.get("MONGO_URI"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # initializing Database configuration
    mongo.init_app(app)

    # a simple page that says hello
    @app.get('/')
    def hello():
        from .db_models.User import User
        nw = User("fahim", "doe2", "do2e@gmail.com", "33333")
        nw.save()
        return 'Hello, World!'

    return app
