class Contador:
  def _init_(self, valor=0):
    self.valor=valor
    self.valor_inicial=valor
  def inc(self):
    self.valor+=1
  def dis(self):
    self.valor-=1
  def reset(self):
    self.valor=0
  def valorActual(self):
    print(self.valor)
  def valorNuevo(self, nuevoValor):
    self.valor=nuevoValor          
    
contador = Contador(10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
contador.valorActual()
contador.valorNuevo(27)
contador.dis()
contador.dis()
contador.valorActual()    