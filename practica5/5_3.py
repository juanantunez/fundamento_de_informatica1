#Ejercicio 3
#Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un descuento al precio, 
# el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que devolver cuánto valdría esa notebook si se aplicase el descuento. 
# Por último hay que instanciar esta clase y en algunos casos aplicar este descuento. 

#aux:estado es el conjunto de atributos

class Notebook:

  def __init__(self, marca, modelo, precio):  #funcion siempre debe tener el self, defino marca modelo y precio de esta clase
    self.marca=marca
    self.modelo=modelo
    self.precio=precio
  def descuento(self, nro): #voy a ingresar un nro de pocentaje, a este lo hago divido 100 y al multiplcarlo por precio, me da cuanto seria el descuento en pesos#aux:ej (50%/100%).30=15
    descuento=(nro/100)*(self.precio)
    return(self.precio-descuento)     #precio -descuento en pesos, me da el precio origi 

#para probarlo
remera= Notebook("e", "w", 30)
print(remera.descuento(50))
