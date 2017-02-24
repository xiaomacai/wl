# coding: utf-8
"""
视图函数文件
"""
from flask import render_template, redirect, url_for, jsonify, request
from . import main
from .forms import NodeForm
from ..models import Node
from .. import db
import json


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


@main.route('/maps')
def maps():
    nodes = Node.query.all()
    ns = ''
    for node in nodes:
        ns += str(node.longitude) + ',' + str(node.latitude)
        ns += '-'
    return render_template('maps2.html', ns=ns)


@main.route('/save_node')
def save_node():
    name = request.args.get('name')
    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')

    node = Node(name=name, longitude=longitude, latitude=latitude)

    import sqlite3
    try:
        db.session.add(node)
        db.session.commit()
    except sqlite3.IntegrityError:
        pass
    nodes = Node.query.all()
    return redirect(url_for('main.maps'))


@main.route('/delete_node/')
def delete_node():
    lng = request.args['lng']
    lat = request.args['lat']
    node = Node.query.filter_by(longitude=lng, latitude=lat).first()
    if node is not None:
        db.session.delete(node)
    nodes = Node.query.all()
    return redirect(url_for('main.nodes'))

