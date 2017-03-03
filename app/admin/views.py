from . import admin
from flask_login import login_required
from ..decorators import admin_required
from flask import render_template, jsonify, redirect, url_for, request
from ..models import User
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
    users = User.query.all()
    return render_template('admin/data.html')


@admin.route('/add_user')
def add_user():
    name = request.args.get('name')
    password = request.args.get('password')
    u = User(name=name, password=password)
    db.session.add(u)
    db.session.commit()
