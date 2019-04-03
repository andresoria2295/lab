#!/usr/bin/python

import os

print ("Ingresar conjunto de palabras: \n")
lectura = os.read(0, 100)

def reverse(string):
    string = "".join(reversed(string))
    return string

print ("\n Conjunto de palabras: \n")
os.write(1, lectura)

print ("\n Conjunto de letras en orden inverso:")
os.write(1, reverse(lectura))
print ("\n")

print ("\n Conjunto de palabras y letras en orden inverso: \n")

lista_lectura = lectura.split()

for string_lectura_invertido in lista_lectura:
    #string_lectura_invertido = ' '.join(lista_lectura)
    os.write(1, string_lectura_invertido[::-1] + " ")
print ("\n")
