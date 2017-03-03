# coding: utf-8
from ..models import User
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    name = StringField(u'用户名', validators=[DataRequired()])
    password = StringField(u'密码', validators=[DataRequired()])

    permissions = IntegerField(u'权限', validators=[DataRequired()])


