#ej 4 parcialitp
#ademas creo 2 archivos txt a mi izq y les escribo cualquier cosa (por separado los creo)->y me creara una carpeta rstdo y un arch q juntara esos 2 txt 
"""
#**Consigna N°4** (Manejo de archivos)

#Escribí un programa que, por un lado, debe crear una nueva carpeta en la posición actual llamada _Resultado_ y, por otro, que lea todos los archivos con extensión `.txt` 
# y escriba el contenido de todos en un único archivo llamado *texto_completo.txt*, que tiene que estar dentro de la carpeta _Resultado_. **NO se pueden usar rutas absolutas**

import os, glob #importo estas 2 bibliotecas

def unir_txt():
    os.mkdir("Resultado")  #La función os.mkdir-> crea un directorio en blanco en el sistema de archivos, en este caso llamado "Resultado"
    lista_txt=glob.glob("*.txt") #devuelve una lista con todos los archivos que terminen en ".txt"
    with open("Resultado/texto_completo.txt", "a") as salida:
        for txt in lista_txt:
            with open (txt, "r") as archivo:
                salida.write(archivo.read())

unir_txt()
"""
#ej de ruta relativa con un ej de la guia, cree un txt que se llama hi.txt y cuando lo probe le agregue el .\ para que quede mejor, pero solo tmbn va
"""
def hol(archivo):
    palabra=""
    maxLong=0 #variable en q vamos poniendo la long d la palabra + larga, arranco con 0 p q pueda comparar
            #aux: si buscara minimo me convendria poner un nro muy pero muy grande
    with open(archivo, "r") as f:
        lista=f.read().split()   #guarda palabras del archivo en una lista separadas cada vez q aparece un espacio
        for word in lista: #para cada palabra en la lista de palabras
            if len(word)>maxLong: #si cant de palabras es la de mayor long 
                maxLong=len(word) #max long pasara a ser la d la palabra q supere a la anterior->aca dice cant de letras de la mayor
                palabra=word #hay q imprimir la palabra x eso vamos anotando cual es la mayor
                print("la palabra mas larga es", palabra, "con", maxLong)  

print(hol(".\hi.txt")) #al meterle ".\" es una ruta relativa

"""
#practicas
"""
Ejercicio 1
Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").

Ejercicio 2
Escribí un programa que lea un archivo e imprima las primeras n líneas.

Ejercicio 3
Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

Ejercicio 4
Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

Ejercicio 5
Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

Ejercicio 6
Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

Ejercicio 7
Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.

Ejercicio 8
Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

Ejercicio 9
Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

Ejercicio 10
Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.
"""
#arrancooo

"""
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


#Ejercicio 2
#Escribí un programa que lea un archivo e imprima las primeras n líneas.

#with open(r"C:\ucema_2do_1ro\fundamentos_info\probar.txt","r") as lineas: #abre y lee arch
   #print(lineas.readlines()[0:2])   #ordena documentos en una lista, cada vez que salta de linea cambia de elemento
                                    #en este caso leera solo 2 elementos

def imprima(nro):
    with open(r"C:\ucema_2do_1ro\fundamentos_info\probar.txt","r") as lineas: #abre y lee arch
        print(lineas.readlines()[0:nro]) 

imprima(2)


#Ejercicio 3
#Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.


def ult(n):
  with open(r"C:\ucema_2do_1ro\fundamentos_info\probar.txt", "r") as f:
    print(f.readlines()[-n:]) #[-2:] anteultima posicion hasta el final 
ult(2)    


#Ejercicio 4
#Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.


def cuantaspalabrasarchivo():
    with open(r"C:\ucema_2do_1ro\fundamentos_info\probar.txt", "r") as f:
        linea = f.read()  #read() lee archivo completo
        palabras = linea.split() #por el split, separa las palabras por espacios en una lista
        return len(palabras) #cuenta los elementos de la lista

print(cuantaspalabrasarchivo())



#Ejercicio 5
#Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

#from asyncore import write

def remplazar_letra(letra):
    import re
    with open(r"C:\ucema_2do_1ro\fundamentos_info\probar.txt", "r") as f:
        linea = f.read() #Lee al archivo completo con read() 
        lineas = linea.replace(letra, letra + "\n")#remplaza toda las letras por esa letra y un salto de linea
        with open(r"C:\ucema_2do_1ro\fundamentos_info\probaratr.txt", "w") as f2:#2do arch en q lo escribe
            return f2.write(lineas)

print(remplazar_letra("u"))




#Ejercicio 6
#Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

#elimine saltos d linea "\n" en archivo d entrada y guardar eso en el archivo d salida


#ACLARACION: en este caso no hice funcion xq no tenia argumento xq sino se complica con los r"archivo no los lee
#ana dijo q es problema en windows algo asi

#def removerNuevaLinea():
with open(r"C:\ucema_2do_1ro\fundamentos_info\probaratr.txt", "r") as f, open(r"C:\ucema_2do_1ro\fundamentos_info\probar.txt", "w") as s:  #2 archivos abiertos xq nos pide abrir un archivo y escribirlo en otro
  for line in f: #recorro linea a linea el archivo d entrada
    s.write(line.strip("\n")) #escribimos en el arch d salida el arch d entrada pero quitandole los "\n"
                              #strip ->elimina espacios extremos (\n son los cambio de linea)
#print(removerNuevaLinea())     


#ejemplo de uso de strip    ".hola.".strip(".") ->"hola"



#Ejercicio 7
#Escribí un porgrama que lea un archivo e identifique la palabra más larga,
#  la cual debe imprimir y decir cuantos caracteres tiene.

#def palMasLarga(arch):
palabra=""
maxLong=0 #variable en q vamos poniendo la long d la palabra + larga, arranco con 0 p q pueda comparar
        #aux: si buscara minimo me convendria poner un nro muy pero muy grande
with open(r"C:\ucema_2do_1ro\fundamentos_info\probaratr.txt", "r") as f:
  lista=f.read().split()   #guarda palabras del archivo en una lista separadas cada vez q aparece un espacio
  for word in lista: #para cada palabra en la lista de palabras
    if len(word)>maxLong: #si cant de palabras es la de mayor long 
      maxLong=len(word) #max long pasara a ser la d la palabra q supere a la anterior->aca dice cant de letras de la mayor
      palabra=word #hay q imprimir la palabra x eso vamos anotando cual es la mayor
print("la palabra mas larga es", palabra, "con", maxLong)      



#Ejercicio 8
#Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

# los 1eros 2 docs q tengo q abrir, los tengo q leer y hay un 3er doc q ya existe 3er, a este le tengo q escribir cosas, le agrego con append
#def joinFiles(file1, file2, file3):
with open(r"C:\ucema_2do_1ro\fundamentos_info\probar.txt", "r") as f1, open(r"C:\ucema_2do_1ro\fundamentos_info\probaratr.txt", "r") as f2, open(r"C:\ucema_2do_1ro\fundamentos_info\3eroacolocar.txt", "a") as f3:
#los 1eros 2 los lee y al 3ero le agregara cosas a lo q ya tiene
  f3.write(f1.read() + f2.read())#le va a agregar al 3ero la suma del 1 y el 2 ->p eso leo estos 2 y los escribo a ambos en el 3ero 

#joinFiles("documento", "documento2", "documento3")    
#vamos a obtener texto f3, abajo f1 y abajo f2



#Ejercicio 9
#Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. 
# Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

#def wo(arch):             
frecuencias={}                 #abro diccio de frecuencias.    frec=veces q aparece tal/total de todas 
with open(r"C:\ucema_2do_1ro\fundamentos_info\probaratr.txt", "r") as f:    #abre archivo
  word_list=f.read().split()  #lo lee y le hace split->separa elemento x elemento en una lista
  for i in word_list:         #i(seria la palabra) en la lista de palabras
    if i in frecuencias:      #si i ya aparecio en la lista de frecuencias
      frecuencias[i]+=1       #sumale 1 
    else:
      frecuencias[i]=1       #si no existe asignale una clave y ponelo en el valor1
  for word in frecuencias.keys(): #
    frecuencias[word]=round(frecuencias[word]/len(word_list), 3) #para cada palabra como clave de diccionario(frecuencias)
                                                                  #para frecuencia de la palabra como valor le pongo ->frecuencia el nro d una palabra dividido el nro total de todas las palabras
                                                                  #el 3 hace referencia a los 3 decimales eso se puede poner unicamente si antes hay un round
  print(frecuencias)          
  
  #aux:creo diccionario con la cant de palabras q aparece ->"para"(clave del diccio), si no existe asignale una clave y ponelo en el valor1




#Ejercicio 10
#Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.
##guardar todos archivos txt en un solo arch, en biblioteca glob y os         



import os, glob #importo estas 2 bibliotecas

def unir():
    os.chdir(r"C:\ucema_2do_1ro\carpeta de txt")  #cambia de carpeta, en este caso a la carpeta indicada en la ruta
    lista_txt=glob.glob("*.txt") #devuelve una lista con todos los archivos que terminen en ".txt"
    with open(r"C:\ucema_2do_1ro\carpeta de txt\acaaaaaaaaa.txt", "a") as salida: #abre el archivo donde guardara los otros y lo llama "salida", aca es donde sumara los demas por eso "a"de append
        for txt in lista_txt: #para cada archivo que abra dentro de la carpeta indicada, los lee y los llama "archivo"
            with open (txt, "r") as archivo: 
                salida.write(archivo.read()) #en el de "salida escribe todos los archivos de los textos"

unir()



"""