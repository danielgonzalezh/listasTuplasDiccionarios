#Leer 8 ciudades colombianas, guardarlas en una lista y mostrar en orden inverso los datos ingresados

ciudades=[]
for i in range(0,8,1):

    ciudad=input('Ingrese ciudad de Colombia: ')
    ciudades.append(ciudad)
print(ciudades)
ciudades.reverse()
print(ciudades)
#Este [::-1]tambien me invierte la lista
#print(ciudades[::-1])
