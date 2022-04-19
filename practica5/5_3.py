#Ejercicio 3
#Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un descuento al precio, el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que devolver cuánto valdría esa notebook si se aplicase el descuento. Por último hay que instanciar esta clase y en algunos casos aplicar este descuento. 

class Notebook:
  def init(self, marca, modelo, precio):  #funcion siempre debe tener el self, defino marca modelo y precio de esta clase
    self.marca=marca
    self.modelo=modelo
    self.precio=precio
  def descuento(self, nro):              #voy a ingresar un nro de pocentaje, a este lo hago divido 100 y al multiplcarlo por precio, me da cuanto seria el descuento
    descuento=(nro/100)*self.precio
    return(self.precio-descuento)     #precio -descuento, me da el precio origi 