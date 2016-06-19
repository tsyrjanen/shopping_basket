import os
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.sqla  import ModelView



app = Flask(__name__)
app.secret_key = 'some_secret'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:paskamopo@localhost/webshop'
app.config['SQLALCHEMY_ECHO'] = True
Session(app)
db = SQLAlchemy(app)

#from app import models, api
import models
import api

db.create_all()
db.session.commit()


