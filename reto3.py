#Leer 5 números enteros y guardar en una lista, después permitir que el usuario busque un número y si este se encuentra en la lista indicar con un mensaje que el resultado es exitoso

listaNumeros=[]


for i in range(0,5,1):
    numeroIngresado=int(input("Ingrese un numero:"))
    listaNumeros.append(numeroIngresado)

buscarNumero = int(input("Ingrese numero a buscar: "))

if(buscarNumero in listaNumeros):
    print('Si esta en la lista')
else:
    print('no esta en la lista')


