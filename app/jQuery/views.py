from . import jQuery
from ..models import Node
from flask import jsonify


@jQuery.route('/all_nodes')
def all_nodes():
    nodes = Node.query.all()

    nodes_str = ''
    for node in nodes:
        nodes_str += str(node.id) + ',' + str(node.longitude) + ',' + str(node.latitude)
        nodes_str += '-'
    return jsonify(result=nodes_str)

