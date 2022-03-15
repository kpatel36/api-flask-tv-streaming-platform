# this page is for laying out objects for each of our forms
# these objects will describe the form fields, types of data and any validators

# imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired #if they arent submitting data, they cant submit the form

# class for the form describing the form's structure and datatypes
class ShowSearch(FlaskForm): #ShowSearch is customization of a form so we are going to want to inherit the base behavior provided by flask via FlaskForm
    #provide fields the form will show
    showname = StringField('Show Name', validators=[DataRequired()])
    submit = SubmitField()