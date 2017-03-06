# coding: utf-8
from . import admin
from flask_login import login_required
from ..decorators import admin_required
from flask import render_template, jsonify, redirect, url_for, request, jsonify
from ..models import User, Load, ShortestPath, Node
from .. import db


@admin.route('/')
@admin_required
def index():
    return render_template('admin/index.html')


@admin.route('/user')
@admin_required
def user():
    users = User.query.all()
    return render_template('admin/user.html', users=users)


@admin.route('/data')
@admin_required
def data():
    loads = Load.query.all()
    res = []
    for item in loads:
        res.append({'start_node_id': item.start_node_id, 'end_node_id': item.end_node_id,
                    'fwed_flow': int(item.fwed_flow), 'free_flow_time': item.free_flow_time,
                    'capacity': item.capacity, 'control_type': item.control_type})
    path = ShortestPath.query.all()
    res2 = []
    for item in path:
        res2.append({'start_node_id': item.start_node_id, 'end_node_id': item.end_node_id,
                    'path_time': item.path_time, 'path': item.path})

    return render_template('admin/data.html', result={'res': res, 'res2': res2})


@admin.route('/experiment_data')
@admin_required
def experiment_data():
    """

    :return:json数据格式的列表，每一项为包含开始节点、终止节点、fw处理后流量、自由流时间、路段通行能力、管制方式
    """
    loads = Load.query.all()
    res = []
    for item in loads:
        res.append({'start_node_id': item.start_node_id, 'end_node_id': item.end_node_id,
                    'fwed_flow': item.fwed_flow, 'free_flow_time': item.free_flow_time,
                    'capacity': item.capacity, 'control_type': item.control_type})

    return jsonify(result=res)


@admin.route('/opt_loads')
@admin_required
def opt_loads():
    return render_template('admin/opt_loads.html')


@admin.route('/opt_nodes')
@admin_required
def opt_nodes():
    return render_template('admin/opt_nodes.html')


@admin.route('/add_user')
def add_user():
    name = request.args.get('name')
    email = request.args.get('email')
    password = request.args.get('password')
    u = User(name=name, password=password, mail=email)
    db.session.add(u)
    db.session.commit()


@admin.route('/control_model')
@admin_required
def control_model():
    return render_template('admin/control_model.html')


@admin.route('/model_parameters')
@admin_required
def model_parameters():
    return render_template('admin/model_parameters.html')

