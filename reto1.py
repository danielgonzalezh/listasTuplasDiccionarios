#Construir un programa que reciba el tamaño de una lista  y la llene con múltiplos de 7

#El resultado de multiplos comienza en 0 [0,7,14,21,.....]segun la longitd de la lista

multiplos=[]

longitudLista=int(input("Ingrese el tamaño de la lista:"))

for i in range(longitudLista):
    
    multiplos.append(i*7)

print(multiplos)

#El resultado de multiplos comienza en 7 [7,14,21,.....]segun la longitd de la lista
multiplos=[]

longitudLista=int(input("Ingrese el tamaño de la lista:"))

for i in range(longitudLista):
    
    multiplos.append((i+1)*7)

print(multiplos)

#El resultado de multiplos comienza en 1 ya que se inicio con un dato en la primer casilla multiplos=[1][1,7,14,21,.....] una casilla mas la longitd de lalista

multiplos=[1]

longitudLista=int(input("Ingrese el tamaño de la lista:"))

for i in range(longitudLista):
    
    multiplos.append((i+1)*7)

print(multiplos)

#Ingrese el tamaño de la lista:7
#[0, 7, 14, 21, 28, 35, 42]
#Ingrese el tamaño de la lista:7
#[7, 14, 21, 28, 35, 42, 49]
#Ingrese el tamaño de la lista:7
#[1, 7, 14, 21, 28, 35, 42, 49]