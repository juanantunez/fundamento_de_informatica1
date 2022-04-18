#Ejercicio 14 Creá una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Escribí un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa tiene que pedir el número de días que se van a introducir.
def tempMed(t1, t2):   #para calc la media dadas ambas temps, las sumo y las divido x su cant(2)
  return (t1+t2)/2

cantidad=int(input("cant dias a pedir temps: "))  #pido q ingrese cant de dias a pedir temps
for indice in range(cantidad):   #para cada vuelta dentro del rango de cantidad, pido tmax y tmin
  tmin=float(input("tmin: "))
  tmax=float(input("tmax: "))
  print("tmed: ", tempMed(tmin, tmax))  #imprimo la tmed, citando a funcion anterior con los parametros indicados