# coding: utf-8
"""
表单
"""
from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField, StringField
from wtforms.validators import DataRequired


class NodeForm(FlaskForm):
    name = StringField(u'地名', validators=[DataRequired()])
    longitude = FloatField(u'经度', validators=[DataRequired()])
    latitude = FloatField(u'纬度', validators=[DataRequired()])
    submit = SubmitField(u'提交')


class LoadForm(FlaskForm):
    start_node = StringField(u'始点', validators=[DataRequired()])
    end_node = StringField(u'终点', validators=[DataRequired()])
    submit =SubmitField(u'提交')