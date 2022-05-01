#Ejercicio 1
#Dada la siguiente clase, identificá la interfaz y el estado de la misma:



#Resolucion:

#interfaz->conjunto de métodos:que mensajes entiende la clase, sin importar lo que después hagan(conjunto de mensajes que cada objeto expone)
#interfaz:energia, comer, acariciar, esta debil 

#estados->conjunto de atributos(no importa lo q cambia o lo que valga, no es el estado inicial)
#estados:alimento y caricias 

class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2

#este no es para probar, era solo para responder preguntas teoricas


