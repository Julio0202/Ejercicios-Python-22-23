
#Creamos el menu de la agenda
'''
1- Insertar Conctacto
2- Borrar contacto
3- Buscar contacto
4- Ver todos los contactos 
5- Salir
'''
#Funcion que pinta el menuy y devuelve la opción seleccionada del 1 al 5
def pintaMenu():
    comodin = 0
    while (comodin<1 or comodin>5):
        print("1-Insertar Contacto\n 2-Borrar contacto\n 3-Buscar contacto\n 4-Ver todos los contactos\n 5-Salir")
        vnomb = []
        vtelef = []
        try:
            print("Inserta el número de lo que quieres hacer")
            comodin = int(input())
        except:
            print("Las opciones son del 1 al 5") 
    return comodin
comodin = pintaMenu()
while (comodin!=5):
    print("Has seleccionado",pintaMenu())
    comodin = pintaMenu()

# Muy floja la agenda no vas para operador telefónico mejor a barrendero de calles

#FUnciones definidas por el usuario
