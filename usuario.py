from encuesta import Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion
class Usuario:
    def __init__(self, correo:str, edad:int, region:int):
        self.__correo = correo
        self.__edad = edad
        self.__region = region

    @property
    def correo(self):
        return self.__correo
    
    @correo.setter
    def correo(self, correo):
        self.__correo = correo

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    @property
    def region(self):
        return self.__region
    
    @region.setter
    def region(self, region):
        self.__region = region

    def responder_encuesta(self):
        pass
