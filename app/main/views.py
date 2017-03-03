# coding: utf-8
from ..models import Permission

"""
视图函数文件
"""
from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/information')
def information():
    return render_template('road_control.html')


@main.app_context_processor
def inject_permissions():
    # 将Permission类引入上下文
    return dict(Permission=Permission)
