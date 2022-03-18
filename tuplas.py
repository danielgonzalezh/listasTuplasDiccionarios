#creando tuplas en python

estudiantes=('Mario','juan carlos')
print(estudiantes)

#estudiantes.append('martha')ERROR NO SE PUEDE
#print(estudiantes)

#recorriendo tuplas

for estudiante in estudiantes:
    print(estudiante)

#Convertir tupla en lista

listaEstudiantes=list(estudiantes)
print(listaEstudiantes)
listaEstudiantes.append('Daniel')
tuplaEstudiantes=tuple(listaEstudiantes)
print(tuplaEstudiantes)