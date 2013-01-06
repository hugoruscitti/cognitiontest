from flask import render_template
from app import app

def helper_pie(values, title="untitled", size=100):
    id = "123"
    size = int((400 / 100.0) * size)
    return render_template('pie.html', id=id, size=size, title=title, values=values)

def helper_sexo(valor):
    valores = {0: '',
               1: 'Masculino',
               2: 'Femenino'}
    return valores[valor]

def helper_estado_civil(valor):
    valores = {0: '',
               1: 'Soltero/a',
               2: 'Casado/a'}
    return valores[valor]

def helper_respuesta(valor):
    valores = {
            0: '',
            1: 'Alto sueldo, pero poca estabilidad laboral',
            2: 'Bajo sueldo, pero mayor estabilidad laboral',
            3: 'en curso...'}
    return valores[valor]

@app.context_processor
def helpers_personalizados():
    return {'sexo': helper_sexo, 'estado_civil': helper_estado_civil, 'pie': helper_pie, 'respuesta': helper_respuesta}
