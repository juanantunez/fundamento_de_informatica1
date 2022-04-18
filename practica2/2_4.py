#ej 4: Una compañía de transporte internacional tiene servicio en algunos países de América del Sur, América Central, América del Norte, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido, tal como se muestra en la tabla:
#Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad. Realizá un programa para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.
peso=int(input("ingrese peso: "))
ubi=input("ingrese ubicacion: ")
if peso <=5000:
  if ubi=="Asur":
    print(f"A sur {peso*10}")
  if ubi=="Acen":
    print(f"A cen {peso*15}")
  if ubi=="Anor":  
    print(f"A nor {peso*18}")
  if ubi=="eur":  
    print(f"eur {peso*24}")
  if ubi =="asi":  
    print(f"asi {peso*30}")
  else:
    print("codigo invalidor")  
else:
  print("no es posible")  