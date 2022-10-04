#Programa El hombre araña también conocido como Spider-man.

print("Dime 1era distancia y 2nd distancia respectivamente")
dis1 = int(input())
dis2 = int(input())
if abs(dis1)>abs(dis2):
    print("Tendrás que ir al segundo camino")
    print("La distancia recorrida sería", ((abs(dis2))*2)+abs(dis1))
else:
    print("Tendrás que ir al primer camino")
    print("La distancia recorrida sería", ((abs(dis1))*2)+abs(dis2))


