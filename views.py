from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from flask import session
from app import app
import models


@app.route('/', methods=['GET', 'POST'])
def ingresar():
    if request.method == 'POST':
        persona = models.Persona(edad=request.form['edad'],
                sexo=request.form['sexo'],
                estado_civil=request.form['estado_civil'],
                respuesta=3)

        try:
            persona.save()
        except ValueError:
            flash("Por favor complemente correctamente el formulario.", "danger")
            return render_template('persona/new.html')

        session['persona_id'] = persona.id
        return redirect('/aviso')

    return render_template('persona/new.html')

@app.route('/aviso')
def aviso_pre_video():
    return render_template('aviso_pre_video.html')

@app.route('/video')
def ver_video():
    return render_template('video.html', video_url="/static/videos/campeon.mp4")

@app.route('/cuestionario', methods=['GET', 'POST'])
def ver_cuestionario():
    if request.method == 'POST':
        try:
            persona_id = session['persona_id']
            persona = models.Persona.get(id=persona_id)
            persona.respuesta = request.form['respuesta']
            persona.save()
            return redirect('/terminado')
        except ValueError:
            flash("Por favor complemente correctamente el formulario.", "danger")
            return render_template('persona/cuestionario.html')
        except KeyError:
            flash("No puede regresar en el asistente, vuelva a comenzar...", "danger")
            return render_template('persona/cuestionario.html')

    return render_template('persona/cuestionario.html')

@app.route("/terminado")
def terminado():
    session.pop('persona_id', None)
    return render_template('terminado.html')

@app.route('/resultados')
def resultados():
    personas = models.Persona.select()
    return render_template('persona/resultados.html', personas=personas, values="[['Han seleccionado BAJO suelo', 30], ['Han seleccionado ALTO sueldo',70]]")
