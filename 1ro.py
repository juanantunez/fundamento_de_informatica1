
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
        return [self.aves[i].equilibrio() for i in range(len(self.aves))] # Recorre lista de aves con un for y por cada ave pregunta si esta en equilibrio. 

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

