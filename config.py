import os

# set up base directory of application - help computer figure out file system and where to find the diff pieces of project
basedir=os.path.abspath(os.path.dirname(__name__))

class Config:
    #set configuration variables for entire flask app
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY')