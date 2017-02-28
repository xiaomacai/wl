# coding: utf-8
"""
db model文件
"""
from . import db
from flask_login import UserMixin
from . import loginManager


class Load(db.Model):
    __tablename__ = 'loads'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    start_node_id = db.Column(db.INTEGER)
    end_node_id = db.Column(db.INTEGER)
    length = db.Column(db.FLOAT)


class Node(db.Model):
    """
    地图点坐标
    """
    __tablename__ = 'nodes'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.TEXT)
    longitude = db.Column(db.FLOAT, nullable=False)  # 经度
    latitude = db.Column(db.FLOAT, nullable=False)   # 纬度


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(64))


@loginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))






