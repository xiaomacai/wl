# coding: utf-8
"""
表单
"""
from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField, StringField, TextAreaField
from wtforms.validators import DataRequired


class LoadForm(FlaskForm):
    start_node = StringField(u'始点', validators=[DataRequired()])
    end_node = StringField(u'终点', validators=[DataRequired()])
    submit = SubmitField(u'提交')


class FeedBackForm(FlaskForm):
    road_name = StringField(u'路段名称')
    content = TextAreaField(u'问题')
    submit = SubmitField(u'反馈')


class FeedBack2Form(FlaskForm):
    road_name = StringField(u'路段名称')
    jindu = StringField(u'施工经度')
    finished_time = StringField(u'预计结束时间')
    content = TextAreaField(u'问题')
    submit = SubmitField(u'反馈')