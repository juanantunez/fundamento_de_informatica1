#Ejercicio 14
#Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.

import re
def reemplaza_espa(string):
    print(re.sub(r"\s", ";", string))                     #\s ->Un espacio, de cualquier tipo (\t\n\r\f)

reemplaza_espa("fie ju  ip")