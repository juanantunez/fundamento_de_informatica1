class Golondrina():
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

class Gorrion():
    def __init__(self,grAc,kmAc):
        self.grAc= grAc
        self.kmAc= kmAc
        self.liGr=[] 
        self.liKm=[]
    def comer_alpiste(self, gr): 
        self.liGr.append(gr) 
        self.grAc+=gr 
    def volar(self, kms): 
        self.liKm.append.appen(kms)
        self.kmAc+=kms

class Ornitologo():
    def __init__(self):
        self.lista_aves = []
    def avesEnEstudio(self):
        print(self.lista_aves)
    def estudiarAve(self,ave):
        self.lista_aves.append(ave)
    def realizarRutinaSobreAves(self):
        for ave in self.lista_aves:
            ave.comer_alpiste(80)
            ave.volar(70)
            ave.comer_alpiste(10)
        print("Rutina Realizada para todas las aves")
    def estaEnEquilibrio(self):
        for ave in self.lista_aves:
            if ave.equilibrio:
                return ave 

pepita = Golondrina(100)
pepito = Golondrina(200)
roberto = Gorrion(100,0)
roberta =Gorrion(200,0)
pepe=Ornitologo()
pepe.estudiarAve(pepita)
pepe.estudiarAve(roberto)
pepe.estudiarAve(roberta)
print(pepe.estaEnEquilibrio())