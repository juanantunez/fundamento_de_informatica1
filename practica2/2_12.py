#Ejercicio 12 Creá un programa que permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guardá la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno. El programa tiene que pedir el número de alumnos que se va a introducir, luego su nombre y sus notas hasta que introduzcamos un número negativo. Al final el programa tiene que mostrar la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa tiene que dar un error.
cantidad = int(input("introducir cantidad de alumnos: "))
alumnos = {}

for num in range(0, cantidad):#para cant d alumnos indicada
    alumno = input("alumno: ")#ingresar nombre alumno
    notas = []#creo lista con notas
    nota = int(input("nota: "))#ingreso nota
    while nota >= 0:#mientras nota sea >=0 sigue tomando notas d ese alumno, d lo contrario cambio d alumno
        notas.append(nota) #agrego nota del alumno
        nota = int(input("nota: ")) #ingreso otra nota
    alumnos[alumno] = notas #notas d alumno
for alumno in alumnos: # p c alumnoe
  print(alumno, sum(alumnos[alumno])/len(alumnos[alumno])) #imprimo la suma d sus notas dividido la cantidad, lo q me dara la nota media