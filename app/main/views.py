# coding: utf-8
from ..models import Permission, FeedBack, FeedBack2, FeedBack3
from flask import render_template, redirect, url_for
from flask_login import current_user, login_required
from . import main
from .forms import FeedBackForm, FeedBack2Form, FeedBack3Form
from .. import db

"""
视图函数文件
"""


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


@main.route('/release_news')
def release_news():
    return render_template('release_news.html')


@main.route('/feedback', methods=['GET', 'POST'])
@login_required
def feedback():
    if current_user.permissions == Permission.USER:
        form = FeedBackForm()
        if form.validate_on_submit():
            fb = FeedBack(user_id=current_user.id, road_name=form.road_name.data)
            fb.content = form.content.data
            db.session.add(fb)
        return render_template('feedback.html', form=form)
    elif current_user.permissions == Permission.GENERAT_MANAGER:
        form = FeedBack2Form()
        if form.validate_on_submit():
            fb = FeedBack2(user_id=current_user.id, road_name=form.road_name.data)
            fb.content = form.content.data
            fb.jindu = form.jindu.data
            fb.finished_time = form.finished_time.onupdate
            db.session.add(fb)
        return render_template('feedback.html', form=form)
    else:
        return redirect(url_for('main.index'))

