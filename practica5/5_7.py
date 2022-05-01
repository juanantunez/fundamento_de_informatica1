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


