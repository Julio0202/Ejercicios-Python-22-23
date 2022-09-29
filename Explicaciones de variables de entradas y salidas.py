from asyncore import read
from errno import EADDRNOTAVAIL
from sre_constants import JUMP
import string

#Tipos de datos y variables
 #Numericos
  #enteros - - int
  #real - - float
 #Cadenas de caracteres - - str
 #Lógico - - bool
mayor_menorEdad=False
edad = 0
nombre = ""

#Entrada y salida de datos 
#Salida con print
#Entrada de datos - - input
nombre = input("Dime tu nombre:\n")
edad = input("Dime tu edad:\n")
print ("Buenos días", nombre, "tu edad es", edad)