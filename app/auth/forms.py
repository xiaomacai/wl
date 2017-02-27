# coding: utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,BooleanField
from wtforms.validators import DataRequired


class LogIn(FlaskForm):
    name = StringField(u'用户名', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    rememberMe = BooleanField(u'保持登陆', default=False)
    submit = SubmitField(u'登陆')