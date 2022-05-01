#Ejercicio 5
#Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último comando que se le dió, en forma de mensaje.
#  Estos mensajes pueden ser: "reset", "incremento", "disminución" o "actualización" (para cuando se coloca un valor nuevo).
#  El método para saber el último comando es ultimoComando, y el resultado de aplicarlo a la serie de comandos dicha en el ejercicio anterior debería ser "disminución".

class Contador:                       
  def __init__(self, valor):
    self.valor=valor
    self.lista1=[]  #hago lista que en caso de sumar un valor sume a la lista el mensaje notificando que sumo y asi para cada modificacion

  def inc(self): #valor suma 1 ->suma a lista mensaje 
    self.valor+=1
    self.lista1.append("incremento")
  def dis(self): #valor resta 1
    self.valor-=1
    self.lista1.append("disminucion")
  def reset(self): #valor pasa a valer 0
    self.valor=0
  def valorActual(self): #printea el valor q lleva al momento
    print(self.valor)     
  def valorNuevo(self, nuevoValor): #le determina el nro al valor
    self.valor=nuevoValor  
    self.lista1.append("actualizacion")
  def ultimoComando(self):
      return self.lista1[-1]  #va a la lista creada con los mensajes y toma solamente el ultimo elemento

#pruebas
rosaa=Contador(1)  
rosaa.inc()
rosaa.inc()
#print(rosaa.valorNuevo(45))
print(rosaa.valor)
#print(rosaa.reset())
#print(rosaa.valorActual())
rosaa.dis()
print(rosaa.ultimoComando())


