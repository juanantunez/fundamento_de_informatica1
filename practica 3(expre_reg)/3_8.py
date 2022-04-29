#Ejercicio 8 Escribí un programa que separe y devuelva los caracteres númericos de un string.
import re
#tex="juans3ito 5 "

def separo(tex):
  for s in re.findall("\d+", tex):#el finadall->p obtener todas las ocurrencias del substring
                                    #/d+ ->donde encuentra uno o mas nros los extrae       #aux:otra es poner el rango numerico
    print(s)
separo("juans3ito 5")    