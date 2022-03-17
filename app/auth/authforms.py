from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo



class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    first_name = StringField ('First Name')
    last_name = StringField('Last Name')
    password = StringField('Password', validators=[DataRequired()])
    confirm_password=StringField('Confirm Password', validators=[EqualTo('password')])
    # EqualTo validator wants you to pass in value of password variable as a string
    # won't accept the submission unless the two are equivalent values
    submit = SubmitField()



class SignInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField()