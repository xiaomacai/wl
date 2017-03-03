# coding: utf-8
"""
初始化
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask_login import LoginManager


from config import config

db = SQLAlchemy()
moment = Moment()
bootstrap = Bootstrap()
loginManager = LoginManager()
loginManager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)
    loginManager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .jQuery import jQuery as jQuery_blueprint
    app.register_blueprint(jQuery_blueprint, url_prefix='/jquery')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .map import map as map_blueprint
    app.register_blueprint(map_blueprint, url_prefix='/map')

    from .experiment import experiment as exp_blueprint
    app.register_blueprint(exp_blueprint, url_prefix='/experiment')

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app

