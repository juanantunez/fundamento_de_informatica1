#Ejercicio 15
#Realizá un programa que validar si una cuenta de mail está escrita correctamente.



def validar_mail_correcto(mail):
    import re
    valido = bool(re.match("[a-zA-Z0-9]+[-_\.]*[a-zA-Z0-9]@[a-z]{1,9}\.[a-z]{2,4}(\.[a-z]{2-4}){0,1}", mail))           #("(\S+)@(\w+)\.(\w+)", mail))
    #\S+ ->cualquier caracter que no sea un espacio    (\w+)
    #@->"@"
    #\w+ ->cualquier caracter alfanumerico
    #\. ->un "." ->se le pone la barra xq el "." sino tiene otro significado
    #[a-z]{2,4}    ->obtenga entre 2 y 4

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


    