#Ejercicio 7
#Escribí un porgrama que lea un archivo e identifique la palabra más larga,
#  la cual debe imprimir y decir cuantos caracteres tiene.

#def palMasLarga(arch):
palabra=""
maxLong=0 #variable en q vamos poniendo la long d la palabra + larga, arranco con 0 p q pueda comparar
        #aux: si buscara minimo me convendria poner un nro muy pero muy grande
with open(r"C:\ucema_2do_1ro\fundamentos_info\probaratr.txt", "r") as f:
  lista=f.read().split()   #guarda palabras del archivo en una lista separadas cada vez q aparece un espacio
  for word in lista: #para cada palabra en la lista de palabras
    if len(word)>maxLong: #si cant de palabras es la de mayor long 
      maxLong=len(word) #max long pasara a ser la d la palabra q supere a la anterior->aca dice cant de letras de la mayor
      palabra=word #hay q imprimir la palabra x eso vamos anotando cual es la mayor
print("la palabra mas larga es", palabra, "con", maxLong)      