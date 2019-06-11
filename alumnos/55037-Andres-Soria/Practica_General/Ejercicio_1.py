#!/usr/bin/python

import os

def lectura():
    EOF = False
    lectura_total = ""
    tamanio = 10

    while not EOF:
        lectura_actual = os.read(1, tamanio)
        lectura_total = lectura_total + lectura_actual

        if len(lectura_actual) < tamanio:
            EOF = True

    return lectura_total

print ("Ingresar conjunto de palabras: \n")
palabras = lectura()

def reverse(string):
    string = "".join(reversed(string))
    return string

print ("\n Conjunto de palabras con letras en orden inverso: \n")

lista_lectura = palabras.split()

for string_lectura_invertido in lista_lectura:
    #string_lectura_invertido = ' '.join(lista_lectura)
    os.write(1, string_lectura_invertido[::-1] + " ")
print ("\n")
