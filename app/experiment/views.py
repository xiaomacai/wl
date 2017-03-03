# coding: utf-8
from . import experiment
from ..models import Load, ShortestPath, Node
from flask import jsonify


@experiment.route('/experiment_data')
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

