#Ejercicio 6
#Implementá una clase que represente una calculadora sencilla, que permita sumar, restar y multiplicar. Este objeto debe entender los siguientes mensajes:

class Calculadora:
    def __init__(self): #inicializa siempre en 0
        self.valor = 0
    
    def cargar(self, numero): #cargo valor y con las demas funciones puedo ir modificando
        self.valor = numero

    def sumar(self, numero):
        self.valor += numero
    
    def restar(self, numero):
        self.valor -= numero
    
    def multiplicar(self, numero):
        self.valor = self.valor*numero

    def valorActual(self):
        return self.valor

#para probar
ew=Calculadora()
ew.cargar(3)
ew.restar(1)        
print(ew.valorActual())