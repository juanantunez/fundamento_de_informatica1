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
"""
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

import requests #biblioteca que necesitamos para hacer pedidos
pedido = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=pantalon')#“get” es pedir un recuso() #ingreso URL de dato->en este caso me devuelve una lista de diccionarios con todas las prendas que el que dentro dentro del diccio en la clave 'tipo' es 'pantalon'->esto se da porq agrego luego de prendas "?tipo=pantalon"
print(pedido.json())

import requests
r = requests.get('https://macowins-server.herokuapp.com/nueva-funcionalidad-que-a-veces-no-anda-bien')
print(r.content) #content: me da el contenido del pedido 

import requests
r = requests.get('https://macowins-server.herokuapp.com/prendas?talle=40&tipo=pantalon')
print(r.json())

import requests
r = requests.get('https://macowins-server.herokuapp.com/ventas/?_page=3')#solo la pagina 3
print(r.json())

#lo que pongo ahora es un URI:
import requests
r = requests.get('protocolo://dominio:puerto/ruta#fragmento?parametro1=valor1&parametro2=valor2')
print(r.json())

#lo que pongo ahora es un URI:
import requests
r = requests.get('cerebro://recuerdos:3403/recientes#hoy?tema=http')
print(r.json())

import requests
requests.get('http://localhost:300')
raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='localhost', port=300): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7fb528ea62e8>: Failed to establish a new connection: [Errno 111] Connection refused',))

import requests
requests.get('http://unSitioQueProbablementeNoExistaEnInternet')
raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='unsitioqueprobablementenoexistaeninternet', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7fb528e84a90>: Failed to establish a new connection: [Errno -2] Name or service not known',))

import requests
requests.get('http://google.com:8902',timeout=5)
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='google.com', port=8902): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7fb5297f3cc0>: Failed to establish a new connection: [Errno 101] Network is unreachable',))

import requests
data = {'id': 21}
r = requests.post('https://macowins-server.herokuapp.com/prendas/', data=data) #crea una prenda con el id 21 y la agrega al pedido

import requests #biblioteca que necesitamos para hacer pedidos
pedido = requests.get('https://macowins-server.herokuapp.com/prendas')#“get” es pedir un recuso() #ingreso URL de dato->en este caso me devuelve una lista de diccionarios con todas las prendas
print(pedido)
print(pedido.json())

import requests
data =  { "tipo": "chomba", "talle": "XS" }
r = requests.post('https://macowins-server.herokuapp.com/prendas', data=data) #agrega al pedido con diccios con id que no nos sirve
print(r.json())

import json, requests
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data =  { "tipo": "chomba", "talle": "XS" }
r = requests.post('https://macowins-server.herokuapp.com/prendas', data=json.dumps(data), headers=headers)
r.status_code
201
requests.get('https://macowins-server.herokuapp.com/prendas').json()
"""