from responses import MetodoAnticonceptivo, Edad
from selector import Voluntarie, Selector, Sexo
from flask import Flask
from flask import request
from flask import render_template

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
    edad = request.args.get('edad')
    sexo = request.args.get('sexo')
    embarazo_actual = response_to_boolean(request.args.get('embarazo_actual'))
    embarazo_planificado = response_to_boolean(request.args.get('embarazo_planificado'))
    metodo_anticonceptivo = request.args.get('metodo_anticonceptivo')
    enfermedad_patologica = response_to_boolean(request.args.get('enfermedad_patologica'))
    controlada = response_to_boolean(request.args.get('controlada'))
    examen_fisico = request.args.get('examen_fisico')
    auscultacion_respiratoria = request.args.get('auscultacion_respiratoria')
    auscultacion_cardiaca = request.args.get('auscultacion_cardiaca')
    pulso = request.args.get('pulso')
    covid = response_to_boolean(request.args.get('covid'))
    vacunacion = response_to_boolean(request.args.get('vacunacion'))
    enfermedad_grave = response_to_boolean(request.args.get('enfermedad_grave'))


    print(f"""
    Params
            edad = {edad}
            sexo = {sexo}
            embarazo_actual = {embarazo_actual}
            embarazo_planificado = {embarazo_planificado}
            metodo_anticonceptivo = {metodo_anticonceptivo}
            enfermedad_patologica = {enfermedad_patologica}
            controlada = {controlada}
            examen_fisico = {examen_fisico}
            auscultacion_respiratoria = {auscultacion_respiratoria}
            auscultacion_cardiaca = {auscultacion_cardiaca}
            pulso = {pulso}
            covid = {covid}
            vacunacion = {vacunacion}
            enfermedad_grave = {enfermedad_grave}
    """)

    expert_engine = Selector()
    expert_engine.reset()
    voluntarie = Voluntarie(
                            edad= Edad(edad),
                            sexo=Sexo(sexo),
                            embarazo_actual=embarazo_actual,
                            embarazo_planificado=embarazo_planificado,
                            metodo_anticonceptivo=MetodoAnticonceptivo(metodo_anticonceptivo),
                            enfermedad_patologica=enfermedad_patologica,
                            controlada=controlada,
                            examen_fisico=examen_fisico,
                            auscultacion_respiratoria=auscultacion_respiratoria,
                            auscultacion_cardiaca=auscultacion_cardiaca,
                            pulso=pulso,
                            covid=covid,
                            vacunacion=vacunacion,
                            enfermedad_grave=enfermedad_grave,
                            )
    expert_engine.declare(voluntarie)
    expert_engine.run()
    print(expert_engine.response)
    return render_template('response.html', packages=expert_engine)


if __name__ == "__main__":
    app.run(debug=True)
