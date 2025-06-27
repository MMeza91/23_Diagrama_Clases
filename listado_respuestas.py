from usuario import Usuario


class ListadoRespuesta:
    def __init__(self, usuario: Usuario):
        if isinstance(usuario, Usuario):
            self.__usuario = usuario
        else:
            raise ValueError("El argumento 'usuario' debe ser una instancia de la clase Usuario")
        self.__respuestas = []
