from flask import render_template
from flask import request
from flask import redirect
from app import app
import models

@app.route('/')
def home():
    users = models.User.select()
    return render_template('home.html', users=users)

@app.route('/usuarios/new', methods=['GET', 'POST'])
def usuarios_new():
    print "usuarios"
    if request.method == 'POST':
        user = models.User(nombre=request.form['nombre'])
        user.save()
        return redirect('/')

    return render_template('usuarios/new.html')

@app.route('/usuarios/edit/<int:user_id>', methods=['GET', 'POST'])
def usuario_editar(user_id):
    user = models.User.get(id=user_id)

    if request.method == 'POST':
        user.nombre = request.form['nombre']
        user.save()
        return redirect('/')

    return render_template('usuarios/edit.html', usuario=user)
