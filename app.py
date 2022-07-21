from random import choice
from diagnosticadorPresuntivo import *
from flask import Flask
from flask import request
from flask import render_template
from flask import send_file
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('init.html')

@app.route("/handle_data")
def handle_data():

    fiebre_mayor_37 = request.args.get('fever')
    dolor_garganta = request.args.get('throat')
    dif_respirar = request.args.get('breath')
    cansancio = request.args.get('fatigue')
    anosmia = request.args.get('smell')
    ageusia = request.args.get('taste')
    tos_seca = request.args.get('cough')
    cefalea = request.args.get('headache')
    secrecion_nasal = request.args.get('mocus')
    grupo_riesgo = request.args.get('risk')
    contacto_estrecho = request.args.get('contact')
    cant_contagios_zona = request.args.get('zone')

    print(f"""
    Params
        fiebre_mayor_37={fiebre_mayor_37}
        dolor_garganta={dolor_garganta}
        dif_respirar={dif_respirar}
        cansancio={cansancio}
        anosmia={anosmia}
        ageusia={ageusia}
        tos_seca={tos_seca}
        cefalea={cefalea}
        secrecion_nasal={secrecion_nasal}
        grupo_riesgo={grupo_riesgo}
        contacto_estrecho={contacto_estrecho}
        cant_contagios_zona={cant_contagios_zona}
    """)

    engine = DiagnosticadorPresuntivo()
    engine.reset()
    paciente_sintomas = PacienteSintomas(fiebre_mayor_37 = fiebre_mayor_37,
        dolor_garganta = dolor_garganta,
        dif_respirar = dif_respirar,
        cansancio = cansancio,
        anosmia = anosmia,
        ageusia = ageusia,
        tos_seca = tos_seca,
        cefalea = cefalea,
        secrecion_nasal = secrecion_nasal,
        grupo_riesgo = grupo_riesgo,
        contacto_estrecho = contacto_estrecho,
        cant_contagios_zona = cant_contagios_zona)
    engine.declare(paciente_sintomas)
    engine.run()
    print(engine.response)
    return engine.response
    # if len(engine.packages) == 0:
    #     return render_template('zrp.html')

    # new_packs = []

    # for pack in engine.packages:
    #     new_packs.append(pack)

    # return render_template('response.html', packages=new_packs)

if __name__ == "__main__":
    app.run()