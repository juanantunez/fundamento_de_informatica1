#Ejercicio 1
#Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").
ocurrencias=[]                    #creo lista vacia para determinar luego la cant
with open ("arch", "r") as lineas:#abrir archivo y leerlo
  for linea in lineas:
    if linea[0] != "P":           #si la 1er palabra de la linea no es P, sumo esa linea a la lista 
      ocurrencias.append(linea)   
print(len(ocurrencias))          #cuanto la cantidad lineas que aparecen la lista