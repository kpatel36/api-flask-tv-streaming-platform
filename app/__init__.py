from flask import Flask
from config import Config

app = Flask(__name__)

# IMPORT BLUEPRINTS
# 1. FIRST BLUEPRINT - AUTH
from .auth.routes import auth 
# from auth folder routes, import auth variable created by instantiation



app.config.from_object(Config)



# create link of communication between blueprints and app
# aka register the blueprints
app.register_blueprint(auth)

# must go @ end
from. import routes