#Ejercicio 2
#Escribí un programa que lea un archivo e imprima las primeras n líneas.
f= open("arch","r")    #abre y lee arch
linea=f.readlines(2)   #ordena documentos en una lista, cada vez que salta de linea cambia de elemento->en este caso leera solo 2 elementos
print(linea)