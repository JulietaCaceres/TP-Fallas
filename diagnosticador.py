from random import choice
from experta import *

class PacienteSintomas(Fact):
	pass

class DiagnosticadorPresuntivo(KnowledgeEngine):
	def __init__(self):
		super().__init__()
		self.response = "No se puede determinar la enfermedad con los datos de entrada"

	@Rule(PacienteSintomas(fiebre_mayor_37 = True,
		dolor_garganta = "NORMAL",
		dif_respirar = "NADA",
		cansancio = "NORMAL",
		anosmia = "NADA",
		ageusia = "NADA",
		tos_seca = "PREEXISTENTE",
		cefalea = True,
		secrecion_nasal = False,
		grupo_riesgo = True,
		contacto_estrecho = "NO",
		cant_contagios_zona = "BAJO"
		)
	)
	def R1_Gripe_Comun(self):
		self.response = "Lo más probable es que el paciente tenga gripe común."

	@Rule(PacienteSintomas(fiebre_mayor_37 = False,
		dolor_garganta = "NADA",
		dif_respirar = "NADA",
		cansancio = "NADA",
		anosmia = "AGUDA",
		ageusia = "AGUDA",
		tos_seca = "NADA",
		cefalea = True,
		secrecion_nasal = False,
		grupo_riesgo = False,
		contacto_estrecho = "CASUAL",
		cant_contagios_zona = "ALTO"
		)
	)
	def R2_Covid_19(self):
		self.response  = "Lo más probable es que el paciente tenga COVID-19."

	@Rule(PacienteSintomas(fiebre_mayor_37 = True,
		dolor_garganta = "INTENSO",
		dif_respirar = "PREEXISTENTE",
		cansancio = "INTENSO",
		anosmia = "PREEXISTENTE",
		ageusia = "PREEXISTENTE",
		tos_seca = "AGUDA",
		cefalea = False,
		secrecion_nasal = False,
		grupo_riesgo = False,
		contacto_estrecho = "PERMANENTE",
		cant_contagios_zona = "ALTO"
		)
	)
	def R3_Covid_19(self):
		self.response = "Lo más probable es que el paciente tenga COVID-19."

	@Rule(PacienteSintomas(fiebre_mayor_37 = True,
		dolor_garganta = "INTENSO",
		dif_respirar = "NADA",
		cansancio = "INTENSO",
		anosmia = "NADA",
		ageusia = "NADA",
		tos_seca = "AGUDA",
		cefalea = True,
		secrecion_nasal = True,
		grupo_riesgo = True,
		contacto_estrecho = "NO",
		cant_contagios_zona = "SINCASOS"
		)
	)
	def R4_Gripe_Comun(self):
		self.response = "Lo más probable es que el paciente tenga gripe común."

	@Rule(PacienteSintomas(fiebre_mayor_37 = True,
		dolor_garganta = "NADA",
		dif_respirar = "AGUDA",
		cansancio = "NORMAL",
		anosmia = "NADA",
		ageusia = "NADA",
		tos_seca = "AGUDA",
		cefalea = False,
		secrecion_nasal = False,
		grupo_riesgo = False,
		contacto_estrecho = "NO",
		cant_contagios_zona = "SINCASOS"
		)
	)
	def R5_Neumonia(self):
		self.response = "Lo más probable es que el paciente tenga neumonía."

	@Rule(PacienteSintomas(fiebre_mayor_37 = False,
		dolor_garganta = "INTENSO",
		dif_respirar = "AGUDA",
		cansancio = "NADA",
		anosmia = "NADA",
		ageusia = "NADA",
		tos_seca = "NADA",
		cefalea = False,
		secrecion_nasal = True,
		grupo_riesgo = True,
		contacto_estrecho = "CASUAL",
		cant_contagios_zona = "BAJO"
		)
	)
	def R6_Resfriado_Comun(self):
		self.response = "Lo más probable es que el paciente tenga un resfriado común."

	@Rule(PacienteSintomas(fiebre_mayor_37 = True,
		dolor_garganta = "NORMAL",
		dif_respirar = "NADA",
		cansancio = "NORMAL",
		anosmia = "AGUDA",
		ageusia = "NADA",
		tos_seca = "PREEXISTENTE",
		cefalea = True,
		secrecion_nasal = True,
		grupo_riesgo = False,
		contacto_estrecho = "CASUAL",
		cant_contagios_zona = "ALTO"
		)
	)
	def R7_No_Gripe_Comun(self):
		self.response = "Lo único que podemos definir es que el paciente no tiene gripe común."

	@Rule(PacienteSintomas(fiebre_mayor_37 = True,
		dolor_garganta = "NADA",
		dif_respirar = "AGUDA",
		cansancio = "INTENSO",
		anosmia = "NADA",
		ageusia = "NADA",
		tos_seca = "AGUDA",
		cefalea = False,
		secrecion_nasal = True,
		grupo_riesgo = True,
		contacto_estrecho = "PERMANENTE",
		cant_contagios_zona = "ALTO"
		)
	)
	def R8_Covid_19(self):
		self.response = "Lo mas probable es que el paciente tenga COVID-19."

	@Rule(PacienteSintomas(fiebre_mayor_37 = True,
		dolor_garganta = "INTENSO",
		dif_respirar = "AGUDA",
		cansancio = "INTENSO",
		anosmia = "PREEXISTENTE",
		ageusia = "AGUDA",
		tos_seca = "AGUDA",
		cefalea = True,
		secrecion_nasal = False,
		grupo_riesgo = False,
		contacto_estrecho = "PERMANENTE",
		cant_contagios_zona = "BAJO"
		)
	)
	def R9_Covid_19(self):
		self.response = "Lo mas probable es que el paciente tenga COVID-19."

	@Rule(PacienteSintomas(fiebre_mayor_37 = False,
		dolor_garganta = "INTENSO",
		dif_respirar = "NADA",
		cansancio = "NADA",
		anosmia = "NADA",
		ageusia = "NADA",
		tos_seca = "AGUDA",
		cefalea = True,
		secrecion_nasal = True,
		grupo_riesgo = True,
		contacto_estrecho = "NO",
		cant_contagios_zona = "ALTO"
		)
	)
	def R10_Resfriado_Comun(self):
		self.response = "Lo mas probable es que el paciente tenga un resfriado común."
