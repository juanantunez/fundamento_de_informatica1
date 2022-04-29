#Ejercicio 7
#Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.  
 

#lo resolvi igual que el ej2 de esta guia, solo que adentro del rango deje un espacio y con eso me considera tmbn espacios 
import re 
def caractPerm(str):
  print(not(re.search("[^a-zA-Z0-9 ]", str))) #para alistar caracteres que no deben aparecer en un rango, utilizo el "[^rango]"  
                                                  #"not bool" significa que la logica es al revez, retorna True si son todos asi y False si alguno no 
#busca cualquier caracter menos los de ese rango, si encuentra seria True, pero como hay un "not"adelante, es False                                                                                                                             # (poner not o not bool es lo mismo)
caractPerm("abc 23") 



"""
def stratr(string):
    sin_esp=string.replace(" ","")
    if sin_esp.isalnum():
        return True
    else:
        return False    

print(stratr("hsin3 W"))

"""

"""
def Stringsoloconcaracterespermitidos(string):
    import re
    #import string
    string_sin_espacios = string.replace(" ", "")
    print(bool(re.search(r'[a-z]', string) and re.search(r'[A-Z]', string) and re.search(r"\s", string) and string_sin_espacios.isalnum()))
   # print(a)
Stringsoloconcaracterespermitidos("hola34Q")   
"""


#ACLARACION:duda con el tema de los espacios para poder terminarlo
         
#nombre_y_edad = input("inserte nombre y edad:")
#nombre_y_edad.isspace() #si son todos unicamente espacios          
#nombre_y_edad.isalpha() #"Verdadero" si todos los caracteres de la cadena son alfabetos
#nombre_y_edad.islower()
#nombre_y_edad.isupper()
#nombre_y_edad.isalnum() #si todos caracteres son alafanumericos (letras y num o x separado)  
       