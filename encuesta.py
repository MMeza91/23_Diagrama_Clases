from pregunta import Pregunta
from listado_respuestas import ListadoRespuesta

class Encuesta:
    def __init__(self, nombre:str):
        self.nombre = nombre

class EncuestaRegion(Encuesta):
    def __init__(self, nombre:str, region:int):
        super().__init__(nombre)
        self.region = region

class EncuestaEdad(Encuesta):
    def __init__(self, nombre:str, edad_min:int, edad_max:int):
        super().__init__(nombre)
        self.edad_min = edad_min
        self.edad_max = edad_max