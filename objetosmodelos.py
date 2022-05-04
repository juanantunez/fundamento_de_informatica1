"""
Los estudiantes (como ustedes) son como cualquier persona, las cuales recuperan energía si duermen o si comen, o la gastan al hacer ejercicio, sin embargo en particular
 los estudiantes también gastan energía al estudiar y se sienten felices al aprobar algún exámen. Resumiendo, las personan pueden:

Decirnos cuánta energía tienen.
Recuperar el máximo de energía (100) al dormir 8 horas, o el proporcional si duermen menos (si duermen 4 ganan la mitad de energía, es decir 50).
Recuperar energía al comer, ganando de esta manera 10 puntos.
Gastar energía al hacer ejercicio, siendo un gasto de 25 puntos por cada media hora de ejercicio.
Como estado de ánimo pueden estar felices o no, pero por defecto no están felices.
Además los estudiantes tienen el siguiente comportamiento:

Al estudiar su energía disminuye 20 puntos por cada hora de estudio.
Si aprueban su estado de ánimo pasa a ser "Feliz".
Definí las clases Persona y Estudiante con los atributos y métodos correspondientes y hacé que esta última herede de la primera. Además instanciá a un Estudiante y ejecutá las siguientes líneas:


auxiliar mio:
#estudiantes comportamiento especifico dentro de clase madre persona   Si duermen 8 al 100% y proporcional (ej: si 4 recupera 50%)      Estudiante heredara de persona
Tenemos que instanciar un estudiante ejecutarle líneas dadas y que de tal resultado       #clase madre no se instancia, se instancian las clases hijas
Clase persona tiene energía y puede estar o no feliz       Atributos: energía y felicidad(estado emocional, no estado en si)
#setiamos energía    #en principio no es feliz    #getter para saber valor del atributo energía   #si hace ej(regla de 3 simple)->si en 30 min gasta 25, en “min” cuanto
#max energía al dormir 8 hs     Si cant de horas>=8 va a tener 100%
Elif Energía que tengo + la que recupere durmiendo(calculo con regla de 3 simple, si con 8 tengo 100%, con cant horas ingresadas cuanto?( sea <=100 )->se lo asigna a la energía
Else: si pasa los 100 entre la energía que tenia y una cant horas x ej menor a 8, va devolver 100
Cada vez que comia se le aumentaba en 10, energía max, (agregar que no puede pasar 100)      Energía q tengo +energía q gano comiendo<=100 como en el anterior def
Clase estudiante    Por cada hora gasta 20 de energía       Si aprueba atributo ser feliz se convierte en true y te devuelve ese atributo. 
"""

#cuyo resultado tiene que ser:

True
25.0

class Estudiante:
    def __init__(self, energia):
        self.energia = energia
        self.estado = False
    
    def energia_actual(self):
        return self.energia
    
    def dormir(self, horas):
        if self.energia + (horas * 100/8) > 100:
            self.energia = 100
        else:
            self.energia += horas * 100/8
    
    def comer(self):
        self.energia += 10
    
    def hacer_ejercicio(self, minutos):
        if self.energia - minutos *25/30 < 0:
            self.energia = 0
        else:
            self.energia -= minutos*25/30
    
    def esta_feliz(self):
        return self.estado
    
    def estudiar(self, hora):
        if self.energia - hora *20 < 0:
            self.energia = 0
        else:
            self.energia -= hora*20
    
    def aprobar(self):
        self.estado = True
        return self.estado

estudiante = Estudiante(100)
estudiante.hacer_ejercicio(30)
estudiante.estudiar(3)
estudiante.comer()
print(estudiante.aprobar())
print(estudiante.energia_actual())


#cuyo resultado tiene que ser:

#True
#25.0