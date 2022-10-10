
vNomb = []
vNomb.insert(0,"Juan")
vNomb.insert(1,"Pepe")
vNomb.insert(2,"Ines")
vNomb.append("Minerva")
vNomb.insert(1,"Julian")

#Eliminar elementos de la lista 
    #vNombres.clear()
vNomb.remove("Pepe")
print(f"El nombre borrado es {vNomb.pop(1)}")
#Con reverse puedo ordenar en orden inverso-
vNomb.sort(reverse=True)
#Contar el numero de elementos de la lista
print(f"Ines aparece", vNomb.count("Ines"), "veces")
print("La lista tiene",  len(vNomb))
print(vNomb)

