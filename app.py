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
    return render_template('init.html')


@app.route("/handle_data")
def handle_data():
    sexo = request.args.get('sexo')
    embarazo_actual = response_to_boolean(request.args.get('embarazo_actual'))
    embarazo_planificado = response_to_boolean(request.args.get('embarazo_planificado'))
    metodo_anticonceptivo = request.args.get('metodo_anticonceptivo')
    enfermedad_patologica = response_to_boolean(request.args.get('enfermedad_patologica'))
    controlada = response_to_boolean(request.args.get('controlada'))

    print(f"""
    Params
            sexo = {sexo}
            embarazo_actual = {embarazo_actual}
            embarazo_planificado = {embarazo_planificado}
            metodo_anticonceptivo = {metodo_anticonceptivo}
            enfermedad_patologica = {enfermedad_patologica}
            controlada = {controlada}
    """)

    expert_engine = Selector()
    expert_engine.reset()
    voluntarie = Voluntarie(
                            sexo=Sexo(sexo),
                            embarazo_actual=embarazo_actual,
                            embarazo_planificado=embarazo_planificado,
                            metodo_anticonceptivo=MetodoAnticonceptivo(metodo_anticonceptivo),
                            enfermedad_patologica=enfermedad_patologica,
                            controlada=controlada)
    expert_engine.declare(voluntarie)
    expert_engine.run()
    print(expert_engine.response)
    return expert_engine.response
    # if len(engine.packages) == 0:
    #     return render_template('zrp.html')

    # new_packs = []

    # for pack in engine.packages:
    #     new_packs.append(pack)

    # return render_template('response.html', packages=new_packs)


if __name__ == "__main__":
    app.run()
