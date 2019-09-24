#!/usr/bin/python3

import getopt
import sys
import argparse
import socket
import threading

"""
opciones, argumentos = getopt.getopt(sys.argv[1:], "f:h")

ruta_archivo = "www.distribuidoraperu.com.ar"
puerto = 5000

for i in opciones:
    if i[0] == "-f":
        #La pos. 1 del arreglo constituye la dirección del archivo.
        ruta_archivo = i[1]
    if i[0] == "-p":
        #La pos. 1 del arreglo constituye el puerto.
        puerto = int(i[1])

#Llamada a función LecturaArchivo para abrir y leer archivo.
LecturaArchivo(ruta_archivo, int(puerto))
"""

analizador = argparse.ArgumentParser()

analizador.add_argument("-f", "--file", dest = "filePath", nargs = 1, required = True, help = "Input file path")
analizador.add_argument("-p", "--port", dest = "readPort", nargs = "?", default = 5000, const = 8080, type = int, help = "Port reading")

argumentos = analizador.parse_args()

print(argumentos.filePath, argumentos.readPort)

servidor = socket.socket()
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind(("127.0.0.1", 8080))
servidor.listen(1)
socket_cliente, direccion = servidor.accept()
hilos_cliente = threading.Thread(target = cliente, args = (socket_cliente, direccion))
hilos_cliente.start()
