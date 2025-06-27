from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado:str, ayuda:str, es_requerido:bool = 0):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.es_requerido = es_requerido
        self.__lista_alternativas = []

        self.__crear_alternativas()

    #Se determina el uso de 5 alternativas por pregunta
    def __crear_alternativas(self):
        for i in range(5):
            contenido = input(f"Ingrese la alternativa N° {i+1}: ")
            tiene_ayuda = input(f"¿Desea agregar una ayuda?(s/n): ")
            if tiene_ayuda.lower() == "s":
                ayuda = input(f"Ingrese la ayuda de la alternativa N° {i+1}: ")
            else:
                ayuda = "Sin más información"
            self.__lista_alternativas.append(Alternativa(contenido, ayuda))

    @property
    def lista_alternativas(self):
        return self.__lista_alternativas

    def mostrar_pregunta(self):
        print(f"""
Enunciado: {self.enunciado}
Ayuda: {self.ayuda}
Pregunta es requerida: {self.es_requerido}
Alternativas: """)
        for i in self.lista_alternativas:
            print(f"\t{self.lista_alternativas.index(i)+1}.- {i.mostrar_alternativa()}")

        
if __name__ == "__main__":

    c = Pregunta("hola", "nada")
    c.mostrar_pregunta()
