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




