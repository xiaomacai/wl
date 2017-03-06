# coding: utf-8
from flask import render_template, redirect, url_for, flash
from .forms import LogIn, SignUp, EditInformation
from . import auth
from ..models import User
from flask_login import login_user, login_required, logout_user, current_user
from ..decorators import admin_required
from .. import db


@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LogIn()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data, password=form.password.data).first()
        if user is not None:
            login_user(user)
            return redirect(url_for('main.index'))
        flash(u'登陆失败')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/signup')
def signup():
    form = SignUp()
    if form.validate_on_submit():
        return redirect(url_for('main.index'))
    return render_template('auth/signup.html', form=form)


@auth.route('/user/<name>')
def user(name):
    user = User.query.filter_by(name=name).first()
    return render_template('auth/user.html', user=user)


@auth.route('/edit_information', methods=['GET', 'POST'])
def edit_information():

    form = EditInformation()
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.name = form.name.data
        current_user.sex = form.sex.data
        current_user.location = form.location.data
        current_user.age = form.age.data
        db.session.add(current_user)
        db.session.commit()
        return redirect(url_for('auth.user', name=current_user.name))
    form.email.data = current_user.email
    form.name.data = current_user.name
    form.sex.data = current_user.sex
    form.age.data = current_user.age
    form.location.data = current_user.location
    return render_template('auth/edit_information.html', form=form)





