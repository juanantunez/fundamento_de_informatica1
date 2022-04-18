#Ejercicio 2 Escribí un programa que pida un número y diga si es positivo, negativo o 0 y además informe si es par o impar (el 0 es un número par).
nro=int(input("ingrese: "))
if nro>0 and nro%2==0:
  print("positivo y par")
elif nro >0 and nro%2!=0:
  print("positivo e impar")  
elif nro <0 and nro%2==0:
  print("negativo y par")
elif nro <0 and nro%2!=0:
  print("negativo e impar")    
else:
  print("0 y par")