#Ejercicio 9
#Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")
import re
def extrae_entre(tex):
    return re.findall("-(.*?)-", tex)#"."->puede ser cualquier caracter "*"(una o mas)->puede haber 0 o mas d estos caracteres ->prioriza delimitadores externos
                        #al poner "?"(0 o una) ademas del "*"->prioriza los delimitadores internos
                        #y pone de cada lado los str delimitadores,toma el 1ro del 1ro y el 1ro del 2do en caso d ser mas de uno
    
   
print(extrae_entre("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"))


#tex= "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
#fav=tex.split("-")   #separa en elementos distintos dentro de una lista cada vez que encuentra un "-"
#print(fav)