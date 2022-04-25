#Ejercicio 2
#Escribí un programa que lea un archivo e imprima las primeras n líneas.
f= open(r"C:\ucema_2do_1ro\fundamentos_info\probaratr.txt","r")    #abre y lee arch
linea=f.readlines()[0:3]   #ordena documentos en una lista, cada vez que salta de linea cambia de elemento->en este caso leera solo 2 elementos
print(linea)