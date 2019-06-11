#!/usr/bin/python
# coding=utf-8

import os

def lecturaArchivo(ruta):
    EOF = False
    lectura_total = ""
    tamanio = 1024

    # 1. Abrir archivo para lectura
    fd = os.open(ruta, os.O_RDONLY)

    while not EOF:
        # Leer x bytes del archivo
        lectura_actual = os.read(fd, tamanio)
        # Adicionar a lo ya leido
        lectura_total = lectura_total + lectura_actual
        if len(lectura_actual) < tamanio:
            EOF = True

    os.close(fd)
    return lectura_total

def csvArreglo(ruta):
    arreglo_total = []
    contenido = lecturaArchivo(ruta)
    # 1. Hacer que cada renglón sea un elemento de un arreglo.
        # ["juan perez,1200", "lucas ortiz,2000"]
    # 2. Hacer que cada elemento del arreglo resultante sea también un arreglo.
        # [["juan parez", "1200"], ["lucas ortiz", "2000"]]

    # Paso 1. Con el espaciado "\n" se forman los renglones.
    arreglo_texto = contenido.split("\n")

    # Paso 2.Quitar y suprimir el primer y último renglón del archivo csv dado que no cuenta con info. importante.
    longitud = len(arreglo_texto) - 2

    # Iterar desde el renglón 1 hasta el último (longitud); con la "," separar los elementos del primer arreglo.
    for i in range(1, longitud):
        formato_arreglo = arreglo_texto[i].split(",")
        arreglo_total.append(formato_arreglo)

    return arreglo_total

def extraerMail(arreglo, monto):
    # Recorrer el arreglo observando cada uno de los saldos que se encuentran en la pos. 4 de cada arreglo.
    # Si los saldos son mayores al monto, extraer el mail y colocarlo en otro arreglo.
    # Devolver y retornar el arreglo con los mails.
    for persona in arreglo:
        if int(persona[4]) > monto:
            print(persona[1])

arreglo_personas = csvArreglo("./archivo.csv")
extraerMail(arreglo_personas, 1200)
