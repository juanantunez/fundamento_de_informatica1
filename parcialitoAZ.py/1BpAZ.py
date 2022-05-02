#**Consigna N°1 B** (RE)
#Escribir funcion que, dado un String, permitan obtener:

# - la lista de los substrings delimitados entre ‘aa’ y ‘gg’, que no incluyan ninguna ‘c’.
#  P.ej. en ‘ttaatatggttaacatgg’, debe tomar solamente ‘tat’, rechazando ‘cat’.

import re
def se(tex):
    print(re.findall("aa([^c].*?)gg", tex))
#"."->puede ser cualquier caracter "*"(una o mas)->puede haber 0 o mas d estos caracteres ->prioriza delimitadores externos
                        #al poner "?"(0 o una) ademas del "*"->prioriza los delimitadores internos
                        #y pone de cada lado los str delimitadores,toma el 1ro del 1ro y el 1ro del 2do en caso d ser mas de uno

                        #: [^a-d] busca cualquier carácter menos a, b, c, d. (caracteres que No estan en ese rango)
se("ttaatatggttaacatgg")            