#Ejercicio 9
#Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")
import re
tex= "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
fav=tex.split("-")   #separa en elementos distintos dentro de una lista cada vez que encuentra un "-"
print(fav)