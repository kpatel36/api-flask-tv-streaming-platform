# this run.py rile gives my terminal and flask shell access to components of app, letting me test via CLI and not worrying about templates or routes

# when you want to do testing through flask shell with this context processor change your FLASK_APP variable in .env to run.py

#imports
from app import app
from app.models import db, TelevisionSeries

# shell context processor - which gives my flask 'shell' (mini terminal with access to my flask app) access to my database models, etc

@app.shell_context_processor
def shell_context():
    return {'db': db, 'TelevisionSeries': TelevisionSeries}

    # id = db.Column(db.String(50), primary_key=True)
    # show_title = db.Column(db.String(150), nullable=False)
    # seasons = db.Column(db.Integer)
    # mpaa_rating = db.Column(db.String(10)) 
    # genre = db.Column(db.String(50), nullable=False)
    # network = db.Column(db.String(50))
    # language = db.Column(db.String(50))
    # status = db.Column(db.String(50))
    # description = db.Column(db.String(250))

    # def __init__(self,dict):
    #     self.id=str(uuid4())
    #     self.title=dict['title'].title()
    #     self.seasons=dict['seasons']
    #     self.mpaa_rating=dict['MPAA rating'].upper()
    #     self.genre =dict['genre'].title()
    #     self.network=dict['network']
    #     self.language=dict['language'].title()
    #     self.status=dict['status'].title()
    #     self.description= dict['description']

    # # function to translate object to dictionary
    # # role here is take self and return dict containing K:V pairs for each attribute
    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'title':self.title, 
    #         'seasons':self.seasons,
    #         'mpaa_rating':self.mpaa_rating,
    #         'genre':self.genre,
    #         'network':self.network,
    #         'language':self.network,
    #         'status':self.status,
    #         'description':self.description