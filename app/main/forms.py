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
    road_name = StringField(u'路段名称', validators=[DataRequired()])
    content = TextAreaField(u'问题', validators=[DataRequired()])
    submit = SubmitField(u'反馈')


class FeedBack2Form(FlaskForm):
    road_name = StringField(u'路段名称', validators=[DataRequired()])
    jindu = StringField(u'施工经度', validators=[DataRequired()])
    finished_time = StringField(u'预计结束时间', validators=[DataRequired()])
    content = TextAreaField(u'问题', validators=[DataRequired()])
    submit = SubmitField(u'反馈')


class FeedBack3Form(FlaskForm):
    start_node_id = StringField(u'路段始点', validators=[DataRequired()])
    end_node_id = StringField(u'路段终点', validators=[DataRequired()])
    qixian = StringField(u'施工期限', validators=[DataRequired()])
    zhouqi = StringField(u'施工周期', validators=[DataRequired()])
    submit = StringField(u'提交')
