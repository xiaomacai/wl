# coding: utf-8
"""
视图函数文件
"""
from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html')