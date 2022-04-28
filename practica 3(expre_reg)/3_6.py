#Ejercicio 6
#Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada. 
import re
def encuentra(lista, frase):
    for i in lista: #"i" hace referencia a cada elemento de la lista 
        print(bool(re.search(i, frase))) #va fijandose elemento por elemento cual esta en la frase y va retornando bool

encuentra(["hola", "como", "va"], "hola")