numeros=[]

tamano=int(input('ingrese el tamaño :'))

for i in range(tamano):
    numero=int(input("ingrese un numero:"))
    numeros.append(numero)

buscar=int(input("ingresa el numero que buscas"))

if(buscar in numeros):
    print(f'el numero {buscar}si esta')

else:
    print(f'el numero {buscar} no esta')

