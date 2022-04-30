#Ejercicio 4
#Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

#no saleeeeeeeeeee


#def cuenta():
#with open(r"C:\ucema_2do_1ro\fundamentos_info\probar.txt", "r") as file:
   # fileContent=file.readlines()
    #palabras=f.split()
    #print(len(fileContent))

#cuenta()    

with open(r"C:\ucema_2do_1ro\fundamentos_info\probar.txt", "r") as f:
    linea = f.read()
    palabras = linea.split()
    print(len(palabras))    