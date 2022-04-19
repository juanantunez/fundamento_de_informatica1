#ej 8
#Escribir un programa para calcular la nota final de un estudiante, teniendo en cuenta que por cada respuesta correcta el estudiante suma 4 puntos, por cada incorrecta se le resta 1 punto y si la respuesta está en blanco no se le suma ni se le resta.
totalPreguntas = int(input('Ingrese el total de preguntas: '))
totalCorrectas = int(input('Ingrese cantidad respuestas correctas: '))
totalIncorrectas = int(input('Ingrese cantidad respuestas incorrectas: '))
notaFinal = 4*totalCorrectas - totalIncorrectas
print(f"La calificacion final es: {notaFinal}")