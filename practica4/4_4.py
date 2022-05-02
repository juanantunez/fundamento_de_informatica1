#Ejercicio 4
#Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.


def cuantaspalabrasarchivo():
    with open(r"C:\ucema_2do_1ro\fundamentos_info\probar.txt", "r") as f:
        linea = f.read()  #read() lee archivo completo
        palabras = linea.split() #por el split, separa las palabras por espacios en una lista
        return len(palabras) #cuenta los elementos de la lista

print(cuantaspalabrasarchivo())


