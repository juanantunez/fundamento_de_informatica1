#Ejercicio 1
#Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra 
# (por ejemplo que imprima cuántas líneas no empiezan con "P").

def ocu(letra):
    ocurrencias=[]                    #creo lista vacia para determinar luego la cant
    with open(r"C:\ucema_2do_1ro\fundamentos_info\probar.txt", "r") as lineas:#abrir archivo y leerlo
        for linea in lineas.readlines():#ordena documento en una lista, cada vez q salta de linea cambia de elemento
            if linea[0] != letra:           #si la 1er palabra de la linea no es P
                ocurrencias.append(linea)  #sumo esa linea a la lista   
    print(len(ocurrencias))  

ocu("P")

#ocurrencias=[]                    #creo lista vacia para determinar luego la cant
#with open(r"C:\ucema_2do_1ro\fundamentos_info\probar.txt", "r") as lineas:#abrir archivo y leerlo
 # for linea in lineas.readlines():#ordena documento en una lista, cada vez q salta de linea cambia de elemento
  #  if linea[0] != "P":           #si la 1er palabra de la linea no es P
   #   ocurrencias.append(linea)  #sumo esa linea a la lista   
#print(len(ocurrencias))          #cuento la cantidad lineas que aparecen la lista

#devuelve 3 en este caso xq en el archivo 3 lineas arrancan con una letra distinta a