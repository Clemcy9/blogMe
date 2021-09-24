from operator import imod
from flask_wtf import FlaskForm
# from flask_wtf.recaptcha import validators
from wtforms import StringField
from wtforms import validators
from wtforms.fields.core import BooleanField
from wtforms.fields.simple import PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from flaskblog.models import User
from flask_login import current_user
from flask_wtf.file import FileField, file_allowed

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(message='pls input correct email')])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            # print('username taken')
            raise ValidationError('That username has been taken')
    
    def validate_email(self,email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            # print('email taken')
            raise ValidationError('That email is taken')
            

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(message='pls input correct email')])
    picture = FileField('Update Profile Pic', validators=[file_allowed(['jpg','png'])])
    submit = SubmitField('Update')

    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                # print('username taken')
                raise ValidationError('That username has been taken')
        
    def validate_email(self,email):
         if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()
            if email:
                # print('email taken')
                raise ValidationError('That email is taken')
                

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content',validators=[DataRequired()])
    submit = SubmitField('Post')