#Ejercicio 11
#Modificá el programa anterior para que además imprima los caracteres que no aparecen en la cadena, pero con el valor 0.
contadores={} #diccio donde vamos a guardar apariciones
alfabeto="abcdefghijklmnñopqrstuvwxyz" #ingreso todo el alfabeto
for letra in alfabeto + alfabeto.upper(): #p c letra en el alfabeto ingresado (minuscula) o en mayuscula
  contadores[letra]=0 #da 0 si no aparece letra en diccio
cadena=input("ingre: ") #pedimos cadena 
for caracter in cadena: #voy tomando caracter x caracter ingresado
  if caracter.lower() in alfabeto: #sea mayus o minus lo paso a minus p ver si esta en alfabeto
    contadores[caracter]+=1 #si esta le sumo uno al caracter q corresponda sea a mayu o minu

for clave, valor in contadores.items():
  print(clave, valor)      #me tiene q dar clave q es letra y valor q es cantidad