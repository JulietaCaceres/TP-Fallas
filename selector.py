from experta import *
from responses import *
from typing import Optional


class Voluntarie(Fact):
    def __init__(self,
                 sexo: Optional[Sexo] = None,
                 embarazo_actual: Optional[bool] = None,
                 embarazo_planificado: Optional[bool] = None,
                 metodo_anticonceptivo: Optional[MetodoAnticonceptivo] = None,
                 enfermedad_patologica: Optional[bool] = None,
                 controlada: Optional[bool] = None,
                 examen_fisico: Optional[ExamenFisico] = None
                 ):
        attrs = dict(sexo=sexo, embarazo_actual=embarazo_actual, embarazo_planificado=embarazo_planificado,
                     metodo_anticonceptivo=metodo_anticonceptivo, enfermedad_patologica=enfermedad_patologica,
                     controlada=controlada, examen_fisico=examen_fisico)
        super().__init__(**{k:v for k,v in attrs.items() if v is not None})


class Selector(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.response = "No se puede determinar la enfermedad con los datos de entrada"

    @Rule(Voluntarie(sexo=Sexo.FEMENINO,
                     embarazo_actual=True
                     )
          )
    def R1_No_Apto(self):
        self.response = "NO APTO: No puede realizar prueba durante el embarazo"

    @Rule(Voluntarie(sexo=Sexo.FEMENINO,
                     embarazo_actual=False,
                     embarazo_planificado=True
                     )
          )
    def R2_No_Apto(self):
        self.response = "NO APTO: No puede realizar la prueba si esta planificando un embarazo."

    @Rule(Voluntarie(sexo=Sexo.FEMENINO,
                     embarazo_actual=False,
                     embarazo_planificado=False,
                     metodo_anticonceptivo=MetodoAnticonceptivo.NO_USA
                     )
          )
    def R3_No_Apto(self):
        self.response = "NO APTO: No puede realizar la prueba si no usa métodos anticonceptivos."

    @Rule(Voluntarie(sexo=Sexo.FEMENINO,
                     embarazo_actual=False,
                     embarazo_planificado=False,
                     metodo_anticonceptivo=MetodoAnticonceptivo.PRESERVATIVO
                     )
          )
    def R4_Recall(self):
        self.response = "RECALL: Si incorpora otro metodo mas efectivo, se le llamara a futuro."

    @Rule(Voluntarie(sexo=Sexo.FEMENINO,
                     embarazo_actual=False,
                     embarazo_planificado=False,
                     metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                     enfermedad_patologica=True,
                     controlada=False
                     )
          )
    def R5_Recall(self):
        self.response = "NO APTO: No puede realizar la prueba si tiene una enfermedad patologica."

    @Rule(Voluntarie(sexo=Sexo.MASCULINO,
                     embarazo_actual=False,
                     embarazo_planificado=False,
                     metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                     enfermedad_patologica=True,
                     controlada=False
                     )
          )
    def R6_Recall(self):
        self.response = "NO APTO: No puede realizar la prueba si tiene una enfermedad patologica."

    @Rule(Voluntarie(sexo=Sexo.MASCULINO,
                     embarazo_actual=False,
                     embarazo_planificado=False,
                     metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                     enfermedad_patologica=False,
                     controlada=True,
                     examen_fisico=ExamenFisico.INTERMEDIO
                     )
          )
    def R7_Recall(self):
        self.response = "RECALL: Si mejora su condición física se lo llamará"

    @Rule(Voluntarie(sexo=Sexo.FEMENINO,
                     embarazo_actual=False,
                     embarazo_planificado=False,
                     metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                     enfermedad_patologica=False,
                     controlada=True,
                     examen_fisico=ExamenFisico.INTERMEDIO
                     )
          )
    def R8_Recall(self):
        self.response = "RECALL: Si mejora su condición física se la llamará"


    @Rule(Voluntarie(sexo=Sexo.MASCULINO,
                     embarazo_actual=False,
                     embarazo_planificado=False,
                     metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                     enfermedad_patologica=True,
                     controlada=True,
                     examen_fisico=ExamenFisico.GRAVE
                     )
          )
    def R9_Recall(self):
        self.response = "NO APTO: Condición física grave"

    @Rule(Voluntarie(sexo=Sexo.FEMENINO,
                     embarazo_actual=False,
                     embarazo_planificado=False,
                     metodo_anticonceptivo=MetodoAnticonceptivo.OTROS,
                     enfermedad_patologica=False,
                     controlada=True,
                     examen_fisico=ExamenFisico.GRAVE
                     )
          )
    def R10_Recall(self):
        self.response = "NO APTO: Condición física grave"