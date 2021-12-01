from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.scrapper.Scrapper import Scrapper

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

scrapper = Scrapper()
from app.controllers import default
from app.models import *