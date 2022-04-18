#Ejercicio 7
#Creá un programa que declare una lista y la vaya llenando de números leídos por teclado hasta que se introduzca un número negativo. Una vez hecho esto se deben imprimir los elementos de la lista.
li=[]

nro=int(input("ingr: "))
while nro >=0:
  li.append(nro)
  nro=int(input("ingr: "))
print(li)