# coding: utf8
from . import jQuery
from ..models import Node, Load
from flask import jsonify, request
from .. import db


@jQuery.route('/all_nodes')
def all_nodes():
    nodes = Node.query.all()

    nodes_list = dict()
    for node in nodes:
        nodes_list[node.id] = ({
            'longitude': node.longitude,
            'latitude': node.latitude,
            'name': node.name
        })
    return jsonify(result=nodes_list)


@jQuery.route('/all_loads')
def all_loads():
    loads = Load.query.all()

    loads_list = []
    for load in loads:
        loads_list.append((load.start_node_id, load.end_node_id, load.id, load.length, load.flow))
    return jsonify(result=list(set(loads_list)))


@jQuery.route('/add_node')
def add_node():
    lng = float(request.args.get('lng'))
    lat = float(request.args.get('lat'))
    address = request.args.get('address')

    node = Node(longitude=lng, latitude=lat, name=address)
    db.session.add(node)

    return all_nodes()


@jQuery.route('/add_load')
def add_load():
    s_id = int(request.args.get('start_node_id'))
    e_id = int(request.args.get('end_node_id'))
    length = float(request.args.get('length'))
    load1 = Load(start_node_id=s_id, end_node_id=e_id, length=length)
    load2 = Load(start_node_id=e_id, end_node_id=s_id, length=length)
    db.session.add(load1)
    db.session.add(load2)
    db.session.commit()
    return jsonify(result=1)


@jQuery.route('/remove_node')
def remove_node():
    id = int(request.args.get('id'))

    # 删除带有该节点的道路
    loads = Load.query.filter_by(start_node_id=id).all()
    for load in loads:
        db.session.delete(load)

    loads = Load.query.filter_by(end_node_id=id).all()
    for load in loads:
        db.session.delete(load)

    nodes = Node.query.filter_by(id=id).all()
    for node in nodes:
        db.session.delete(node)

    db.session.commit()
    return jsonify(result=1)


@jQuery.route('/remove_load')
def remove_load():
    s_id = int(request.args.get('start_node_id'))
    e_id = int(request.args.get('end_node_id'))

    loads = Load.query.filter_by(start_node_id=s_id, end_node_id=e_id).all()

    for load in loads:
        db.session.delete(load)

    loads = Load.query.filter_by(start_node_id=e_id, end_node_id=s_id).all()

    for load in loads:
        db.session.delete(load)

    db.session.commit()
    return jsonify(result=1)

