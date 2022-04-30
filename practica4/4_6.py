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

