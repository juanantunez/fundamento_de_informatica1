#ej 5 Creá un programa que pida el número de día de la semana (del 1 al 7) e imprima el nombre correspondiente. Si se ingresa un número fuera de rango tiene que imprimir un mensaje indicando que el número es incorrecto.

#ACLARACION:lo hice para 2 dias para hacerlo mas corto
nro=int(input("ingrese: "))
if 1<=nro<=2:
  if nro==1:
    print("domingo")
  if nro==2:
    print("lunes") 
else:
  print("incorrecto")