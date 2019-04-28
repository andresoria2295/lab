#!/usr/bin/python
# coding=utf-8

import sys
import getopt
import os
import multiprocessing

def lecturaArchivo(ruta, tamanio):
    EOF = False
    lectura_total = ""
    q = multiprocessing.Queue()

    # 1. Abrir archivo para lectura
    fd = os.open(ruta, os.O_RDONLY)

    while not EOF:
        # Leer x bytes del archivo
        lectura_actual = os.read(fd, tamanio)
        q.put(lectura_actual)
        # Adicionar a lo ya leido
        lectura_total = lectura_total + lectura_actual
        if len(lectura_actual) < tamanio:
            EOF = True

    os.close(fd)
    return q


opciones, argumentos = getopt.getopt(sys.argv[1:], "f:n:")
print opciones

for i in opciones:
    if i[0] == "-f":
        ruta_archivo = i[1]
        print "Esto es una ruta de archivo. "
    if i[0] == "-n":
        valor_bytes = i[1]
        print "Esto es un valor en bytes. "

print ruta_archivo
print valor_bytes

cola = lecturaArchivo(ruta_archivo, int(valor_bytes))

print cola.get()

print ("Proceso padre: " + str(os.getpid()))

def aperturaProceso():
    print("Proceso hijo: " + str(os.getpid()))

proceso_1 = multiprocessing.Process(target = aperturaProceso)
proceso_1.start()
proceso_2 = multiprocessing.Process(target = aperturaProceso)
proceso_2.start()

'''
palabras = cola.get()
cont_palabras = palabras.split()
print len(cont_palabras)
'''
