from flask import Flask
from flask_peewee.db import Database

app = Flask(__name__)
app.config.from_object('config.Configuration')
db = Database(app)
