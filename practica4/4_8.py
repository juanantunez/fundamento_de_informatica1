#Ejercicio 8
#Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

# los 1eros 2 docs q tengo q abrir, los tengo q leer y hay un 3er doc q ya existe 3er, a este le tengo q escribir cosas, le agrego con append
#def joinFiles(file1, file2, file3):
with open(r"C:\ucema_2do_1ro\fundamentos_info\probar.txt", "r") as f1, open(r"C:\ucema_2do_1ro\fundamentos_info\probaratr.txt", "r") as f2, open(r"C:\ucema_2do_1ro\fundamentos_info\3eroacolocar.txt", "a") as f3:
#los 1eros 2 los lee y al 3ero le agregara cosas a lo q ya tiene
  f3.write(f1.read() + f2.read())#le va a agregar al 3ero la suma del 1 y el 2 ->p eso leo estos 2 y los escribo a ambos en el 3ero 

#joinFiles("documento", "documento2", "documento3")    
#vamos a obtener texto f3, abajo f1 y abajo f2