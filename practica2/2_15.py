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





#diccio ya va a tener datos
#funciones necesarias