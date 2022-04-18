#ej 6
#Dada una cierta cantidad de minutos (ingresada por teclado) hacer un programa que muestre cuántas horas y minutos son. Por ejemplo 150 minutos son 2 horas y 30 minutos.
minutos= int(input("ingrese: "))
horas=minutos // 60
minutos_resto= minutos %60 #lo q me sobra d una hora si la cant supero 60 va a min y por ende seran los unicos min q aparecen en pantalla
print("tiempo: ", horas, "h", minutos_resto, "m")
