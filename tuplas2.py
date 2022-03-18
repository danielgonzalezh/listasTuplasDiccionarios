#Convertir la tupla=(50,45,20,30,40,87) en una lista que solo contenga números >40  

tuplaNumeros=(50,45,20,30,40,87)

listaNumeros=[]

for i in range(len(tuplaNumeros)):
    if tuplaNumeros[i] >40:
        listaNumeros.append(tuplaNumeros[i])
print(listaNumeros)
