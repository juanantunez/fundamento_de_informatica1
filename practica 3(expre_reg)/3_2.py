#Ejercicio 2 Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.
import re 
def caractPerm(str):
  print(not(re.search("[^a-zA-Z0-9]", str))) #para alistar caracteres que no deben aparecer en un rango, utilizo el "[^rango]"  
                                                  #"not bool" significa que la logica es al revez, retorna True si son todos asi y False si alguno no 
#busca cualquier caracter menos los de ese rango, si encuentra seria True, pero como hay un "not"adelante, es False                                                                                                                             # (poner not o not bool es lo mismo)
caractPerm("abc*23") 
