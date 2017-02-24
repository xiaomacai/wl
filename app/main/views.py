# coding: utf-8
"""
视图函数文件
"""
from flask import render_template, redirect, url_for
from . import main
from .forms import NodeForm
from ..models import Node
from .. import db


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
    return render_template('maps2.html')

