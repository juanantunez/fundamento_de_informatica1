def lineadearchivo():
    """
    Funcion que lee un archivo y dice cuantas lineas empiezan con n letra
    """
    with open(r"C:\ucema_2do_1ro\fundamentos_info\probar.txt", "r") as f:
        contador = 0
        for linea in f:
            if not linea.startswith("P"):
                contador += 1
                print(contador)

print(lineadearchivo())

"""
import os
def leer_arch():
    with open (r"\C:\Users\Usuario\Downloads\manipulacion_archivos.txt","r") as mi_arch:
      contador = 0
      for linea in mi_arch:
          if not linea.startswith("P"):
              contador += 1
              print(contador)  

print (leer_arch())

"""