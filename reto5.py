numeros=[]

for i in range(0,5,1):
    numero=int(input("ingrese un numero:"))
    numeros.append(numero)

numeroBuscado= int(input("digite el numero a buscar:"))
loTengo =False
for numero in range(0,5,1):
    if(numeroBuscado==numeros):
        loTengo=True
        break
    else:
        loTengo=False

if(loTengo !=False):
    print("se lo tengo papa")
else:
    print("No lo tengo")

