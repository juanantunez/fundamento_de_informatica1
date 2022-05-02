import os, glob #importo estas 2 bibliotecas

def unir(arch):
    os.chdir(r"C:\Users\notebook\OneDrive\Documents\GitHub\fundamento_de_informatica1")  #cambia de carpeta, en este caso a la carpeta indicada en la ruta
    lista_txt=glob.glob("*.txt") #devuelve una lista con todos los archivos que terminen en ".txt"
    with open(arch, "a") as salida: #abre el archivo donde guardara los otros y lo llama "salida", aca es donde sumara los demas por eso "a"de append
        for txt in lista_txt: #para cada archivo que abra dentro de la carpeta indicada, los lee y los llama "archivo"
            with open (txt, "r") as archivo: 
                salida.write(archivo.read()) #en el de "salida escribe todos los archivos de los textos"

unir("acasepo.txt")