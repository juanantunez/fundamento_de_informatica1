#**Consigna N°1 A** (RE)
#Escribir funciones que, dado un String, permitan obtener

 #- cuántas veces aparece el string bc9. P.ej. aparece 2 veces en xsabc9cabcb3sabc9, y ninguna en hola amigos mios.

import re
def aparece_string(cadena):
    print(len(re.findall("bc9", cadena)))  
    #dado que findall retorna lista con todas las ocurrencias del substring ej: ["patron", "patron"]
    #al hacer len de esta lista, obtengo la cantidad de veces que aparece el patron

aparece_string("bc9aretbc9")
