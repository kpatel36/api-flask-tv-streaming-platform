from flask import Flask
from config import Config

app = Flask(__name__)

# IMPORT BLUEPRINTS
# 1. FIRST BLUEPRINT - AUTH
from .auth.routes import auth 
from .tvapi.routes import api
# from auth folder routes, import auth variable created by instantiation

# imports for our database stuff
from .models import db
from flask_migrate import Migrate

app.config.from_object(Config)



# create link of communication between blueprints and app
# aka register the blueprints
app.register_blueprint(auth)
app.register_blueprint(api)

# set up our ORM and Migrate connections
db.init_app(app) 
migrate = Migrate(app,db) #variable 'migrate' is equal to instance of class 'Migrate' which will utilize both our database and our app


# must go @ end - comes after the ORM and migration setups
from . import routes
from . import models # from the app folder import the routes file