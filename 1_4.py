#ej 4
#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales en mayúsculas
titulo=input("ingrese:")
palabras=[]
for palabra in str.split(titulo, " "): #cada vez q encuentra un espacio, separa en listas distintas las palabras
    list.append(palabras, str.upper(palabra[0])+palabra[1:]) #a la lista vacia le va agregando a cada palabra de la lista su posicion 0 en mayuscula y el resto en minuscula ya asi con c una d la lista

print(str.join(" ", palabras))     #a la lista formada, la tranformo en una frase, separada por espacios entre cada elemento d la lista q habia