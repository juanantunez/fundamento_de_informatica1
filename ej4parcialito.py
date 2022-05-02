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