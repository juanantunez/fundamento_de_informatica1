#Ejercicio 3 Escribí un programa que dado un número del 1 al 6, ingresado por teclado, muestre cuál es el número que está en la cara opuesta de un dado. Si el número es menor a 1 y mayor a 6 se debe mostrar un mensaje indicando que es incorrecto el número ingresado.
n= int(input("Ing: "))

if 0<n<7:
  print(7-n)     
else:
  print("error")   