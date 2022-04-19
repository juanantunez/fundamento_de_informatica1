#ej 5
#Realizar un programa que lea tres números por teclado y calcule el promedio de ellos.
n= int(input("cantidad de notas: ")) #cant d notas q voy a ingresar

suma=0 #p suma d notas
i=1 #p controlar ciclo y poder tocar todas lsa notas necesarias
while (i<=n): #mientras i sea menor o igual q la cantidad d notas
  print("ingrese", i) 
  nota=float(input()) #el prom sera decimal quizas
  suma=suma+nota #en la variable suma vamos acumulando las notas
  i+=1 #suma hasta llegar a la cant d notas
prom=suma/n
print("el promedio : ", prom)
