# coding: utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,BooleanField
from wtforms.validators import DataRequired, EqualTo


class LogIn(FlaskForm):
    name = StringField(u'用户名', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    rememberMe = BooleanField(u'保持登陆', default=False)
    submit = SubmitField(u'登陆')


class SignUp(FlaskForm):
    name = StringField(u'用户名', validators=[DataRequired()])
    email = StringField(u'邮箱', validators=[DataRequired()])
    password = PasswordField(u'密码', validators=[DataRequired(), EqualTo('password2', u'两次密码不一致')])
    password2 = PasswordField(u'确认密码', validators=[DataRequired()])
    submit = SubmitField(u'注册')


class EditInformation(FlaskForm):
    name = StringField(u'用户名', validators=[DataRequired()])
    email = StringField(u'邮箱', validators=[DataRequired()])
    location = StringField(u'地址')
    sex = StringField(u'性别')
    age = StringField(u'年龄')
    submit = SubmitField(u'修改')

