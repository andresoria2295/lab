#!/usr/bin/python

import os

# open / write / read / close
# os.open(path, flags) => devuelve un file descriptor.
    # path: ruta al archivo.
    # flags: os.O_RDONLY | os.O_RDWR | os.O_WRONLY | os.O_CREAT

# os.close(fd) => cierra el archivo con el fd indicado.
# os.read(fd, size) => contenido.
# os.write(fd, contenido) => cantidad de bytes leidos (int)

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

def escrituraArchivo(ruta, contenido):
    fd = os.open(ruta, os.O_WRONLY)
    bytes_escritos = os.write(fd, contenido)
    print("Se han escrito " + str(bytes_escritos) + " bytes al archivo " + ruta)
    os.close(fd)
    return

print("Ingresar archivo de entrada: \n")
archivo_entrada = raw_input()
print("\n")
print("Ingresar archivo de salida: \n")
archivo_salida = raw_input()
print("\n")

contenido = lecturaArchivo(archivo_entrada)
escrituraArchivo(archivo_salida, contenido)
