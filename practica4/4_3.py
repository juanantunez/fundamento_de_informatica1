#Ejercicio 3
#Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.
li=[] 
with open("arch", "r") as f:
  lineas=[linea.split() for linea in f] #separa y guarda elementos de un arch en una lista cada #split separa en distinros elementos dentro de una lista a partir del documento solicitado
for linea in lineas:
  print(linea)  
with open("arch", "r") as f:
  data=f.readlines()[10] #lee en este caso las ultimas 
print(data)   
