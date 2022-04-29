#Ejercicio 13
#Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.

#no me sale...
import re
def primeros_caracteres(string):
    #sub->(1er:reemplaza las ocurrencias de tal patron,2do:por tal patron, 3er: en un str determinado)
    print(re.sub("\W","_", string, 2))#aux sub->se puede agregar un parametro al final de la funcion sub vcon el numero de veces que queres limitar el remplazo

primeros_caracteres("gu&ju*ju*")    