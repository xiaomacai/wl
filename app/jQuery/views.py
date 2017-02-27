from . import jQuery
from ..models import Node
from flask import jsonify


@jQuery.route('/all_nodes')
def all_nodes():
    nodes = Node.query.all()

    nodes_list = []
    for node in nodes:
        nodes_list.append({
            'id': node.id,
            'longitude': node.longitude,
            'latitude': node.latitude,
            'name': node.name
        })
    return jsonify(result=nodes_list)

