# coding: utf-8
from . import map
from flask import render_template


@map.route('/nodes')
def nodes():
    return render_template('map/nodes.html')


@map.route('/loads')
def loads():
    return render_template('map/loads.html')