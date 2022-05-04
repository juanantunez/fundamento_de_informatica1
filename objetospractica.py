#ej 2 parcialito
"""
#**Consigna N°2** (POO)
#Un taller de diseño de autos quiere estudiar un nuevo prototipo. Para eso, nos piden hacer un modelo concentrado en las características del motor.
#El prototipo de motor tiene 5 cambios (de primera a quinta), y soporta hasta 5000 rpm.
#La velocidad del auto se calcula así: _**(rpm / 100) * (0.5 + (cambio / 2))**_. Por ejemplo en tercera a 2000 rpm, la velocidad es 20 * (0.5 + 1.5) = 40.
#También nos interesa controlar el consumo. Se parte de una base de 0.05 litros por kilómetro. A este valor se le aplican los siguientes ajustes:
#* Si el motor está a más de 3000 rpm, entonces se multiplica por (rpm - 2500) / 500. Por ejemplo, a 3500 rpm hay que multiplicar por 2, a 4000 rpm por 3, etc.
#* Si el motor está en primera, entonces se multiplica por 3.
#* Si el motor está en segunda, entonces se multiplica por 2.
#Los efectos por revoluciones y por cambio se acumulan. Por ejemplo, si el motor está en primera y a 5000 rpm, entonces el consumo es 0.05 * 5 * 3 = 0.75 litros/km.
#El modelo debe entender estos mensajes:
#arrancar() , se pone en primera con 500 rpm.
#subirCambio()
#bajarCambio()
#subirRPM(cuantos)
#bajarRPM(cuantos)
#velocidad()
#consumoActualPorKm(), calcula el consumo actual y lo devuelve

#5 cambios |   soporta hasta 5000 rpm | velocidad=  (rpm / 100) * (0.5 + (cambio / 2)) | consumo=0,05 cada  km |si rpm>3000 : se hace *(rpm - 2500) / 500 |1ra con 500 rpm |
#  hay q indicar cuantos rpm sube o baja
3
class Auto:
    def __init__(self):             
        self.consumo=0.05   #dato
        self.cambio=0
        self.rpm=0
    def arrancar(self):   
        self.cambio+=1
        self.rpm+=500   #dato
    def subirCambio(self):
        if self.cambio <5: #max cambio es 5 
            self.cambio+=1
        else:
            return None   #retorna None en caso q no se pueda
    def bajarCambio(self):
        if self.cambio >1: #min cambio es 1
            self.cambio-=1
        else:
            return None 
    def subirRPM(self, cantidad): #como dice enunciado, es una cant a ingresar
        if self.rpm <=5000:
            self.rpm+=cantidad
        else:
             self.rpm= 5000    #xq es el max
    def bajarRPM(self, cantidad):
        if self.rpm - cantidad >=0:
            self.rpm-=cantidad
        else: 
             self.rpm=0  #xq es el min
    def velocidad(self):
        return ((self.rpm / 100) * (0.5 + (self.cambio / 2))) #formula dato

    def consumoActualPorKm(self):   
        if self.rpm>3000:  #siempre q sea >3000 
            if self.cambio==1:
                return self.consumo*((self.rpm-2500)/500) *3 #hay q hacer consumo * cuenta correspondiente * 3(por estar en 1ra)
            elif self.cambio==2:
                return self.consumo*((self.rpm-2500)/500) *2 #mismo q en anterior pero *2, por estar en 2da
            elif 3<= self.cambio <=5:
                return self.consumo*((self.rpm-2500)/500) #aca solo consumo * cuenta correspondiente
        elif self.cambio==1:
            return self.consumo*3   #hace solo conusmo *3
        elif self.cambio==2:
            return self.consumo*2 #mismo q anterior pero *2
        elif 3<=self.cambio<=5:
            return self.consumo           #solo consumo 

#Al ejecutar esto:

#```python
auto1 = Auto()
auto1.arrancar()
auto1.subirRPM(3500)
auto1.subirCambio()
auto1.subirCambio()
auto1.subirCambio()
auto1.bajarCambio()
print(auto1.velocidad())
print(auto1.consumoActualPorKm())

#la velocidad debería ser 80 y el consumo 0.15 litros/km.
"""
#ej 1 de parcial otro añoo
"""
### Consigna N°1
Dada la siguiente clase resolvé los siguientes ejercicios y respondé las preguntas:
  Python
  class Pokemon():
     def __init__(self, vidas = 10, nombre, nivel = 1):
        self.vidas = vidas
        self.nombre = nombre
        self.nivel = nivel
     
     def pelear(self):
        self.vidas -= 3
        
     def entrar_pokebola(self, entrenador):
        self.vidas += 2
     
     def comer(self):
        self.vidas += 5
  
   a) ¿Cuál es el nombre de la clase? ¿Cuál es el estado de un Pokemón? ¿Qué mensajes entiende un Pokemon? 
  
   
   b) Instanciá al Pokemón Sylveon.
   
   c) Definir el método beso_drenaje que le otorga 5 vidas, ya que drena la energía de su oponente.
   
   d) Definir un método saludar que retorne el nombre del Pokemon por duplicado.

  
   #a) pokemon    #vidas, nombre, nivel (conjunto de atrubutos) #pelear, entrenar_pokemon_comer (metodos)

class Pokemon():

   def __init__(self, vidas = 10, nombre="sylveon", nivel = 1): #DIRECTO PONGO ACA EL NOMBRE PARA QUE ESTE  YA INICIALIZADO TODOS SUS ATRIBUTOS
      self.vidas = vidas
      self.nombre = nombre
      self.nivel = nivel
     
   def pelear(self):
      self.vidas -= 3
        
   def entrar_pokebola(self, entrenador):
      self.vidas += 2
     
   def comer(self):
      self.vidas += 5

   def beso_drenaje(self):                                         #FUNCION A SUMAR
      self.vidas+=5
   def saludar(self):                                              #FUNCION A SUMAR
      self.nombre=self.nombre + "" + self.nombre

pokemon_sylveon = Pokemon()                                                         #->ACA ESTA INSTANCIADO EL POKEMOS_SYLVEON
pokemon_sylveon.pelear()  #el pokemon pierde 3 de vida
pokemon_sylveon.comer() # el pokemon gana 5 de vida
pokemon_sylveon.entrar_pokebola("entre")     #el pokemon gana 2 de vida
pokemon_sylveon.beso_drenaje()
print(pokemon_sylveon.vidas)
pokemon_sylveon.saludar()
print(pokemon_sylveon.nombre)
   """
#ej 4 parcial otro año
   """
### Consigna N°4
En un mundo distópico la humanidad es atacada sin descanso por titanes. Estos titanes son muy resistentes pero no inmortales, su salud (100 de máxima) puede ir disminuyendo si reciben daño debido a algún ataque,
 y si llega a 0 se muere. Al recibir este ataque la salud disminuye 1.5 por cada puntos de daño recibido. Además tienen la capacidad de destruir cierto número de casas dependiendo de su salud, 
 siendo 6 casas cuando su salud es máxima o un número proporcional si su salud es menor a la máxima (si tiene 60 puntos de salud destruiría 3.6 casas, es decir, 3 casas completas y más de la mitad de otra).
  Sin embargo no tienen la capacidad de comunicarse con los humanos, siendo un grito, "¡Aaaarrrg!", el único sonido que hacen. 
  Pero para empeorar las cosas existen súper titanes, los cuales tienen la capacidad de correr y regenerarse la salud (20 puntos cada 15 minutos).
Definí las clases Titan y Supertitan con los atributos y métodos correspondientes y hacé que esta última herede de la primera. Además instanciá a dos Supertitanes y ejecutá las siguientes líneas:

#datos:
#class titan->  | saludmax=100 | salud=0 muere | ataque=salud-1,5 por cada punto | 6casas destruye con salud max ->nro proporcional con salud menor | (ptos salud q tiene * 6 casas ) /100 = cant casas a destruir | comunica->grito "arrg"  
#class super titanes-> correr regenerearse la salud 20 puntos cada 15 minutos |  


class Titan():

    def __init__(self, salud):
        self.salud=salud
    def salud_actual(self):
        return self.salud

    def recibir_ataque(self, cant):
        if cant*1.5<self.salud:
            self.salud -=cant* 1.5
        else:
            return 0    

    def cuantas_casas(self):
        if self.salud >16.6:
            return (self.salud * 6  ) /100 
        else:
            return 0    


    def grito(self):
        print("¡Aaaarrrg!")    
    def esta_vivo(self):
        if self.salud >0:
            return True        

class Supertitan(Titan):

    def correr(self):
        print("corre")

    def recuperarse(self, minutos):
        self.salud += 20 * minutos / 15  #20 puntos de salud *cant de minutos /15 minutos = cantidad de puntos de salud

#prueba dada por ej:

supertitan1 = Supertitan(100)
supertitan1.recibir_ataque(40)
print(supertitan1.salud_actual())
print(supertitan1.cuantas_casas())
print(supertitan1.esta_vivo())
print("\n")
supertitan2 = Supertitan(70)
print(supertitan2.grito())
supertitan2.recibir_ataque(30)
print(supertitan2.cuantas_casas())
supertitan2.recuperarse(15)
print(supertitan2.salud_actual())
supertitan2.recibir_ataque(30)
print(supertitan2.esta_vivo())

python
40.0
2.4
True


¡Aaaarrrg!
1.5
45.0
False
"""
#modelos1


"""
En un mundo distópico la humanidad es atacada sin descanso por titanes. Estos titanes son muy resistentes pero no inmortales, su salud (100 de máxima) puede ir 
disminuyendo si reciben daño debido a algún ataque, y si llega a 0 se muere. Al recibir este ataque la salud disminuye 1.5 por cada puntos de daño recibido.
 Además tienen la capacidad de destruir cierto número de casas dependiendo de su salud, siendo 8 casas cuando su salud es máxima o un número proporcional si su salud 
 es menor a la máxima (si tiene 60 puntos de salud destruiría 4.8 casas, es decir, 4 casas completas y más de la mitad de otra). Sin embargo no tienen la capacidad de
 comunicarse con los humanos, siendo un grito, "¡Aaaarrrg!", el único sonido que hacen. Definí la clase Titan con los atributos y métodos correspondientes.
  Además instanciá a un Titan y ejecutá las siguientes líneas:


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


True
55
4.4
"¡Aaaarrrg!"
5.0
False
"""

#modelos 2
"""

Se está pensando en el diseño de un juego que incluye la nave espacial Enterprise. En el juego, esta nave tiene un nivel de potencia de 0 a 100, y un nivel de coraza de 0 a 20. La Enterprise puede:

encontrarse con una pila atómica, en cuyo caso su potencia aumenta en 25.
encontrarse con un escudo, en cuyo caso su nivel de coraza aumenta en 10.
recibir un ataque, en este caso se especifican los puntos de fuerza del ataque recibido. La Enterprise "detiene" el ataque con la coraza, y si la coraza no alcanza, el resto se descuenta de la potencia. Por ejemplo si la Enterprise con 80 de potencia y 12 de coraza recibe un ataque de 20 puntos de fuerza, puede parar solamente 12 con la coraza, los otros 8 se descuentan de la potencia. La nave debe quedar con 72 de potencia y 0 de coraza. Si la Enterprise no tiene nada de coraza al momento de recibir el ataque, entonces todos los puntos de fuerza del ataque se descuentan de la potencia.
La potencia y la coraza tienen que mantenerse en los rangos indicados, por ejemplo, si la Enterprise tien 16 puntos de coraza y se encuentra con un escudo, entonces queda en 20 puntos de coraza, no en 26. Tampoco puede quedar negativa la potencia, a lo sumo queda en 0. La Enterprise nace con 50 de potencia y 5 de coraza. Implementar este modelo de la Enterprise, que tiene que entender los siguientes mensajes:

potencia()

coraza()

encontrarPilaAtomica()

encontrarEscudo()

recibirAtaque(puntos)

Al ejecutar esto:

enterprise = Enterprise()
enterprise.encontrarPilaAtomica()
enterprise.recibirAtaque(14)
enterprise.encontrarEscudo()
la potencia de la Enterprise debe ser 66, y su coraza debe ser 10.

Agregar al modelo de la Enterprise, la capacidad de entender estos mensajes.

fortalezaDefensiva(), que es el máximo nivel de ataque que puede resistir, o sea, coraza más potencia.
necesitaFortalecerse(), tiene que ser true si su coraza es 0 y su potencia es menos de 20.
fortalezaOfensiva(), que corresponde a cuántos puntos de fuerza tendría un ataque de la Enterprise. Se calcula así: si tiene menos de 20 puntos de potencia entonces es 0, si no es (puntos de potencia - 20) / 2.


class Enterprise:
    def __init__(self,):
        self.potencia = 50
        self.coraza = 5
    
    def encontrarPilaAtomica(self):
        if self.potencia + 25 > 100:
            self.potencia = 100
        else:
            self.potencia += 25
    
    def encontrarEscudo(self):
        if self.coraza + 10 > 20:
            self.coraza = 20
        else:
            self.coraza += 10
    
    def recibirAtaque(self, cantidad):
        if self.coraza - cantidad < 0:
            if self.potencia - (cantidad - self.coraza) < 0:
                self.potencia = 0
                self.coraza = 0
            else:
                self.potencia -= (cantidad - self.coraza)
                self.coraza = 0
    
    def fortalezaDefensiva(self):
        return self.coraza + self.potencia
    
    def necesitaFortalecerse(self):
        return self.potencia < 20 and self.coraza == 0
    
    def fortalezaOfensiva(self):
        if self.potencia < 20:
            return 0
        else:
            return (self.potencia - 20) / 2
            
enterprise = Enterprise()
enterprise.encontrarPilaAtomica()
enterprise.recibirAtaque(14)
enterprise.encontrarEscudo()
print(enterprise.potencia)
print(enterprise.coraza)

66
10
"""
#modelos 3
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
"""
#practicas
"""
Ejercicio 1
Dada la siguiente clase, identificá la interfaz y el estado de la misma:

class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2
Ejercicio 2
Modificá el método volar de la clase Golondrina visto en la clase de teoría de manera que no pueda volar si al hacerlo la energía toma el valor 0 o valor negativo.

Ejercicio 3
Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un descuento al precio, el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que devolver cuánto valdría esa notebook si se aplicase el descuento. Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.

Ejercicio 4
Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, recordando el valor actual. También puede resetear este valor y al hacerlo se pone en cero. Además es posible indicar directamente un número nuevo que reemplace al valor actual. Este objeto debe entender los siguientes mensajes:

inc()

dis()

reset()

valorActual()

valorNuevo(nuevoValor)

Como ejemplo el resultado de ejecutar las siguientes líneas tiene que ser 12 y 25.

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
Ejercicio 5
Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último comando que se le dió, en forma de mensaje. Estos mensajes pueden ser: "reset", "incremento", "disminución" o "actualización" (para cuando se coloca un valor nuevo). El método para saber el último comando es ultimoComando, y el resultado de aplicarlo a la serie de comandos dicha en el ejercicio anterior debería ser "disminución".

Ejercicio 6
Implementá una clase que represente una calculadora sencilla, que permita sumar, restar y multiplicar. Este objeto debe entender los siguientes mensajes:

cargar(numero)

sumar(numero)

restar(numero)

multiplicar(numero)

valorActual()

Si se evalúa la siguiente secuencia:

calculadora = Calculadora()
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
calculadora.valorActual()
el resultado debe ser 24.

Ejercicio 7
Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas como CSS (coeficiente de serenidad silenciosa), CSSP y CSSV (como el CSS pero “pico” y “veces”). El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar, por la cantidad total de gramos de comida que ingiere. El CSSP es la misma división pero considerando solamente lo que voló la vez que más voló y lo que comió la vez que más comió. El CSSV es otra vez la misma idea, respecto de la cantidad de veces que voló y comió. Si un gorrión nunca comió, los coeficientes deben ser None. Un gorrión se considera en equilibrio si su CSS está entre 0.5 y 2.

"""
#practica2obj

"""
Ejercicio 1
Dadas las siguientes clases responder:

cuales son sus estados

cuales son sus interfaces

¿Comparten interfaz?

¿Son polimórficas?

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
Ejercicio 2
Modificar la clase Golondrina vista en la teoría para poder preguntar si una golondrina está en equilibrio. Este equilibrio se alcanza cuando la energía se encuentra entre 150 y 300.

Ejercicio 3
Consideremos que un ornitólogo tiene un conjunto de aves bajo estudio. Cada una de estas aves puede ser un gorrión (del ejercicio 7 de la práctica anterior), o una golondrina. Un ornitólogo somete, cada vez que lo decide, a cada una de las aves que tiene en estudio a una rutina que consiste en: hacerla comer 80 gramos, hacerla volar 70 kms, y finalmente hacerla comer otros 10 gramos. Se propone:

implementar la clase Ornitologo, de forma tal que acepte las operaciones estudiarAve(ave), avesEnEstudio(), realizarRutinaSobreAves(), avesEnEquilibrio(). Realizar rutina es ejecutar la rutina descripta más arriba sobre cada ave que tiene en estudio. Las aves en equilibrio son aquellas aves, entre las que el ornitólogo tiene en estudio, que responden True cuando se les consulta estaEnEquilibrio().

comprobar el código que se escribió con esta secuencia:

definir un ornitólogo, dos golondrinas y dos gorriones,
inicializar las aves con valores conocidos,
decirle al ornitólogo que estudie una de las golondrinas y los dos gorriones,
decirle al ornitólogo que realice su rutina sobre aves,
verificar los valores de las cuatro aves definidas, para las tres que tiene en estudio el ornitólogo estos valores deberían haber cambiado, para la otra ave no.
Ejercicio 4
Vamos a salir de paseo (¡si la pandemia nos deja!). Para esto podemos utilizar como vehículos motos o autos, y de estos dos medios de transporte sabemos que:

comienzan con una cantidad que podemos establecer de combustible

los autos pueden llevar 5 personas como máximo y al recorrer una distancia consumen medio litro de combustible por cada kilómetro recorrido

las motos pueden llevar 2 personas y consumen un litro por kilómetro recorrido;

pueden cargar_combustible en la cantidad que digamos y al hacerlo suben su cantidad de combustible

saben responder si entran una cantidad de personas. Esto sucede cuando esa cantidad es menor o igual al máximo que pueden llevar.

Definí las clases Moto, Auto y MedioDeTransporte y hace que las dos primeras hereden de la tercera.

"""
#arrancoo 1ra

"""

#Ejercicio 1
#Dada la siguiente clase, identificá la interfaz y el estado de la misma:



#Resolucion:

#interfaz->conjunto de métodos:que mensajes entiende la clase, sin importar lo que después hagan(conjunto de mensajes que cada objeto expone)
#interfaz:energia, comer, acariciar, esta debil 

#estados->conjunto de atributos(no importa lo q cambia o lo que valga, no es el estado inicial)
#estados:alimento y caricias 

class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2

#este no es para probar, era solo para responder preguntas teoricas


#Ejercicio 2
#Modificá el método volar de la clase Golondrina visto en la clase de teoría de manera que no pueda volar si al hacerlo,
#la energía toma el valor 0 o valor negativo.

#ej clase teorica:  

class Golondrina:
  def __init__(self, energia):     #energia total con que arrancan
    self.energia = energia

  def comer_alpiste(self, gramos): # suma 4 de energía por alpiste que coma
    self.energia += 4 * gramos     #si precisa parametro

  def volar_en_circulos(self): #las vueltas no precisan parámetro,es 1 vuelta
    self.volar(0)

  def volar(self, kms):     
    if self.energia>10 +kms:       #si tiene energia>10 va a poder volar, dado que al dar una vuelta en circulo le quedara energia aun
      self.energia -= 10 + kms     #que gaste 10 de energía x cada vuelta en circulo                                                   
    else:                          #de lo contrario, con energia <=10, se quedara sin energia luego de volar, por lo tanto no podra volar
      print("no tiene energia para volar") 

#para probarlo ->si tira "None" es q puede volar, de lo contrario printea "no puede"

pepa= Golondrina(100)
pepa.comer_alpiste(3) #energia pasaria a 112 si inicial 100 y gr 3
print(pepa.volar(3)) #quiere volar 3kms ->al ser 112>10+3 va a volar    
print(pepa.energia) #112-13 energia q queda


#aca hay otra prueba en la que no podra volar

#pepa= Golondrina(1)
#pepa.comer_alpiste(2) #energia pasaria a 9 si inicial 1 y gr 2
#print(pepa.volar(3)) #quiere volar 2kms ->al NO SER ser 9>10+2 NO va a volar  ->printea que no puede  
#print(pepa.energia) #devuelve energia que tiene y por la q no podra volar


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




#Ejercicio 7
#Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas como CSS 
# (coeficiente de serenidad silenciosa), CSSP y CSSV (como el CSS pero “pico” y “veces”). 
# El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar, por la cantidad total de gramos de comida que ingiere.
#  El CSSP es la misma división pero considerando solamente lo que voló la vez que más voló y lo que comió la vez que más comió.
#  El CSSV es otra vez la misma idea, respecto de la cantidad de veces que voló y comió. 
# Si un gorrión nunca comió, los coeficientes deben ser None. Un gorrión se considera en equilibrio si su CSS está entre 0.5 y 2.


class Gorrion:
    def __init__(self,grAc,kmAc):
        self.grAc= grAc
        self.kmAc= kmAc
        self.liGr=[] #listas donde se iran sumando los gr  y km   arrancan vacias xq todavia no volo ni comio
        self.liKm=[]

    def comer(self, gr): #le pide los gr q come, los agrego a lista y los sumo a gr actuales
        self.liGr.append(gr) #separa en != elem, las !=cant
        self.grAc+=gr #va sumando los gr de cada vez

    def volar(self, kms): #(mismo q en función de comer)
        self.liKm.append(kms)
        self.kmAc+=kms
    def css(self): #si gr es >0 todo ok y calcula normalmente,                                       
        if self.grAc >0:
            return self.kmAc/self.grAc
        else:                    # en caso que el gr no sea <0 retornara None, con el fin de que no de error por tener denominador 0 o menor
            return None

    def cssp(self):# no necesariamente en misma posición los max, pueden estar en != posiciones
        if self.grAc >0:
            return max(self.liKm)/max(self.liGr)
        else:
            return None

    def cssv(self):
        if self.grAc >0:
            return len(self.liKm)/len(self.liGr)
        else:
            return None

    def enEq(self):
        return 0.5 <= self.css() <=2

#para probarlos
pepita = Gorrion(70, 50) #este hay q poner si o si con parametros que yo quiera

#estos de aca los voy poniendo para que vaya sumando nros a la lista
pepita.comer(50)
pepita.volar(50)
pepita.comer(120)
#este si o si precisaba una lista para probar
print(pepita.cssp())

#para este con el inical bastaba para probar
print(pepita.enEq())
"""
#arrancoo 2da
"""
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



#Ejercicio 2
#Modificar la clase Golondrina vista en la teoría para poder preguntar si una golondrina está en equilibrio. Este equilibrio se alcanza cuando la energía se encuentra entre 150 y 300.


#seria solamente agregarle esa funcion:
def esta_en_equilibrio(self):
    return 150 <= self.energia <= 300



    #Ejercicio 3
#Consideremos que un ornitólogo tiene un conjunto de aves bajo estudio. Cada una de estas aves puede ser un gorrión (del ejercicio 7 de la práctica anterior), o una golondrina. 
# Un ornitólogo somete, cada vez que lo decide, a cada una de las aves que tiene en estudio a una rutina que consiste en: hacerla comer 80 gramos, hacerla volar 70 kms, 
# y finalmente hacerla comer otros 10 gramos. 
# Se propone:
#implementar la clase Ornitologo, de forma tal que acepte las operaciones estudiarAve(ave), avesEnEstudio(), realizarRutinaSobreAves(), avesEnEquilibrio().
#  Realizar rutina es ejecutar la rutina descripta más arriba sobre cada ave que tiene en estudio. 
# Las aves en equilibrio son aquellas aves, entre las que el ornitólogo tiene en estudio, que responden True cuando se les consulta estaEnEquilibrio().
#comprobar el código que se escribió con esta secuencia:
#definir un ornitólogo, dos golondrinas y dos gorriones,
#inicializar las aves con valores conocidos,
#decirle al ornitólogo que estudie una de las golondrinas y los dos gorriones,
#decirle al ornitólogo que realice su rutina sobre aves,
#verificar los valores de las cuatro aves definidas, para las tres que tiene en estudio el ornitólogo estos valores deberían haber cambiado, para la otra ave no.


#clases golondrina y gorrion son de un ej de la guia anterior

class Golondrina:
    def __init__(self, energia):
        self.energia = energia
    def comer_alpiste(self, gramos):
        self.energia += 4 * gramos
    def volar_en_circulos(self):
        self.volar(0)
    def volar(self, kms):
        if self.energia > 0:
            self.energia -= 10 + kms
    def equilibrio(self):
        return 150 < self.energia < 300

class Gorrion:
    def __init__(self,grAc,kmAc):
        self.grAc= grAc
        self.kmAc= kmAc
        self.liGr=[] 
        self.liKm=[]
    def comer_alpiste(self, gr): 
        self.liGr.append(gr) 
        self.grAc+=gr 
    def volar(self, kms): 
        self.liKm.append(kms)
        self.kmAc+=kms
    def css(self): #si gr es >0 todo ok y calcula normalmente,                                       
        if self.grAc >0:
            return self.kmAc/self.grAc
        else:                    # en caso que el gr no sea <0 retornara None, con el fin de que no de error por tener denominador 0 o menor
            return None

    def cssp(self):# no necesariamente en misma posición los max, pueden estar en != posiciones
        if self.grAc >0:
            return max(self.liKm)/max(self.liGr)
        else:
            return None

    def cssv(self):
        if self.grAc >0:
            return len(self.liKm)/len(self.liGr)
        else:
            return None

    def equilibrio(self):
        return 0.5 <= self.css() <=2    


class Ornitologo:
    def __init__(self):
        self.aves=[]

    def esAv(self, ave): #estudiarAve
        self.aves.append(ave)

    def avEnEs(self):
        return self.aves    

    def avEnEq(self): #ave en eq
        return [self.aves[i].equilibrio() for i in range(len(self.aves))]
    # Recorre lista de aves con un for y por cada ave pregunta si esta en equilibrio. 

    def RutAv(self):#rutina ave
        [self.aves[i].comer_alpiste(80) for i in range(len(self.aves))] #recorre lista de aves y hacerles comer #tanto, volar tanto, etc
        [self.aves[i].volar(70) for i in range(len(self.aves))]
        [self.aves[i].comer_alpiste(10) for i in range(len(self.aves))]

pepita = Golondrina(100)
#pepito = Golondrina(200)
roberto = Gorrion(100, 30)
#roberta =Gorrion(200,0)
pepe=Ornitologo()
pepe.esAv(pepita)
pepe.esAv(roberto)
pepe.RutAv()
#pepe.esAv(roberta)
print(pepe.avEnEq())       





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


"""
#ej muy dificil de objetos(final)
"""
#EJ DIFICILICIMO DE FINAL

# Consigna N°2

# *A)* Dado la siguiente clase respondé: ¿Cuál es el nombre de la clase? ¿Cuál es su estado? ¿Qué mensajes entiende el Avatar? 

# Python
# class Avatar():
# 	def __init__(self, energia = 10, elementos, mascota):
# 		self.energia = energia
#         self.elementos = []
#         self.mascota = mascota
     
#     def estado_avatar(self):
#         self.energia -= 8

#     def meditar(self):
# 		self.energia += 1

# 	def comer(self):
#        self.energia += 5
#a)
#clase:avatar
#estado: energia, elementos, mascota
#mensajes: estado_avatar, meditar, comer

# *B)* Vamos a modelar de manera muy simple la mecánica de un nuevo juego Sonic. Como sabemos Sonic acumula puntos (matando enemigos), anillos y vidas, pero en este nuevo juego también tiene energía
#  (la cual empieza en 100, que es la energía máxima) y solo existe un tipo de enemigo con distintas variaciones a las cuales vamos a llamar XS, S, M, L y XL (si, como los talles de ropa)
#  dependiendo de la dificultad que representan (cuantos golpes se necesitan para matarlos). Por cada golpe que da, Sonic pierde energía, la cual le toma un tiempo recuperar,
#  por lo que no puede dar más de 3 golpes seguidos y es más vulnerable a ataques de enemigos. Considerando todo esto Sonic tiene que entender los mensajes:

#  - *agarrarAnillo(cantidad)*, el cual aumenta en cierta cantidad los anillos que tiene Sonic.
#  - *darGolpe()* el cual disminuye en un 30% del total la energía de Sonic. En el caso de no tener la energía necesaria debe aparecer un cartel que diga esto.
#  - *recuperarEnergia(tiempo)* el cual recupera energía desde 10 hasta los 100 puntos en 10 segundos (recupera proporcionalmente si el tiempo es menor y recupera hasta 100 si el tiempo es mayor a 10).
#  - *matarEnemigo(enemigo)* el cual disminuye la energía dependiendo del enemigo y en caso de quedarse con menos energía de la que necesita Sonic pierde el 10% de los anillos 
# (consideramos que Sonic siempre ataca cuando tiene la energía al máximo). Al matar al enemigo gana una cantidad de puntos correspondiente al enemigo
#  (XS: 20 puntos, S: 35 puntos, M: 50 puntos, L: 65 puntos, XL: 80 puntos).

# Definí las clases *Sonic* y *Enemigo* e instancialas (un enemigo S y uno XL) y ejecutá las siguientes líneas:
#aux t = Enemigo(80)     r = Enemigo(30)       sonico = SonicMejorado()

class Sonic:
    def __init__(self):
        self.energia = 100
        self.puntos = 0
        self.anillos = 0
        self.vidas = 0
    
    def agarrarAnillos(self, cantidad):
        self.anillos += cantidad
    
    def darGolpe(self, cantidad): 
        if cantidad > 3:   #no puede dar mas de 3 seguidos
            print("Sonic no puede golpear mas de 3 veces seguidas")
        elif self.energia - 30 * cantidad < 0:  #self.energia-(self.energia*0.3)<=0
            print("Sonic no tiene energia suficiente para dar golpes")
        else:
            self.energia -= 30 * cantidad     #self.energia-=self.energia*0.3
    
    def recuperarEnergia(self, tiempo):
        if tiempo >= 10: #tiempo mayor a 10 retorno 100
            self.energia = 100
        elif self.energia + tiempo * 9 > 100:
            self.energia = 100
        elif self.energia + tiempo * 9 <= 100:
            self.energia += tiempo * 9
        #else:
        #   self.energia+=10*    
        
    def matarEnemigo(self, enemigo):
        if 60 < enemigo.energia <= 80:
            self.darGolpe(3)
            self.puntos += enemigo.energia
            if self.energia < enemigo.energia:
                self.anillos=self.anillos * 0.1 #piernde 10% de anillos
                self.energia = 0
        elif 30 < enemigo.energia <= 60:
            self.darGolpe(2)
            self.puntos += enemigo.energia
            if self.energia < enemigo.energia:
                self.anillos = self.anillos* 0.1
                self.energia = 0
        elif enemigo.energia <= 30:
            self.darGolpe(1)
            self.puntos += enemigo.energia
            if self.energia < enemigo.energia:
                self.anillos = self.anillos* 0.1
                self.energia =0

class SonicMejorado(Sonic):
    def energiaPorAnillos(self, cantidadAnillos):
        self.energia += cantidadAnillos * 0.2

class Enemigo:
    def __init__(self, energia):
        self.energia = energia





 #t = Enemigo(80)           sonico = SonicMejorado()

sonic=Sonic()
r = Enemigo(30)
t = Enemigo(80)


sonic.agarrarAnillos(50)
sonic.matarEnemigo(r)
print(sonic.anillos)
print(sonic.energia)
sonic.recuperarEnergia(10)
print(sonic.energia)
sonic.matarEnemigo(t)
print(sonic.anillos)
print(sonic.energia)
sonic.recuperarEnergia(5)
print(sonic.energia)
# 

# El resultado de esto debería ser:

# 	50
# 	70
# 	100
# 	5.0
# 	0
# 	45.0

# *C)* A medida que avanza el juego Sonic obtiene nuevas habilidades tales como recuperar energía agarrando anillos de manera que recupera 0.2 unidades de energía por cada anillo que agarra. 
# Definí la clase *SonicMejorado* que herede de *Sonic* y que además entienda el mensaje *energiaPorAnillos(cantidadAnillos)* el cual recupere la energía de Sonic como está definido más arriba.
# Ejecutando las siguientes líneas (eliminando la ejecución del inciso *B*):

# python
# sonicMejorado.agarrarAnillos(50)
# sonicMejorado.matarEnemigo(enemigoS)
# print(sonicMejorado.anillos)
# print(sonicMejorado.energia)
# sonicMejorado.recuperarEnergia(10)
# print(sonicMejorado.energia)
# sonicMejorado.matarEnemigo(enemigoXL)
# print(sonicMejorado.anillos)
# print(sonicMejorado.energia)
# sonicMejorado.recuperarEnergia(5)
# print(sonicMejorado.energia)
# sonicMejorado.energiaPorAnillos(50)
# print(sonicMejorado.energia)
# 

# El resultado de esto debería ser:
	
# 	50
# 	70
# 	100
# 	5.0
# 	0
# 	45.0
# 	55.0

"""

