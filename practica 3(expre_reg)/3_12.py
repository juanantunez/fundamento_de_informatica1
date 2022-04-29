#Ejercicio 12
#Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|).

def remplazar_por_barra(string):
    import re
    print(re.sub(r"[ _:]", "|", string))
    #sub->(1er:reemplaza las ocurrencias de tal patron,2do:por tal patron, 3er: en un str determinado)

remplazar_por_barra("Lorem ipsum dolor sit: amet, consectetur_ipsum elit. Amet sit amet.")



"""
tex = "Lorem ipsum dolor sit: amet, consectetur_ipsum elit. Amet sit amet."
tex1=tex.replace(" ", "|") #toma el texto origi y lo cambia por tex1, en que cambia los espacio por |
texco=tex1.replace("_", "|") #toma tex1 y lo cambia por texco, en que cambia "_" por |
texcoatr=texco.replace(":", "|")
print(texcoatr)
"""
