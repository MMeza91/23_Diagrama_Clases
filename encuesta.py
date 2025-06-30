from pregunta import Pregunta
from listado_respuestas import ListadoRespuesta
from usuario import Usuario

class Encuesta:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.lista_preguntas = []
        self.respuestas = []
        #crea las preguntas de la encuesta
        self.crear_preguntas()


    def crear_preguntas(self):
        while True:
            enunciado = input("Ingrese el enunciado de la pregunta: ")
            ayuda = input("Ingrese la ayuda de la pregunta: ")
            es_requerido = int(input("Ingrese 1 si la pregunta es requerida, 0 si no lo es: "))
            self.lista_preguntas.append(Pregunta(enunciado,ayuda,es_requerido))
            #Se consulta si se sigue en el bucle o no
            consulta = input("Quiere agregar otra pregunta? s/n: ")
            if consulta.lower() == "n":
                break

    def mostrar_encuesta(self):
        print(f"Nombre de encuesta: {self.nombre}")
        for i in self.lista_preguntas:
            indice = self.lista_preguntas.index[i]
            print(f"Pregunta {indice +1}:")
            i.mostrar_pregunta()

    def reponder_preguntas(self, usuario :Usuario):
        respuesta = ListadoRespuesta(usuario)
        for i in self.lista_preguntas:
            indice = self.lista_preguntas.index[i]
            respuesta.respuestas.append(input(f"Indique su respuesta para la pregunta N° {indice +1}: "))
        self.respuestas.append(respuesta)
        


class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre:str, *region:int):
        super().__init__(nombre)
        self.__region = list(region)
    
    @property
    def region(self):
        return self.__region
    
    @region.setter
    def region(self, region:int):
        self.__region = region

    def limite(self, usuario :Usuario):
        if usuario.region in self.region:
            return True
        else:
            return False

    def reponder_preguntas(self, usuario :Usuario):
        if self.limite(usuario):
            respuesta = ListadoRespuesta(usuario)
            for i in self.lista_preguntas:
                indice = self.lista_preguntas.index[i]
                respuesta.respuestas.append(input(f"Indique su respuesta para la pregunta N° {indice +1}: "))
            self.respuestas.append(respuesta)
        else:
            print("Esta encuesta no se puede realizar")

    

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, edad_min:int, edad_max:int, nombre:str):
        super().__init__(nombre)
        self.__edad_min = edad_min
        self.__edad_max = edad_max

    @property
    def edad_min(self):
        return self.__edad_min
    
    @edad_min.setter
    def edad(self, edad_min:int):
        self.__edad_min = edad_min

    @property
    def edad_max(self):
        return self.__edad_max
    
    @edad_max.setter
    def edad_max(self, edad_max:int):
        self.__edad_max = edad_max

    def limite(self, usuario :Usuario):
        if (usuario.edad >= self.edad_min and usuario.edad <= self.edad_max):
            return True
        else:
            return False

    def reponder_preguntas(self, usuario :Usuario):
        if self.limite(usuario):
            respuesta = ListadoRespuesta(usuario)
            for i in self.lista_preguntas:
                indice = self.lista_preguntas.index[i]
                respuesta.respuestas.append(input(f"Indique su respuesta para la pregunta N° {indice +1}: "))
            self.respuestas.append(respuesta)
        else:
            print("Esta encuesta no se puede realizar")

