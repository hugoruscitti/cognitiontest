from flask import Flask
from flask_peewee.db import Database

app = Flask(__name__)
app.config.from_object('config.Configuration')
db = Database(app)

import models

models.create_tables(db)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
