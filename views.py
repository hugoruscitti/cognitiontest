from flask import render_template
from app import app
import models

@app.route('/')
def home():
    users = models.User.select()
    return render_template('home.html', users=users)

@app.route('/usuarios/new')
def usuarios_new():
    return render_template('usuarios/new.html')
