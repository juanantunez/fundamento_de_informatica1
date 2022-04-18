#ej 7
#Un comerciante, el cual tiene un sueldo base, recibe un 10% extra por comisión por cada venta que realiza. Realizar un programa que devuelva el dinero que recibirá por comisión luego de 4 ventas y el total de dinero que ganará ese mes, teniendo en cuenta estas ventas y su sueldo base.
CANTIDAD_VENTAS = 4
COMISION        = 0.10
totalComision   = 0.0

sueldoBase = float(input('Ingrese sueldo base $')) #ingreso sueldo base
for venta in range(CANTIDAD_VENTAS): #para cada una d las 4 ventas
    print('Ingrese monto de la venta No. {0} '.format(venta+1),end='$') #voy ingresando x teclado monto correspondiente a c venta, va recorriendo c venta
    venta = float(input()) #ingreso d cuanto fue la venta x teclado
    totalComision += (COMISION)*venta #com tot va a sumar cada comision (hace el 10% d c venta) y recorre
    print("Las ganancias de comision son ${0:.2f}".format(totalComision))#hasta 2 nros despues de la ,
    print("y el total es ${}".format(totalComision+sueldoBase ))