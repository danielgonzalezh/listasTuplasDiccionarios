estudiante={
    'nombre':'Falcao',
    'edad':34,
    'esFutbolista':True
}
#imprimir/acceder a todas las llaves
#atributos de mi diccionario
print(estudiante)
#necesito acceder a un atributo o llave del diccionario
print(estudiante['nombre'])
print(estudiante.get('nombre'))
print(estudiante.get('edad'))

#recorrer un diccionario y obtener sus valores

for valor in estudiante.values():
    print(valor)