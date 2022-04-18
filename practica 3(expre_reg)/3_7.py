#Ejercicio 7
#Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.  

#ACLARACION:duda con el tema de los espacios para poder terminarlo
         
nombre_y_edad = input("inserte nombre y edad:")
nombre_y_edad.isspace() #si son todos unicamente espacios          
nombre_y_edad.isalpha() #"Verdadero" si todos los caracteres de la cadena son alfabetos
nombre_y_edad.islower()
nombre_y_edad.isupper()
nombre_y_edad.isalnum() #si todos caracteres son alafanumericos (letras y num o x separado)         