# coding: utf-8
"""
db model文件
"""
from . import db


class Load(db.Model):
    __tablename__ = 'loads'
    id = db.Column(db.INTEGER, primary_key=True)
    start_node_id = db.Column(db.INTEGER, db.ForeignKey('nodes.id'), primary_key=True)
    end_node_id = db.Column(db.INTEGER, db.ForeignKey('nodes.id'), primary_key=True)
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





