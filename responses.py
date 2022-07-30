from enum import Enum


class Sexo(str, Enum):
    FEMENINO = "FEMENINO"
    MASCULINO = "MASCULINO"


class MetodoAnticonceptivo(str, Enum):
    NO_USA = "NO_USA"
    PRESERVATIVO = "PRESERVATIVO",
    OTROS = "OTROS"


class ExamenFisico(str, Enum):
    INTERMEDIO = "INTERMEDIO"
    NORMAL = "NORMAL"
    GRAVE = "GRAVE"
