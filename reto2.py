#Construir un programa que reciba el tamaño de una lista y la llene con números entregados por el usuario

numeros=[]

tamanoLista=int(input("Ingrese el tamaño de la lista:"))

for i in range(tamanoLista):
    
    numero=int(input("Ingrese un numero:"))
    numeros.append(numero)
print(numeros)
#[::-1]me invierte la lista o con numeros.reverse()
print(numeros[::-1])

