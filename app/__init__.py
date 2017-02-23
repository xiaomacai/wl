# coding: utf-8
"""
初始化
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from config import config

db = SQLAlchemy()
moment = Moment()
bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)

    from .main import main as main_bluprint
    app.register_blueprint(main_bluprint)

    return app
