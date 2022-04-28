#Ejercicio 5
#Escribí un programa que diga si un string empieza con un número específico.

#no me sale...
import re
def empieza_con_talnro(string, nro):
    print(bool(re.search("^"+str(nro), string))) #"bool"para que devuelva o true o false
                                                #busca si al ppio de linea("^")esta el nro pasado a str (str(nro))
empieza_con_talnro("3era",3) #si esta retorna true
