# coding: utf-8
"""
db model文件
"""
from . import db


class Node(db.Model):
    """
    地图点坐标
    """
    __tablename__ = 'nodes'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.TEXT)
    longitude = db.Column(db.FLOAT)  # 经度
    latitude = db.Column(db.FLOAT)   # 纬度

