#Ejercicio 12
#Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|).

tex = "Lorem ipsum dolor sit: amet, consectetur_ipsum elit. Amet sit amet."
tex1=tex.replace(" ", "|") #toma el texto origi y lo cambia por tex1, en que cambia los espacio por |
texco=tex1.replace("_", "|") #toma tex1 y lo cambia por texco, en que cambia "_" por |
texcoatr=texco.replace(":", "|")
print(texcoatr)