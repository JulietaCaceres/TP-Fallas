from random import choice
from selector import *
from flask import Flask
from flask import request
from flask import render_template
from flask import send_file
import os

app = Flask(__name__)


def response_to_boolean(response):
    return True if response == "SI" else False


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/encuesta", methods=['GET', 'POST'])
def encuesta():
    return render_template('init.html')


@app.route("/resulta", methods=['GET', 'POST'])
def resultado():
    return render_template('response.html')

@app.route("/handle_data", methods=['GET', 'POST'])
def handle_data():
    sexo = request.args.get('sexo')
    print("-----------------------entro aca con sexo: {}".format(sexo))
    embarazo_actual = response_to_boolean(request.args.get('embarazo_actual'))
    embarazo_planificado = response_to_boolean(request.args.get('embarazo_planificado'))
    metodo_anticonceptivo = request.args.get('metodo_anticonceptivo')
    enfermedad_patologica = response_to_boolean(request.args.get('enfermedad_patologica'))
    controlada = response_to_boolean(request.args.get('controlada'))
    examen_fisico = request.args.get('examen_fisico')

    print(f"""
    Params
            sexo = {sexo}
            embarazo_actual = {embarazo_actual}
            embarazo_planificado = {embarazo_planificado}
            metodo_anticonceptivo = {metodo_anticonceptivo}
            enfermedad_patologica = {enfermedad_patologica}
            controlada = {controlada}
            examen_fisico = {examen_fisico}
    """)

    expert_engine = Selector()
    expert_engine.reset()
    voluntarie = Voluntarie(
                            sexo=Sexo(sexo),
                            embarazo_actual=embarazo_actual,
                            embarazo_planificado=embarazo_planificado,
                            metodo_anticonceptivo=MetodoAnticonceptivo(metodo_anticonceptivo),
                            enfermedad_patologica=enfermedad_patologica,
                            controlada=controlada,
                            examen_fisico=examen_fisico)
    expert_engine.declare(voluntarie)
    expert_engine.run()
    print(expert_engine.response)
    return render_template('response.html', packages=expert_engine)


if __name__ == "__main__":
    app.run(debug=True)
