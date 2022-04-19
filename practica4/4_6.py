#Ejercicio 6
#Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

#elimine saltos d linea "\n" en archivo d entrada y guardar eso en el archivo d salida
def removerNuevaLinea(entrada, salida):
  with open(entrada, "r") as f, open(salida, "w") as s:  #2 archivos abiertos xq nos pide abrir un archivo y escribirlo en otro
    for line in f: #recorro linea a linea el archivo d entrada
      s.write(line.strip("\n")) #escribimos en el arch d salida el arch d entrada pero quitandole los "\n"
removerNuevaLinea("documento", "documento2")     

