#Ejercicio 15
#Realizá un programa que validar si una cuenta de mail está escrita correctamente.



def validar_mail_correcto(mail):
    import re
    valido = bool(re.match("(\S+)@(\w+)\.(\w+)", mail))
    #\S+ ->cualquier caracter que no sea un espacio    (\w+)
    #@->"@"
    #\w+ ->cualquier caracter alfanumerico
    #\. ->un "."

    print(valido)

validar_mail_correcto("juansanlo@gmail.com")

"""\S busca cualquier caracter menos espacio, @ busca el arroba
despues solo puede recibir caracter alfanumerico ppor eso el \w
despues . y despues de nuevo \w. los + son para que busque una o mas veces

def validar_mail_correcto(mail):
    import re
    valido = bool(re.match(r'(\S+)@(\w+).(\w+)', mail))
    print(valido)
"[w+_-]@[\w+]\.[a-z]"
    [\d+]
"""


    