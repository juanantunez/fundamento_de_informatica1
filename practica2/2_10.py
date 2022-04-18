#Ejercicio 10
#Escribí un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena (considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).
contadores={} #diccio donde vamos a guardar apariciones
cadena=input("ingre: ") #pedimos cadena
for caracter in cadena: #voy tomando letra x letra
  if caracter in contadores: #si caracter ya esta en diccio, agrego una
    contadores[caracter]+=1
  else:
    contadores[caracter]=1 #si caracter no estaba en diccio, creo la clave y le asigno uno
for clave, valor in contadores.items():
  print(clave, valor)      #me tiene q dar clave q es letra y valor q es cantidad