#Ejercicio 9
#Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

def wo(arch):             
  frecuencias={}                 #abro diccio de frecuencias.    frec=veces q aparece tal/total de todas 
  with open(arch, "r") as f:    #abre archivo
    word_list=f.read().split()  #lo lee y le hace split->separa elemento x elemento en una lista
    for i in word_list:         #i(seria la palabra) en la lista de palabras
      if i in frecuencias:      #si i ya aparecio en la lista de frecuencias
        frecuencias[i]+=1       #sumale 1 
      else:
        frecuencias[i]=1       #si no existe asignale una clave y ponelo en el valor1
    for word in frecuencias.keys(): #
      frecuencias[word]=round(frecuencias[word]/len(word_list), 3) #para cada palabra como clave de diccionario(frecuencias)
                                                                    #para frecuencia de la palabra como valor le pongo ->frecuencia el nro d una palabra dividido el nro total de todas las palabras
                                                                    #el 3 hace referencia a los 3 decimales eso se puede poner unicamente si antes hay un round
  print(frecuencias)          
  
  #aux:creo diccionario con la cant de palabras q aparece ->"para"(clave del diccio), si no existe asignale una clave y ponelo en el valor1
