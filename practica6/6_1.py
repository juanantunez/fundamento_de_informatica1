#Ejercicio 1
#Dadas las siguientes clases responder:
#cuales son sus estados
#cuales son sus interfaces
#¿Comparten interfaz?
#¿Son polimórficas?

#resolucion:
#estados->conjunto de atributos:alimento y caricias (no importa lo q cambia o lo que valga, no es el estado inicial)#en gato los mismos

#interfaz->conjunto de métodos:que mensajes entiende la clase, sin importar lo que después hagan: 
#interfaz en perro:energía, comer, alimento, acariciar,estadebil, pasear
#interfaz en gato: energía, comer, alimento, acariciar,estadebil

#comparten interfaz?->si, comparten parcialmente xq por ej “pasear” perro lo tiene y gato no

#son polimorgicas->(No son polimorficas)->
# polimorfismo es cuando hay dos o + objetos que pueden recibir mensajes de un 3er objeto, en este caso podemos crear una 3era clase que tenga método “comer”
#y lo pueda aplicar a estas 2, ej”clase humano”,  de ahí lo que hagan esas 2 clases no importa, lo que importa es que les pueda mandar el mensaje
#EN ESTE CASO no hay un 3ero que las use, por ende no hay polimorfismo, si hubiera una 3er clase u objeto  que haga uso d estos 2, si serian polimórficas en el método “comer”, no así en general

class Perro:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 10)

    def comer(self, gramos):
        self.alimento += gramos

    def alimento(self):
	    print(self.alimento)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 2

    def pasear(self, km):
	    self.alimento -= km / 4

class Gato:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 8)

    def comer(self, gramos):
        self.alimento += gramos * 1.5

    def caricias(self):
	    print(self.caricias)

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 4