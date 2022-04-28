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

