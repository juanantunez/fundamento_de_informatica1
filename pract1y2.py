#practica1
"""
Ejercicio 1
Escribir un programa que imprima la longitud de un string el cual se lee por teclado.

Ejercicio 2
Realizar un programa donde se imprima la 5ta y 6ta letra de un string pasado por teclado en mayúscula (Asegurarse de que el string tenga la cantidad de caracteres suficientes).

Ejercicio 3
Escribir un programa que pregunte el nombre y apellido al usuario y lo salude.

Ejercicio 4
Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales en mayúsculas

Ejercicio 5
Realizar un programa que lea tres números por teclado y calcule el promedio de ellos.

Ejercicio 6
Dada una cierta cantidad de minutos (ingresada por teclado) hacer un programa que muestre cuántas horas y minutos son. Por ejemplo 150 minutos son 2 horas y 30 minutos.

Ejercicio 7
Un comerciante, el cual tiene un sueldo base, recibe un 10% extra por comisión por cada venta que realiza. Realizar un programa que devuelva el dinero que recibirá por comisión luego de 4 ventas y el total de dinero que ganará ese mes, teniendo en cuenta estas ventas y su sueldo base.

Ejercicio 8
Escribir un programa para calcular la nota final de un estudiante, teniendo en cuenta que por cada respuesta correcta el estudiante suma 4 puntos, por cada incorrecta se le resta 1 punto y si la respuesta está en blanco no se le suma ni se le resta.

Ejercicio en grupo I - Compra de una casa
Uno de los sueños comunes entre las personas sin duda es poder tener una casa propia, sin embargo (en general) no es algo muy sencillo, ya que hay que ahorrar bastante solo para el depósito de la casa. En este ejercicio hay que determinar cuánto tiempo tomaría ahorrar la cantidad suficiente de dinero para pagar el depósito. Para esto vamos a tomar algunas suposiciones:

Llamemos al valor de la casa costo_total.
El porcentaje de este costo que se corresponde con el depósito será porcentaje_deposito. Para este caso el porcentaje va a ser de 25%.
La cantidad actual de ahorros, cantidad_ahorrada, empezará en 0.
Consideremos que se realiza una inversión del dinero ahorrado por la cual se obtiene cierta ganancia, g, por año (es decir, por mes se obtendrían cantidad_ahorrada multiplicada por g/12). Supongamos que por esta inversión se gana 4% (g = 0.04).
El sueldo anual será sueldo_anual.
La cantidad que se ahorra por mes será porcentaje_ahorrado, el cual debe ser expresada como un valor decimal del sueldo mensual (si es 10%, este porcentaje será 0.1)
Por último, al sueldo mensual lo llamaremos sueldo_mensual (sueldo_anual/12)
El programa debe calcular cuantos meses tomaría ahorrar el dinero necesario para pagar el depósito. Este programa debe preguntarle al usuario cual es su sueldo anual, que porcentaje del sueldo quiere ahorrar por mes y cual es el costo de la casa en cuestión.

Para este problema se va a asumir que el usuario va a introducir valores válidos para las variables (es decir, no van a ingresar un string en el valor de la casa).

"""
#practica2
"""

Alternativa condicional
Ejercicio 1
Creá un programa que lea una cadena por teclado y compruebe si la primer letra es mayúscula o minúscula.

Ejercicio 2
Escribí un programa que pida un número y diga si es positivo, negativo o 0 y además informe si es par o impar (el 0 es un número par).

Ejercicio 3
Escribí un programa que dado un número del 1 al 6, ingresado por teclado, muestre cuál es el número que está en la cara opuesta de un dado. Si el número es menor a 1 y mayor a 6 se debe mostrar un mensaje indicando que es incorrecto el número ingresado.

Ejercicio 4
Una compañía de transporte internacional tiene servicio en algunos países de América del Sur, América Central, América del Norte, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido, tal como se muestra en la tabla:

Zona	Ubicación	Costo/gramo
1	América del Sur	10.00 dólares
2	América Central	15.00 dólares
3	América del Norte	18.00 dólares
4	Europa	24.00 dólares
5	Asia	30.00 dólares
Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad. Realizá un programa para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.

Ejercicio 5
Creá un programa que pida el número de día de la semana (del 1 al 7) e imprima el nombre correspondiente. Si se ingresa un número fuera de rango tiene que imprimir un mensaje indicando que el número es incorrecto.

Listas
Ejercicio 6
Creá una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copiá los elementos de la lista en otra lista pero en orden inverso, imprimí los elementos de esta última lista.

Recordá que la manera de copiar una lista en otra es:

lista2 = list(lista1)
Ejercicio 7
Creá un programa que declare una lista y la vaya llenando de números leídos por teclado hasta que se introduzca un número negativo. Una vez hecho esto se deben imprimir los elementos de la lista.

Ejercicio 8
Realizá un programa que declare tres listas lista1, lista2 y lista3, donde las dos primeras listas deben tener cinco enteros cada una, ingresados por teclado y asigne para cada elemento de la lista3 la suma de los elementos de la lista1 y la lista2 (es decir, el primer elemento de la lista3 tiene que ser la suma del primer elemento de la lista1 y el primero de la lista2)

Ejercicio 9
Hacé un programa que guarde los nombres y la edades de los alumnos de un curso. Se debe introducir el nombre y la edad de cada alumno por teclado. El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*). Al finalizar se deben mostrar los siguientes datos:

La edad máxima de todos los alumnos.
Los alumnos que tengan la edad máxima
Diccionarios
Ejercicio 10
Escribí un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena (considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).

Ejercicio 11
Modificá el programa anterior para que además imprima los caracteres que no aparecen en la cadena, pero con el valor 0.

Ejercicio 12
Creá un programa que permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guardá la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno. El programa tiene que pedir el número de alumnos que se va a introducir, luego su nombre y sus notas hasta que introduzcamos un número negativo. Al final el programa tiene que mostrar la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa tiene que dar un error.

Funciones
Ejercicio 13
Creá un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro creando la función esMultiplo.

Ejercicio 14
Creá una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Escribí un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa tiene que pedir el número de días que se van a introducir.

Ejercicio 15
Creá un programa para gestionar datos de los socios de un club, el cual permita:

Cargar la información de los socios en un diccionario para acceder por número de socio. Los datos que se deben almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al dia (s/n) (el programa tiene que dejar de cargar cuando se ingrese el número 0). El programa debe iniciar con los datos de los socios fundadores ya cargados, los cuales son:

Socio número 1, Florencia Ocampo, ingresó el 14/09/2001, cuota al día

Socio número 2, David Estévez, ingresó el 14/09/2001, cuota al día

Socio número 3, Sofía Cáceres, ingresó el 14/09/2001, cuota al día

Informar la cantidad de socios que tiene el club.

Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas.

Modificar la fecha de ingreso de todos los socios ingresados el 21/10/2017, indicando que en realidad ingresaron el 22/10/2017.

Solicitar el nombre y apellido d eun socio y darlo de baja (eliminarlo del listado).

Imprimir el listado de socios completos.

Definir las funciones que creas necesarias.
"""
#arranco1ra
"""
#ej 1
# Escribir un programa que imprima la longitud de un string el cual se lee por teclado.
pal=input("ing: ")
print(len(pal))

#ej 2
#Realizar un programa donde se imprima la 5ta y 6ta letra de un string pasado por teclado en mayúscula (Asegurarse de que el string tenga la cantidad de caracteres suficientes).
pal=input("ing:")
print(pal[4:6].upper())


#ej 3
#Escribir un programa que pregunte el nombre y apellido al usuario y lo salude.
a= input("Ing: ")
print("hola {}".format(a))


#ej 4
#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales en mayúsculas
titulo=input("ingrese:")
palabras=[]
for palabra in str.split(titulo, " "): #cada vez q encuentra un espacio, separa en listas distintas las palabras
    list.append(palabras, str.upper(palabra[0])+palabra[1:]) #a la lista vacia le va agregando a cada palabra de la lista su posicion 0 en mayuscula y el resto en minuscula ya asi con c una d la lista

print(str.join(" ", palabras))     #a la lista formada, la tranformo en una frase, separada por espacios entre cada elemento d la lista q habia

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

#ej 6
#Dada una cierta cantidad de minutos (ingresada por teclado) hacer un programa que muestre cuántas horas y minutos son. Por ejemplo 150 minutos son 2 horas y 30 minutos.
minutos= int(input("ingrese: "))
horas=minutos // 60
minutos_resto= minutos %60 #lo q me sobra d una hora si la cant supero 60 va a min y por ende seran los unicos min q aparecen en pantalla
print("tiempo: ", horas, "h", minutos_resto, "m")


#ej 7
#Un comerciante, el cual tiene un sueldo base, recibe un 10% extra por comisión por cada venta que realiza. Realizar un programa que devuelva el dinero que recibirá por comisión luego de 4 ventas y el total de dinero que ganará ese mes, teniendo en cuenta estas ventas y su sueldo base.
CANTIDAD_VENTAS = 4
COMISION        = 0.10
totalComision   = 0.0

sueldoBase = float(input('Ingrese sueldo base $')) #ingreso sueldo base
for venta in range(CANTIDAD_VENTAS): #para cada una d las 4 ventas
    print('Ingrese monto de la venta No. {0} '.format(venta+1),end='$') #voy ingresando x teclado monto correspondiente a c venta, va recorriendo c venta
    venta = float(input()) #ingreso d cuanto fue la venta x teclado
    totalComision += (COMISION)*venta #com tot va a sumar cada comision (hace el 10% d c venta) y recorre
    print("Las ganancias de comision son ${0:.2f}".format(totalComision))#hasta 2 nros despues de la ,
    print("y el total es ${}".format(totalComision+sueldoBase ))


    #ej 8
#Escribir un programa para calcular la nota final de un estudiante, teniendo en cuenta que por cada respuesta correcta el estudiante suma 4 puntos, por cada incorrecta se le resta 1 punto y si la respuesta está en blanco no se le suma ni se le resta.
totalPreguntas = int(input('Ingrese el total de preguntas: '))
totalCorrectas = int(input('Ingrese cantidad respuestas correctas: '))
totalIncorrectas = int(input('Ingrese cantidad respuestas incorrectas: '))
notaFinal = 4*totalCorrectas - totalIncorrectas
print(f"La calificacion final es: {notaFinal}")

#ej9 no se hace..

"""
#arranco2da
"""
#Ejercicio 1 Creá un programa que lea una cadena por teclado y compruebe si la primer letra es mayúscula o minúscula.
i=input("ingrese: ")
if i[0]. islower():
  print("minuscula")
else: 
  print("mayuscula") 

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

  #Ejercicio 3 Escribí un programa que dado un número del 1 al 6, ingresado por teclado, muestre cuál es el número que está en la cara opuesta de un dado. Si el número es menor a 1 y mayor a 6 se debe mostrar un mensaje indicando que es incorrecto el número ingresado.
n= int(input("Ing: "))

if 0<n<7:
  print(7-n)     
else:
  print("error")   


  #ej 4: Una compañía de transporte internacional tiene servicio en algunos países de América del Sur, América Central, América del Norte, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido, tal como se muestra en la tabla:
#Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad. Realizá un programa para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.
peso=int(input("ingrese peso: "))
ubi=input("ingrese ubicacion: ")
if peso <=5000:
  if ubi=="Asur":
    print(f"A sur {peso*10}")
  if ubi=="Acen":
    print(f"A cen {peso*15}")
  if ubi=="Anor":  
    print(f"A nor {peso*18}")
  if ubi=="eur":  
    print(f"eur {peso*24}")
  if ubi =="asi":  
    print(f"asi {peso*30}")
  else:
    print("codigo invalidor")  
else:
  print("no es posible")  


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

  #Ejercicio 6
#Creá una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copiá los elementos de la lista en otra lista pero en orden inverso, imprimí los elementos de esta última lista.
#Recordá que la manera de copiar una lista en otra es:
#lista2 = list(lista1)
lista1=[]
for i in range(5): 
  lista1.append(input("ingrese el: "))
lista2 = list(lista1)
lista2.reverse()
print(lista2)


#Ejercicio 7
#Creá un programa que declare una lista y la vaya llenando de números leídos por teclado hasta que se introduzca un número negativo. Una vez hecho esto se deben imprimir los elementos de la lista.
li=[]

nro=int(input("ingr: "))
while nro >=0:
  li.append(nro)
  nro=int(input("ingr: "))
print(li)

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


#ej9 no sale

#Ejercicio 10
#Escribí un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena (considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).
contadores={} #diccio donde vamos a guardar apariciones
cadena=input("ingre: ") #pedimos cadena
for caracter in cadena: #voy tomando letra x letra
  if caracter in contadores: #si caracter ya esta en diccio, agrego una
    contadores[caracter]+=1
  else:
    contadores[caracter]=1 #si caracter no estaba en diccio, creo la clave y le asigno uno
for clave, valor in contadores.items():
  print(clave, valor)      #me tiene q dar clave q es letra y valor q es cantidad

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


  #Ejercicio 12 Creá un programa que permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guardá la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno. El programa tiene que pedir el número de alumnos que se va a introducir, luego su nombre y sus notas hasta que introduzcamos un número negativo. Al final el programa tiene que mostrar la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa tiene que dar un error.
cantidad = int(input("introducir cantidad de alumnos: "))
alumnos = {}

for num in range(0, cantidad):#para cant d alumnos indicada
    alumno = input("alumno: ")#ingresar nombre alumno
    notas = []#creo lista con notas
    nota = int(input("nota: "))#ingreso nota
    while nota >= 0:#mientras nota sea >=0 sigue tomando notas d ese alumno, d lo contrario cambio d alumno
        notas.append(nota) #agrego nota del alumno
        nota = int(input("nota: ")) #ingreso otra nota
    alumnos[alumno] = notas #notas d alumno
for alumno in alumnos: # p c alumnoe
  print(alumno, sum(alumnos[alumno])/len(alumnos[alumno])) #imprimo la suma d sus notas dividido la cantidad, lo q me dara la nota media


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

#Ejercicio 14 Creá una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Escribí un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa tiene que pedir el número de días que se van a introducir.
def tempMed(t1, t2):   #para calc la media dadas ambas temps, las sumo y las divido x su cant(2)
  return (t1+t2)/2

cantidad=int(input("cant dias a pedir temps: "))  #pido q ingrese cant de dias a pedir temps
for indice in range(cantidad):   #para cada vuelta dentro del rango de cantidad, pido tmax y tmin
  tmin=float(input("tmin: "))
  tmax=float(input("tmax: "))
  print("tmed: ", tempMed(tmin, tmax))  #imprimo la tmed, citando a funcion anterior con los parametros indicados


  #Ejercicio 15
#Creá un programa para gestionar datos de los socios de un club, el cual permita:
#1ra : Cargar la información de los socios en un diccionario para acceder por número de socio. Los datos que se deben almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al dia (s/n) (el programa tiene que dejar de cargar cuando se ingrese el número 0). El programa debe iniciar con los datos de los socios fundadores ya cargados, los cuales son:
#Socio número 1, Florencia Ocampo, ingresó el 14/09/2001, cuota al día
#Socio número 2, David Estévez, ingresó el 14/09/2001, cuota al día
#Socio número 3, Sofía Cáceres, ingresó el 14/09/2001, cuota al día
#2da : Informar la cantidad de socios que tiene el club.
#3ra : Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas.
#4ta : Modificar la fecha de ingreso de todos los socios ingresados el 21/10/2017, indicando que en realidad ingresaron el 22/10/2017.
#5ta : Solicitar el nombre y apellido d eun socio y darlo de baja (eliminarlo del listado).
#6ta : Imprimir el listado de socios completos.
#Definir las funciones que creas necesarias.

#Cargar la información(consigna 1)
def cargarSocios(socios): #reciba como parametro un socio en q se van a almacenar datos #p agrupar datos d persona ej nombre: juan ->p esto tengo q crear un diccionario
  nro=int(input("n d socio: ")) #acceder a info x nro d socio 
  while nro!=0:  #mientras ingrese nro !=0 sigue pidiendo datos d socios, una vez q se ingresa 0 ya no se pueden cargar mas nros
    nombre=input("ingrese nombe: ") #ingreso datos
    fecha=input("ingrese fecha: ")
    cuota=input("ingrese cuota: ")
    pago=cuota.lower()=="s"                    #no entiendoooo
    socios[nro]=[nombre, fecha, pago] #le cargo a ese nro d socio, lo datos
    nro=int(input("n d socio: ")) #en caso d ser !=0 vuelvo a pedir otro n d socio
  return socios    #esto debe retornar el diccionario socios

 #def numeroSocio #c entrada al diccio va a ser un socio. p saber cant total d socios del club->hacemos un len del diccio(no requiere f)  
def modificarFecha(socios, fechaAnterior, fechaNueva): # Modificar la fecha de ingreso (consina 4)
  for datos in socios.values(): #entra a los valores q son la lista de datos d cada socio q se encuentra dentro del diccio
    if datos[1]==fechaAnterior: #si el dato en posicion 1 q es la fecha (recordar q en posicion en lista se cuenta a partir d 0 es la fecha anterior)
      datos[1]==fechaNueva #la modifica x una nueva, d lo contrario no hace nada
  return socios    

def numeroSocio(socios, nombre): #consigna 5
  for nro, datos in socios.items(): #mirar en socios cada conjunto d datos del diccionario(lo q hay en c lista) a partir de ver clave(nro) y valor (datos)
    if datos[0].lower()==nombre.lower(): #si dato d posicion 0 es igual al nombre 
      return nro

def formatoFecha(fecha): #emprolija
  return fecha[:2]+"/"+fecha[2:4]+"/"+fecha[4:]   #del ppio a posicion 2 sin contar , barra, d 2 a 4 sin contar, barra y d 4 ahasta el final->todo esto p q quede bien formateada la fecha
def imprimirListado(socios): #consigna 6
  for nro, datos in socios.items(): #recorro diccio x clave valor
    print("numero: ", nro) #nro q es clave
    print("nombre: ", datos[0]) #valor en posicion 0 d la lista
    print("fecha d ingreso: ", formatoFecha(datos[1])) #valor en posicion 1 d la lista, formateado d la forma q la funcion anterior lo especifica
    if datos[2]: #si es true, q devuelva al dia, sino q esta en deuda
      print("cuota al dia")
    else:
      print("en deuda")  
    print(".......")
  return None

socios_activos={1: ["Florencia Ocampo", "14092001", True], 2:["David Estévez","14092001", True], 3:["Sofía Cáceres", "14092001", True]}        #datos ya cargados y donde despues agrego (es diccio general)

print("cargar socios")
socios_activos=cargarSocios(socios_activos) #a socios_activos diccionario ya existente le voy cargando socios con la funcion cargarSocios q es a 1ra q cree y esto lo guardo en la ya existente socios_activos

#informar la cantidad de socios que tiene el club (consigna 2)
print("el club tiene", len(socios_activos), "socios")     #p poner la cantidad d socios del club hacemos un len-> c entrada al diccio va a ser un socio

print("registrar pago d cuotas") #Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas (consigna 3)
nro=int(input("nro d socio: "))
socios_activos[nro][2]=True #al nro d socio indicado en la posicion 2 d la lista le da True (q tiene las cuotas al dia)  

print("modifico fecha d ingreso...") 
socios_activos=modificarFecha(socios_activos, "21102017", "22102017") #prueba  modificar fecha cambiandola (sigue consigna 4)

print("eliminar socio") #(sigue consigna 5)
nombre=input("nombre y apellido: ")
nro= numeroSocio(socios_activos, nombre) #por el nombre ya obtenemos el nro y lo eliminamos del diccio con la funcion del
del socios_activos[nro]

imprimirListado(socios_activos) #(sigue consigna 6 )

"""