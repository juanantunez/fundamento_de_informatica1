#Ejercicio 11
#Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima. (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
import re
li=["Práctica Python", "Práctica C++", "Práctica Fortran"]
def DosP(li):
  for i in li:
    res=re.match("(P\w*)\W(P\w*)", i)#match: si pongo la 1ra palbra y coincide ahi devuelve, si no es la 1ra devuelve nulo 
                                    #si 1ra es P, devuelve P y w*(devulve cualquier caracter alfanumerico que le siga), luego un caracter no alfanumerico y si despues arranca con P, devulve tmbn la siguiente palabra
    if res is not None:   #si esto es es asi devuelve el res
      print(res.group())  # group() para que lo devuelva con su delimitador P coreespondiente
DosP(li)      