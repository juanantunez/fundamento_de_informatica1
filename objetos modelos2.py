"""
En un mundo distópico la humanidad es atacada sin descanso por titanes. Estos titanes son muy resistentes pero no inmortales, su salud (100 de máxima) puede ir 
disminuyendo si reciben daño debido a algún ataque, y si llega a 0 se muere. Al recibir este ataque la salud disminuye 1.5 por cada puntos de daño recibido.
 Además tienen la capacidad de destruir cierto número de casas dependiendo de su salud, siendo 8 casas cuando su salud es máxima o un número proporcional si su salud 
 es menor a la máxima (si tiene 60 puntos de salud destruiría 4.8 casas, es decir, 4 casas completas y más de la mitad de otra). Sin embargo no tienen la capacidad de
 comunicarse con los humanos, siendo un grito, "¡Aaaarrrg!", el único sonido que hacen. Definí la clase Titan con los atributos y métodos correspondientes.
  Además instanciá a un Titan y ejecutá las siguientes líneas:
"""


#cuyo resultado tiene que ser:

#Ejercicios modelos parcial
class Titan:
    def __init__(self, vida):
        self.vida = vida
    
    def recibir_ataque(self,danio):
        self.vida -= danio*1.5

    def esta_vivo(self):
        return self.vida > 0
    
    def salud_actual(self):
        return self.vida
    
    def cuantas_casas(self):
        return self.vida *8/100
    
    def grito(self):
        return "Aaaarrrg"
    
    def destruir_casas(self):
        self.vida -= int(self.cuantas_casas())*100/8
    

titan1 = Titan(100)
titan1.recibir_ataque(30)
print(titan1.esta_vivo())
print(titan1.salud_actual())
print(titan1.cuantas_casas())
print(titan1.grito())
titan1.destruir_casas()
print(titan1.salud_actual())
titan1.recibir_ataque(4)
print(titan1.esta_vivo())

"""
True
55
4.4
"¡Aaaarrrg!"
5.0
False
"""