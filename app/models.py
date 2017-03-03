# coding: utf-8
"""
db model文件
"""
from . import db
from flask_login import UserMixin
from . import loginManager
from random import randint
from datetime import datetime


class Load(db.Model):
    __tablename__ = 'loads'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    start_node_id = db.Column(db.INTEGER)
    end_node_id = db.Column(db.INTEGER)
    length = db.Column(db.FLOAT)             # 路段长度
    flow = db.Column(db.FLOAT)               # 路段交通流量
    fwed_flow = db.Column(db.FLOAT)          # 经过fw分配后的交通流量
    free_flow_time = db.Column(db.FLOAT)     # 自由流时间
    travel_time = db.Column(db.FLOAT)        # 路段旅行时间
    control_type = db.Column(db.INTEGER)     # 管制类型（2为全管制，1为局部管制,默认为0 不管制）
    control_start_time = db.Column(db.DATETIME)     # 管制开始时间（默认为当前时间)
    control_end_time = db.Column(db.DATETIME)       # 管制结束时间，默认为当前时间)

    def __init__(self, **kwargs):
        super(Load, self).__init__(**kwargs)
        if self.length is not None:
            self.flow = randint(1000, 3000)
            self.travel_time = self.length / 60
            self.control_type = 0
            self.control_start_time = datetime.utcnow()
            self.control_end_time = datetime.utcnow()

    @staticmethod
    def insert_flow():
        loads = Load.query.all()
        for load in loads:
            load.flow = randint(1000, 3000)
            db.session.add(load)
        db.session.commit()

    @staticmethod
    def insert_travel_time():
        loads = Load.query.all()
        for load in loads:
            load.travel_time = load.length / 50
            db.session.add(load)
        db.session.commit()

    @staticmethod
    def insert_free_flow_time():
        from data import free_flow_time
        for k, v in free_flow_time.iteritems():
            for k2, v2 in v.iteritems():
                load = Load.query.filter_by(start_node_id=int(k), end_node_id=int(k2)).first()
                load.free_flow_time = v2
                db.session.add(load)
        db.session.commit()

    @staticmethod
    def insert_fwed_flow():
        from data import fwed_flows
        for k, v in fwed_flows().iteritems():
            for k2, v2 in v.iteritems():
                load = Load.query.filter_by(start_node_id=int(k), end_node_id=int(k2)).first()
                load.fwed_flows = v2
                db.session.add(load)
        db.session.commit()


class ShortestPath(db.Model):
    """
    最短路径表
    """
    id = db.Column(db.INTEGER, primary_key=True)
    start_node_id = db.Column(db.INTEGER)
    end_node_id = db.Column(db.INTEGER)
    path_time = db.Column(db.FLOAT)     # 正常情况下通过该路段需要时间
    path = db.Column(db.String(128))    # 最短路径‘1-2-3-4’表示从1到4的最短路为1234

    @staticmethod
    def init_path():
        from data import shortest_paths
        for item in shortest_paths():
            path = ShortestPath(start_node_id=int(item[0]), end_node_id=int(item[-2]))
            path.path_time = item[-1]
            path.path = '-'.join(item[:-1])
            db.session.add(path)
        db.session.commit()


class Node(db.Model):
    """
    地图点坐标
    """
    __tablename__ = 'nodes'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.TEXT)
    longitude = db.Column(db.FLOAT, nullable=False)  # 经度
    latitude = db.Column(db.FLOAT, nullable=False)   # 纬度

    pd = db.Column(db.INTEGER)  # 节点周围人口密集程度


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(64))


@loginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))






