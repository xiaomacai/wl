# coding: utf-8
"""
视图函数文件
"""
from flask import render_template, redirect, url_for, jsonify, request, flash
from . import main
from .forms import NodeForm, LoadForm
from ..models import Node, Load
from .. import db
import json
import sqlite3


def select_nodes():
    nodes = Node.query.all()
    ns = ''
    for node in nodes:
        ns += str(node.id) + ',' + str(node.longitude) + ',' + str(node.latitude)
        ns += '-'
    return ns


@main.route('/', methods=['POST', 'GET'])
def index():
    form = NodeForm()
    node = Node()
    if form.validate_on_submit():
        node.name = form.name.data
        node.longitude = form.longitude.data
        node.latitude = form.latitude.data
        db.session.add(node)
        return redirect(url_for('main.index'))
    form.name.data = node.name
    form.latitude.data = node.latitude
    form.longitude.data = node.longitude
    return render_template('index.html', form=form)


@main.route('/nodes')
def nodes():
    nodes = Node.query.all()
    return render_template('nodes.html', nodes=nodes)


@main.route('/js_nodes')
def js_nodes():
    return jsonify(result=select_nodes())


@main.route('/loads')
def loads():
    ns = select_nodes()
    return render_template('loads.html', ns=ns)


@main.route('/save_load')
def save_load():
    start_node = request.args.get('start_node')
    end_node = request.args.get('end_node')


@main.route('/maps')
def maps():
    ns = select_nodes()
    return render_template('maps2.html', ns=ns)


@main.route('/save_node')
def save_node():
    name = request.args.get('name')
    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')

    node = Node(name=name, longitude=longitude, latitude=latitude)
    try:
        db.session.add(node)
        db.session.commit()
    except sqlite3.IntegrityError:
        pass
    flash(u'添加成功')
    return redirect(url_for('main.maps'))


@main.route('/delete_node/')
def delete_node():
    id = request.args.get('id')
    if id is not None:
        node = Node.query.filter_by(id=id).first()
        if node is not None:
            db.session.delete(node)
        else:
            flash(u'编号为{}的节点不存在'.format(id))
        return redirect(url_for('main.maps'))
    else:
        lng = request.args['lng']
        lat = request.args['lat']
        node = Node.query.filter_by(longitude=lng, latitude=lat).first()
        if node is not None:
            db.session.delete(node)
    return redirect(url_for('main.nodes'))

