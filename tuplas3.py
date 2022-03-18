#Convertir la tupla=(50,45,20,30,40,87) en una lista que solo contenga números  PARES

numerosTupla=(50,45,20,30,40,87)


listaNumeros=[]

for numeroTupla in numerosTupla:
    if numeroTupla >40:
        listaNumeros.append(numeroTupla)
print(listaNumeros)
