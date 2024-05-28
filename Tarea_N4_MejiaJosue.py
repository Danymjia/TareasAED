#Codigo adaptado utilizando una estructura de decisión múltiple (if-elif-else)

print(" ****** BIENVENIDO A BURGER KING ********\n")
print("Ingrese los datos para la factura electrónica\n")
nombreCliente = input("Ingrese su nombre: ")
numeroCedula = int(input("Ingrese su número de cédula: "))
correo = input("Ingrese su correo: ")
numHamburguesas = int(input("Ingrese el número de hamburguesas a adquirir: "))

print("-----------------------------------------------------------")
print("Ingrese uno de los siguientes tipos de hamburguesas: ")
print("1) sencilla")
print("2) doble")
print("3) triple")
tipoHamburguesa = int(input("Ingrese la opción: "))

if tipoHamburguesa == 1:
    precio = numHamburguesas * 1.50
elif tipoHamburguesa == 2:
    precio = numHamburguesas * 2.50
elif tipoHamburguesa == 3:
    precio = numHamburguesas * 3.25
else:
    print("-----------------------------------------------------------")
    print("Este tipo de hamburguesa no existe")
    print("Muchas gracias")

print("-----------------------------------------------------------")
print("Ingrese su forma de pago")
print("1) Tarjeta de crédito")
print("2) Efectivo")
tipoPago = int(input("Ingrese la opción: "))

if tipoPago == 1:
    recargo = precio * 0.05
    pf = precio + recargo
    print("-----------------------------------------------------------")
    print(f"Genial, {nombreCliente}, el precio final es ${pf: .2f}")
    print(f"La factura se enviará a su correo {correo}")
elif tipoPago == 2:
    recargo = precio * 0.05
    pf = precio + recargo
    print("-----------------------------------------------------------")
    print(f"Genial, {nombreCliente}, el precio final es ${pf: .2f}")
    print(f"La factura se enviará a su correo {correo}")
else:
    print("-----------------------------------------------------------")
    print("No existe ese tipo de pago")
    print("Muchas gracias")
