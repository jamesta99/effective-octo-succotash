import os

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))
blog_app = Flask(__name__)
blog_app.config.from_mapping(
   SECRET_KEY = 'TREECS_YEK',
   SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'blog_app.db'),
   SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(blog_app)

from blog_app import routes, models
