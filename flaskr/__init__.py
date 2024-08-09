import os

from datetime import timedelta
from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

mongo = PyMongo()
bcrypt = Bcrypt()
jwt = JWTManager()

from .user import routes as user_routes
from .blog import routes as blog_routes
from .comment import routes as comment_routes
from .vote import routes as vote_routes


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("SECRET_KEY"),
        MONGO_URI=os.environ.get("MONGO_URI"),
        JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY"),
        JWT_ACCESS_TOKEN_EXPIRES=timedelta(days=7)

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

    # initializing database
    mongo.init_app(app)

    bcrypt.init_app(app)
    jwt.init_app(app)

    # Store bcrypt and jwt in the app context
    app.bcrypt = bcrypt
    app.jwt = jwt

    # initializing routes
    app.register_blueprint(user_routes.user_bp, url_prefix="/api/user/")
    app.register_blueprint(blog_routes.blog_bp, url_prefix="/api/blog/")
    app.register_blueprint(comment_routes.comment_bp, url_prefix="/api/comment/")
    app.register_blueprint(vote_routes.vote_bp, url_prefix="/api/vote/")

    # a simple page that says hello
    @app.get('/')
    def hello():

        return 'Hello, World!'

    return app
