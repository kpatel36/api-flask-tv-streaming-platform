 # models.py is responsible for everything database
 # primarily the instantiation of our ORM
 # and the creation of our database models (aka tables/entitites)

 # import our ORM
from flask_sqlalchemy import SQLAlchemy

# from datetime import datetime, timezone
# from werkzeug.security import generate_password_hash
from uuid import uuid4
# from secrets import token_hex
# 
# from flask_login import Login_Manager, User Mixin
#login =LoginManager()

#necessary function for our login manager
# @login.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

 # create the instance of our ORM (tranlator between python and SQL)
db = SQLAlchemy()

 # creation of our database model - essentially the python code for a SQL create table

 # create a class of whatever name we want the table to have
 # it's going to inherit from the SQLAlchemy database model class

class TelevisionSeries(db.Model):
    # lay out columns just like we would in a SQL create table query
    id = db.Column(db.String(50), primary_key=True)
    show_title = db.Column(db.String(150), unique=True )# nullable=False)
    seasons = db.Column(db.Integer)
    #mpaa_rating = db.Column(db.String(10)) 
    genre = db.Column(db.String(50)) #nullable=False)
    network = db.Column(db.String(50))
    language = db.Column(db.String(50))
    status = db.Column(db.String(50))
    description = db.Column(db.String(250))

    def __init__(self,dict):
        self.id=str(uuid4())
        self.show_title=dict['show_title'].title()
        self.seasons=dict['seasons']
        self.genre =dict['genre']
        self.network=dict['network']
        self.language=dict['language']
        self.status=dict['status']
        self.description= dict['description']

    # function to translate object to dictionary
    # role here is take self and return dict containing K:V pairs for each attribute
    def to_dict(self):
        return {
            'id': self.id,
            'show_title':self.show_title, 
            'seasons':self.seasons,
            'genre':self.genre,
            'network':self.network,
            'language':self.language,
            'status':self.status,
            'description':self.description
        }


    def from_dict(self,dict):
        """
        works for the updateSeries route - accepts dictionary provided by request and updates the info with any present keys
        if value is present in the update dict, then we update the associate value

        """
        if dict.get('show_title'):
            self.show_title=dict['show_title']
        if dict.get('seasons'):
            self.seasons=dict['seasons']
        if dict.get('genre'):
            self.genre=dict['genre']
        if dict.get('network'):
            self.network=dict['network']
        if dict.get('language'):
            self.show_title=dict['language']
        if dict.get('status'):
            self.status=dict['status']
        if dict.get('description'):
            self.description=dict['description']