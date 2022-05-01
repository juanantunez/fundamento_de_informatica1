#Ejercicio 4
#Vamos a salir de paseo (¡si la pandemia nos deja!). Para esto podemos utilizar como vehículos motos o autos, y de estos dos medios de transporte sabemos que:

#comienzan con una cantidad que podemos establecer de combustible

#los autos pueden llevar 5 personas como máximo y al recorrer una distancia consumen medio litro de combustible por cada kilómetro recorrido

#las motos pueden llevar 2 personas y consumen un litro por kilómetro recorrido;

#pueden cargar_combustible en la cantidad que digamos y al hacerlo suben su cantidad de combustible

#saben responder si entran una cantidad de personas. Esto sucede cuando esa cantidad es menor o igual al máximo que pueden llevar.

#Definí las clases Moto, Auto y MedioDeTransporte y hace que las dos primeras hereden de la tercera.

class MedioDeTransporte:
  def __init__(self,combustible): #combus inicial (atributo)
    self.combustible=combustible
#esta siguiente funcion se puede poner como no
  #def combustible_actual(self): #cant combust (getter)
    #return self.combustible
  def entran_personas(self, personas): #entra si personas ingresamos x parámetro <=maxpersonas
    return personas<=self.maximo_personas()
  def cargar_combustible(self, cantidad): #tiene q poder cargar combustible ingresada x parámetro	
    self.combustible+=cantidad
class Moto(MedioDeTransporte):
  def maximo_personas(self): #metodo devuelve 2 (maxpersonas es el mismo que aparece en clase madre)
    return 2
  def recorrer(self, km): #combustible lo hereda y lo modifica de tal forma
    self.combustible-=km
class Auto(MedioDeTransporte):
  def maximo_personas(self):
    return 5

  def recorrer(self, km):
    self.combustible-= km/2

#para probar
me=Auto(3)
me.recorrer(1)
print(me.combustible)