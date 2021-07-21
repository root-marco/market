from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):

  def validate_username(self, username_param):
    user = User.query.filter_by(username=username_param.data).first()
    if user: raise ValidationError('username already exists')

  def validate_email(self, email_param):
    email = User.query.filter_by(email=email_param.data).first()
    if email: raise ValidationError('email already exists')

  username = StringField(label='username:',
    validators=[Length(min=2, max=30), DataRequired()])

  email = StringField(label='email:',
    validators=[Email(), DataRequired()])

  password1 = PasswordField(label='password:',
    validators=[Length(min=6), DataRequired()])

  password2 = PasswordField(label='confirm password:',
    validators=[EqualTo('password1'), DataRequired()])

  submit = SubmitField(label='sign up')


class LoginForm(FlaskForm):
  
  username = StringField(label='username:',
    validators=[DataRequired()])
  
  password = PasswordField(label='password:',
    validators=[DataRequired()])

  submit = SubmitField(label='sign in')
