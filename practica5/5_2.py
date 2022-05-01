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



