#Ejercicio 4
#Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).

import re
def une_(string):
    if re.search("[a-z]_[a-z]", string) is not None:
        return "encuentra"
    else:
        return "no encuentra"    
print(une_("hola_como"))    
    
