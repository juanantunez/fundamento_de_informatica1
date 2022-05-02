#**Consigna N°3** (Manejo de exepciones)
#Ejecutá el script_misterioso.py y realizá resolvé:
#    1. ¿Qué tipo de exepción arroja la corrida del script? 
#    2. Mejorá el código para que capture dicho error específicamente y lo maneje imprimiendo una advertencia al usuario sobre las posibles causas de dicho error
#    3. ¿Qué otras excepciones deberias considerar?

#esta es la funcion que da el enunciado:

"""
muestras_2 = []

def obtener_media(lista):
    sumatoria = 0

    for valor in lista:
        sumatoria += valor
    longitud = len(lista)

    return sumatoria / longitud

obtener_media(muestras_2)
"""
#1:
#como error me da ZeroDivisionError

#2:
muestras_2 = []

def obtener_media(lista):
    sumatoria = 0

    for valor in lista:
        sumatoria += valor
    try:                       #el try se lo pongo recien a esta altura que es donde puede dar error
        longitud = len(lista)
        return sumatoria / longitud
    except ZeroDivisionError:     #pongo except con el error que se que me da y abajo printeo mensaje        
        print("no se puede dividir por 0") 

print(obtener_media(muestras_2))
#3:
#se podria verificar que la lista, sea una lista, ya que si el parametro es de otro tipo(no iterable), el for no funcionaria