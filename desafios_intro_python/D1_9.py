#desafio 9

pedido = { "Ana" :"vegan", "Paul": "veganas", "Luz": "vegetarianas"}
def f():   #no hace falta poner argumento xq va a trabajar directo modificando el diccio origi
  dict2={} #diccionario vacio
  for clave in pedido.values():  #para cada clave 
    dict2[clave]=0
    dict2[clave]+=1 
  print(dict2)   