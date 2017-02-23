# coding: utf-8
"""
配置文件
"""
import os
basedir = os.path.abspath(os.path.dirname(__name__))


class Config():
    SECRET_KEY = os.getenv('SECRET_KEY') or 'SE23dSVPOIU*&^*23e3r2A&'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI') or  \
                              'sqlite:///' + os.path.join(basedir, 'dev-data.sqlite')   # ‘sqlite:///’配置数据库文件位置


config = {
    'development': DevelopmentConfig,

    'default': DevelopmentConfig
}