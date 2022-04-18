#Ejercicio 8
#Realizá un programa que declare tres listas lista1, lista2 y lista3, donde las dos primeras listas deben tener cinco enteros cada una, ingresados por teclado y asigne para cada elemento de la lista3 la suma de los elementos de la lista1 y la lista2 (es decir, el primer elemento de la lista3 tiene que ser la suma del primer elemento de la lista1 y el primero de la lista2)
li1=[]
n=int(input("ing: "))
for n in range(0, 4):
  n=int(input("ing: "))
  li1.append(n)
print(f"lista 1 es: {li1}")
li2=[]
n=int(input("ing: "))
for n in range(0, 4):
  n=int(input("ing: "))
  li2.append(n)
print(f"lista 2 es: {li2}") 
li3=[] 
for n in range(0, 4):
  li3.append(li1[n]+li2[n])
print(f"la lista 3 es: {li3}")  