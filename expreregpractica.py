
#Parcialitoooooooo
"""
1A
# **Consigna N°1 A** (RE)
#Escribir funciones que, dado un String, permitan obtener

 #- cuántas veces aparece el string bc9. P.ej. aparece 2 veces en xsabc9cabcb3sabc9, y ninguna en hola amigos mios.

import re
def aparece_string(cadena):
    print(len(re.findall("bc9", cadena)))  
    #dado que findall retorna lista con todas las ocurrencias del substring ej: ["patron", "patron"]
    #al hacer len de esta lista, obtengo la cantidad de veces que aparece el patron

aparece_string("bc9aretbc9")

1B
#**Consigna N°1 B** (RE)
#Escribir funcion que, dado un String, permitan obtener:

# - la lista de los substrings delimitados entre ‘aa’ y ‘gg’, que no incluyan ninguna ‘c’.
#  P.ej. en ‘ttaatatggttaacatgg’, debe tomar solamente ‘tat’, rechazando ‘cat’.

import re
def se(tex):
    print(re.findall("aa([^c]*?)gg", tex))
 "*"(una o mas)->puede haber 0 o mas d estos caracteres ->prioriza delimitadores externos
                        #al poner "?"(0 o una) ademas del "*"->prioriza los delimitadores internos
                        #y pone de cada lado los str delimitadores,toma el 1ro del 1ro y el 1ro del 2do en caso d ser mas de uno

                        #: [^a-d] busca cualquier carácter menos a, b, c, d. (caracteres que No estan en ese rango)
se("ttaatatggttaacatgg")            


#"."->puede ser cualquier caracter  NO ES NECESARIO EN ESTE EJ
"""
#otro añoo ej
"""
### Consigna N°3
Escribir una función que, dado un String, permita validar si este se corresponde o no a una fecha (con formato día, mes, año).


def validar_mail_correcto(fecha):
    import re
    valido = bool(re.match(r"[0-9]{2}/[0-9]{2}/[0-9]{4}", fecha))      

    print(valido)

validar_mail_correcto("04/10/2001")

#otra forma
#def validar_si_es_fecha(string):
 #   import re
  #  re.match(r'\d{2}/\d{2}/\d{4}', string)
  """
  #practicasss
"""
Ejercicio 1
Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.

Ejercicio 2
Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.

Ejercicio 3
Creá un programa que verifique las siguientes condiciones:

si un string dado tiene una h seguida de ninguna o más e.

si un string dado tiene una h seguida de una o más e.

si un string dado tiene una h seguida de una o más e.

si un string dado tiene una h seguida de dos o tres e.

Ejercicio 4
Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).

Ejercicio 5
Escribí un programa que diga si un string empieza con un número específico.

Ejercicio 6
Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.

Ejercicio 7
Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.

Ejercicio 8
Escribí un programa que separe y devuelva los caracteres númericos de un string.

Ejercicio 9
Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")

Ejercicio 10
Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &.

Ejercicio 11
Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).

Ejercicio 12
Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|).

Ejercicio 13
Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.

Ejercicio 14
Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.

Ejercicio 15
Realizá un programa que validar si una cuenta de mail está escrita correctamente.
"""
#arrancooooooo
"""

#Ejercicio 1 Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.
import re
texto="lorem ipsum dolor sit amet, consectetur adipiscing elit, amet et amet"
patron="[a-zA-Z0-9]"
def prog(patron, texto):
  if re.search(patron, texto): #si patron se encuentra en el texto        aux:search()->posiciones en q esta el 1er patron (1er posicion a la ultima sin incluir)
    print("verificado")         
  else:
    print("no verificado")  
prog(patron, texto)   


#Ejercicio 2 Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.
import re 
def caractPerm(str):
  print(not(re.search("[^a-zA-Z0-9]", str))) #para alistar caracteres que no deben aparecer en un rango, utilizo el "[^rango]"  
                                                  #"not bool" significa que la logica es al revez, retorna True si son todos asi y False si alguno no 
#busca cualquier caracter menos los de ese rango, si encuentra seria True, pero como hay un "not"adelante, es False                                                                                                                             # (poner not o not bool es lo mismo)
caractPerm("abc*23") 

#Ejercicio 3

#Creá un programa que verifique las siguientes condiciones:
#si un string dado tiene una h seguida de ninguna o más e.
#si un string dado tiene una h seguida de una o más e.
#si un string dado tiene una h seguida de dos o tres e.

#ACLARACION:no lo puedo hacer para 1 solo programa (pero por separado obtengo los rstdos)
#1ra
import re 
def hayPatron(str):
  patron="he*"  #en caso que haya he* -> "a" seguida de "e*"significa cero o más ocurrencias de en este caso "e"patrón 
  if  re.search(patron, str) is not None:#si el search encuentra esto, es decir que no da rstdo nulo ("not None")
    return "encuentra"
  else:
    return "no encuentra"
print(hayPatron("h")) 

#Ejercicio 4
#Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).

import re
def une_(string):
    if re.search("[a-z]_[a-z]", string) is not None:
        return "encuentra"
    else:
        return "no encuentra"    
print(une_("hola_como"))   


#Ejercicio 5
#Escribí un programa que diga si un string empieza con un número específico.

#no me sale...
import re
def empieza_con_talnro(string, nro):
    print(bool(re.search("^"+str(nro), string))) #"bool"para que devuelva o true o false
                                                #busca si al ppio de linea("^")esta el nro pasado a str (str(nro))
empieza_con_talnro("3era",3) #si esta retorna true


#Ejercicio 6
#Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada. 
import re
def encuentra(lista, frase):
    for i in lista: #"i" hace referencia a cada elemento de la lista 
        print(bool(re.search(i, frase))) #va fijandose elemento por elemento cual esta en la frase y va retornando bool

encuentra(["hola", "como", "va"], "hola")


#Ejercicio 7
#Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.  
 

#lo resolvi igual que el ej2 de esta guia, solo que adentro del rango deje un espacio y con eso me considera tmbn espacios 
import re 
def caractPerm(str):
  print(not(re.search("[^a-zA-Z0-9 ]", str))) #para alistar caracteres que no deben aparecer en un rango, utilizo el "[^rango]"  
                                                  #"not bool" significa que la logica es al revez, retorna True si son todos asi y False si alguno no 
#busca cualquier caracter menos los de ese rango, si encuentra seria True, pero como hay un "not"adelante, es False                                                                                                                             # (poner not o not bool es lo mismo)
caractPerm("abc 23") 


#Ejercicio 8 Escribí un programa que separe y devuelva los caracteres númericos de un string.
import re
#tex="juans3ito 5 "

def separo(tex):
  for s in re.findall("\d+", tex):#el finadall->p obtener todas las ocurrencias del substring
                                    #/d+ ->donde encuentra uno o mas nros los extrae       #aux:otra es poner el rango numerico
    print(s)
separo("juans3ito 5")    


#Ejercicio 9
#Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")
import re
def extrae_entre(tex):
    return re.findall("-(.*?)-", tex)#"."->puede ser cualquier caracter "*"(una o mas)->puede haber 0 o mas d estos caracteres ->prioriza delimitadores externos
                        #al poner "?"(0 o una) ademas del "*"->prioriza los delimitadores internos
                        #y pone de cada lado los str delimitadores,toma el 1ro del 1ro y el 1ro del 2do en caso d ser mas de uno
    
   
print(extrae_entre("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"))


#tex= "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
#fav=tex.split("-")   #separa en elementos distintos dentro de una lista cada vez que encuentra un "-"
#print(fav)


#Ejercicio 10
#Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &. 

#DIJO GUILLE QUE ESTE EJ ASI NO VA A A ENTRAR, CON LO Q HICE ALCANZA

def obtener_substring(substring):
    import re
    a = print(re.split("@|&", substring)) #para separar usa "|"
    print (a)

obtener_substring("@hola@ret&hdehde&")



#Ejercicio 11
#Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
import re
#li=["Práctica Python", "Práctica C++", "Práctica Fortran"]
def DosP(li):
  for i in li:
    res=re.match("(P\w*)\W(P\w*)", i)#match: si pongo la 1ra palbra y coincide ahi devuelve, si no es la 1ra devuelve nulo 
                                    #si 1ra es P, devuelve P y luego w*(devulve cualquier caracter alfanumerico que le siga)
                                    #luego un caracter"\W" no alfanumerico
                                    #y si despues arranca con Py luego w*(devulve cualquier caracter alfanumerico que le siga)
    if res is not None:   #si esto es es asi devuelve el res
      print(res.group())  # group() para que lo devuelva con su delimitador P coreespondiente
DosP(["Práctica Python", "Práctica C++", "Práctica Fortran"])      



#Ejercicio 12
#Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|).

def remplazar_por_barra(string):
    import re
    print(re.sub(r"[ _:]", "|", string))
    #sub->(1er:reemplaza las ocurrencias de tal patron,2do:por tal patron, 3er: en un str determinado)

remplazar_por_barra("Lorem ipsum dolor sit: amet, consectetur_ipsum elit. Amet sit amet.")


#Ejercicio 13
#Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.

#no me sale...
import re
def primeros_caracteres(string):
    #sub->(1er:reemplaza las ocurrencias de tal patron,2do:por tal patron, 3er: en un str determinado)
    print(re.sub(r"\W+","_", string, 2))#aux sub->se puede agregar un parametro al final de la funcion sub vcon el numero de veces que queres limitar el remplazo

primeros_caracteres("gu&ju*ju*")    


#Ejercicio 14
#Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.

import re
def reemplaza_espa(string):
    print(re.sub(r"\s", ";", string))                     #\s ->Un espacio, de cualquier tipo (\t\n\r\f)

reemplaza_espa("fie ju  ip")


#Ejercicio 15
#Realizá un programa que validar si una cuenta de mail está escrita correctamente.



def validar_mail_correcto(mail):
    import re
    valido = bool(re.match("[a-zA-Z0-9]+[-_\.]*[a-zA-Z0-9]@[a-z]{1,9}\.[a-z]{2,4}(\.[a-z]{2-4}){0,1}", mail))          

    print(valido)

validar_mail_correcto("juansanlo@gmail.com")

 #aux para entender:   #@->"@" #\. ->un "." ->se le pone la barra xq el "." sino tiene otro significado  #[a-z]{2,4}    ->obtenga entre 2 y 4

"""
