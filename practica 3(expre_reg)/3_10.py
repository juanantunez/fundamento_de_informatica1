#Ejercicio 10
#Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &. 

#DIJO GUILLE QUE ESTE EJ ASI NO VA A A ENTRAR, CON LO Q HICE ALCANZA

def obtener_substring(substring):
    import re
    a = print(re.split("@|&", substring)) #para separar usa "|"
    print (a)

obtener_substring("@hola@ret&hdehde&")
