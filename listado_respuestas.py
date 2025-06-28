from usuario import Usuario


class ListadoRespuesta:
    def __init__(self, usuario: Usuario):
        self.__usuario = usuario
        self.__respuestas = []

    @property
    def usuario(self):
        return self.__usuario

    @property
    def respuestas(self):
        return self.__respuestas
