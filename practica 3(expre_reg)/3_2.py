#Ejercicio 2 Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.
import re 
def caractPerm(str):
  return not bool(re.search("[^a-zA-Z0-9]", str)) #para alistar caracteres que no deben aparecer utilizando el "^"", pero como puse "not" significa que la logica es al revez, retorna True si son todos asi y False si alguno no 
                                                                                                                             # (poner not o not bool es lo mismo)
print(caractPerm("abc*23"))  