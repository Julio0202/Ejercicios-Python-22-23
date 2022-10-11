'''
Opción 1:
Lista para nombres
Lista para telefonos

Opción 2:
Lista para nombres y telefonos 
Ejemplo [Juan - Telefono, Pepe - Telefono]

'''
#Opción 1
vNomb = []
vTelf = []
vNomb.append(input("Dime un nombre: "))
vTelf.append(input("Dime un telefono: "))
print("El telefono de", vNomb.pop(),"es",vTelf.pop())