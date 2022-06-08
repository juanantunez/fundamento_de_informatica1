#tutorial HTTP :
#import requests #biblioteca que necesitamos para hacer pedidos
#Aplicacion Rest: Se correlaciona las url con los verbos http->verbo http es get:get filtro la tabla y me trajo ese recurso en particular
#“get” es pedir un recuso() #ingreso URL de dato->que puede ser para que devuelva una prenda en especifico (un diccio)o opara que devuelva todas las prendas(lista de diccio)
#"json()" es el formato en el cual los servidores devuelven la informacion al cliente->json() es el q trae la informacion en si 
#lo 1ro que me deuveulve es el "Status code" habla de como funciono la condición y el estado del pedido:
#si decuelve -> <Response[200]> #siginifica que me funciona
#si decuelve -> <Response[404]> #siginifica que me da error (puede ser xq no exista )
#aux: si devuelve <Response[202] es accepted
#Luego devuelve la informacion en si en formato json()

#headers: me da toda la metadata del pedido, es decir la fecha, tipo de informacion q trae
#print(pedido.status_code) # pide el solo el nro del status_code q devolvia entre <Response[nro]>

#print(len(pedido.json()))#Para saber cantidad de prendas o recursos que tiene

#si URL es:
#'https://macowins-server.herokuapp.com/prendas/1' #en este caso me devuelve un diccio con una prenda en especifico ->porq al final tiene /1 ("/nro" al final da a entender esto)aux:si pongo /nro y me da error 404, significa que ese nro de prenda no existe
#'https://macowins-server.herokuapp.com/prendas' #en este caso me devuelve una lista de diccionarios con todas las prendas

#estructura:

import requests #biblioteca que necesitamos para hacer pedidos
pedido = requests.get('https://macowins-server.herokuapp.com/prendas/1')#“get” es pedir un recuso() #ingreso URL de dato->que en este caso pide una prenda en especifico
print(pedido) #me devuelve el <Response[nro]>
print(pedido.json()) #"json()" es el formato en el cual los servidores devuelven la informacion al cliente ya sea diccio o lista de diccio
print(pedido.headers)#headers: me da toda la metadata del pedido, es decir la fecha, tipo de informacion q trae
print(pedido.status_code) # pide el solo el nro del status_code q devolvia entre <Response[nro]>

import requests #biblioteca que necesitamos para hacer pedidos
pedido = requests.get('https://macowins-server.herokuapp.com/prendas/1')#“get” es pedir un recuso() #ingreso URL de dato->que en este caso pide una prenda en especifico
print(pedido)
print(pedido.json()) #"json()" es el formato en el cual los servidores devuelven la informacion al cliente

"""
#Se correlaciona las url con los verbos http->verbo http es get:get filtro la tabla y me trajo ese recurso en particular

me devuelve:
<Response[200]> #siginifica que me funciona
{“id”:1,”tipo”: “pantalón”, “talle”:35}  #devuelve esto xq en la URL yo le pedi la prenda 1 de ropa


import requests #biblioteca que necesitamos para hacer pedidos
pedido = requests.get('https://macowins-server.herokuapp.com/prendas')#“get” es pedir un recuso() #ingreso URL de dato->en este caso me devuelve una lista de diccionarios con todas las prendas
print(pedido)
print(pedido.json())


me devuelve:
<Response[200]> #siginifica que me funciona
[{“id”:1,”tipo”: “pantalón”, “talle”:35}, {'id': 2, 'tipo': 'pantalon', 'talle': 36},...., {'id': 18, 'tipo': 'saco', 'talle': 'M', 'enStock': False}, ...]#devuelve esto xq en la URL yo le pedi es todas las prendas->me devuelve una lista de diccionarios con todas las prendas
#aux:que diga 'enStock': False ->es normal, significa que no hay en stock de esa prenda

import requests #biblioteca que necesitamos para hacer pedidos
pedido = requests.get('https://macowins-server.herokuapp.com/prendas/20')#“get” es pedir un recuso() #ingreso URL de dato->que en este caso pide una prenda en especifico
print(pedido)
print(pedido.json())


me devuelve:
<Response[200]> #siginifica que me funciona
{'id': 20, 'tipo': 'saco', 'talle': 'XL'}  #devuelve esto xq en la URL yo le pedi la prenda 20 de ropa


import requests #biblioteca que necesitamos para hacer pedidos
pedido = requests.get('https://macowins-server.herokuapp.com/prendas')
print(len(pedido.json()))#Para saber cantidad de prendas o recursos que tiene

#devuelve cantidad de prendas nro de cantidad de prendas que tiene:
20

import requests
pedido =requests.get("https://maxowins-server.herokuapp.com/prendas/400")
print(pedido)

me devuelve:
<Response[404]> #siginifica que me da error


#headers: me da toda la metadata del pedido, es decir la fecha, tipo de informacion q trae


import requests
pedido =requests.get("https://maxowins-server.herokuapp.com/prendas/1")
print(pedido.headers)#headers: me da toda la metadata del pedido, es decir la fecha, tipo de informacion q trae

me devuelve:
diccio con la metadata del pedido(fecha, tipo de info, etc)

import requests 
pedido = requests.get('https://macowins-server.herokuapp.com/prendas/1')
print(pedido.status_code) # pide el solo el nro del status_code q devolvia entre [] al principio

me devuelve:
ese nro de statud_code (ya sea 200 o 404, etc)->en este caso 200
"""











