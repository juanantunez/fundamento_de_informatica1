#Ejercicio 10
#Escribí un programa que añada a un archivo dado todos los archivos de texto (.txt) que hayan en una determinada carpeta.
##guardar todos archivos txt en un solo arch, en biblioteca glob y os         
    
import glob
import os
def funcion1(arch, ruta):
  os.chdir(ruta) #chdir para poder ir a donde corresponde
  li_txt=glob.glob("*.txt") #nos quedamos con todos los txt (glob biblio y glob metodo)-> solo los nombre d los arch aparecen
  with open(arch, "a") as s: #abro el archivo y le agrego
    for file in li_txt: 
      file=open(s, "r")        #por c arch en lista txt los abro y lo guardo en la variable file
      s.write(file.read())     #lo escribo y leo 
      file.close()             #lo cierro