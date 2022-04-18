#Ejercicio 1 Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.
import re
texto="lorem ipsum dolor sit amet, consectetur adipiscing elit, amet et amet"
patron="[a-zA-Z0-9]"
def prog(patron, texto):
  if re.search(patron, texto): #si patron se encuentra en el texto                 aux:search()->posiciones en q esta el 1er patron (1er posicion a la ultima sin incluir)
    print("verificado")         
  else:
    print("no verificado")  
print(prog(patron, texto))   