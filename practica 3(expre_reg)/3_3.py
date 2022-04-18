#Ejercicio 3

#Creá un programa que verifique las siguientes condiciones:
#si un string dado tiene una h seguida de ninguna o más e.
#si un string dado tiene una h seguida de una o más e.
#si un string dado tiene una h seguida de una o más e.
#si un string dado tiene una h seguida de dos o tres e.

#ACLARACION:no lo puedo hacer para 1 solo programa (pero por separado obtengo los rstdos)
#1ra
import re 
def hayPatron(str):
  patron="he+"  #en caso que haya he+ -> "+"significa Una o más ocurrencias del patrón ->dice que encuentra "not None"->es True
  if  re.search(patron, str) is not None:
    return "encuentra"
  else:
    return "no encuentra"
print(hayPatron("he")) 

#ult
import re 
def hayPatron(str):
  patron="he{2,3}"  #en caso que haya he+ -> "+"significa Una o más ocurrencias del patrón ->dice que encuentra "not None"->es True
  if  re.search(patron, str) is not None:
    return "encuentra"
  else:
    return "no encuentra"
print(hayPatron("hee"))    