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




