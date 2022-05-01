#Ejercicio 4
#Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, recordando el valor actual.
#También puede resetear este valor y al hacerlo se pone en cero. Además es posible indicar directamente un número nuevo que reemplace al valor actual.
#Este objeto debe entender los siguientes mensajes:

#reolucion:
class Contador:
  def __init__(self, valor):
    self.valor=valor

  def inc(self): #valor suma 1
    self.valor+=1
  def dis(self): #valor resta 1
    self.valor-=1
  def reset(self): #valor pasa a valer 0
    self.valor=0
  def valorActual(self): #printea el valor q lleva al momento
    print(self.valor)     
  def valorNuevo(self, nuevoValor): #le determina el nro al valor
    self.valor=nuevoValor  

#pruebas
rosaa=Contador(1)  
rosaa.inc()
rosaa.inc()
#print(rosaa.valorNuevo(45))
print(rosaa.valor)
print(rosaa.reset())
print(rosaa.valorActual())