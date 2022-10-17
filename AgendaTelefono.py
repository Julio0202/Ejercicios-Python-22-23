
#Creamos el menu de la agenda
'''
1- Insertar Conctacto
2- Borrar contacto
3- Buscar contacto
4- Ver todos los contactos 
5- Salir
'''
comodin = 0
print("1-Insertar Contacto\n 2-Borrar contacto\n 3-Buscar contacto\n 4-Ver todos los contactos\n 5-Salir")
while (comodin!=5):
    vnomb = []
    vtelef = []
    print("Inserta el número")
    num = int(input())
    if num==1:
        print("Dime su contacto")
        contact = str(input())
        vnomb.append(contact)
        print("Dime su numero")
        telef = int(input())
        vtelef.append(telef)
