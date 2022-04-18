#Ejercicio 13
#Creá un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro creando la función esMultiplo.
n1=int(input("ingre1: "))   #ingreso ambos nros
n2=int(input("ingre2: "))
def esMultiplo(n1, n2):
  if n1%n2==0:              #si el resto entre estos nros es 0 significa q son multiplos
    return True
  else:
    return False
print(esMultiplo(n1,n2))    #printeo para q diga si es true o false