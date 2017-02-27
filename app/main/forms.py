# coding: utf-8
"""
表单
"""
from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField, StringField
from wtforms.validators import DataRequired



class LoadForm(FlaskForm):
    start_node = StringField(u'始点', validators=[DataRequired()])
    end_node = StringField(u'终点', validators=[DataRequired()])
    submit =SubmitField(u'提交')