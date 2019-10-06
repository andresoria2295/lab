#!/usr/bin/python

import socket
import threading
import os

def parse(tamanio):
    #Formulacion de string de la peticion a partir del tamano en bytes.
    string = str(tamanio)
    #Division de cadena de caracteres (peticion) en lista. Listado de string.
    #Toma de segundo elemento de la lista posteriormente de "Host: ".
    string = string.split("Host: ")[1]
    #Division de cadena en lista donde cada linea (renglon) es un elemento de la lista.
    string = string.splitlines()[0]
    #Devolucion de string previamente listado.
    return string

def manejador(cliente, direccion):
    #Se recibe la peticion del cliente.
    peticion = cliente.recv(1024000)
    #Llamada a funcion parse para extraer direccion.
    #extraccion = parse(peticion)
    #print (extraccion)
    #Creacion de socket para conectarse a servidor remoto (S).
    servidor_remoto = socket.socket()
    #Division de cadena extraccion en lista y toma del primer elemento de la lista.
    #direccion_url = extraccion.split(":")[0]
    #Division de cadena extraccion en lista y toma del segundo elemento en formato entero de la lista.
    #Excepcion de fuera de rango -> puerto = 80
    #puerto = int (extraccion.split(":")[1])
    #Coneccion a servidor remoto.
    #servidor_remoto.connect((direccion_url, puerto))
    servidor_remoto.connect(("www.coto.com.ar", 80))
    #Envio de peticion a servidor remoto.
    servidor_remoto.send(peticion)

    while True:
        #Tomar respuesta de servidor remoto.
        respuesta = servidor_remoto.recv(20480)
        if not respuesta:
 	    break
        #Devolucion de respuesta de la peticion al cliente.
        cliente.send(respuesta)

    #Cierre de servidor remoto.
    servidor_remoto.close()
    #Cierre de cliente.
    cliente.close()

# S - P - C

#Creacion de socket para comunicacion entre cliente (C) y proxy (P).
proxy_socket = socket.socket()
proxy_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Especificacion de direccion del socket.
proxy_socket.bind(("127.0.0.1", 8080))
#Hacer que el servidor escuche a nuevas conexiones.
proxy_socket.listen(5)

while True:
    #Aceptacion de nueva conexion del cliente (C).
    cliente_socket, cliente_direccion = proxy_socket.accept()
    #Creacion de hilo con el nuevo socket para manejar y administrar la solicitud (peticion).
    hilo_cliente = threading.Thread(target = manejador, args = (cliente_socket, cliente_direccion))
    #Inicializacion de hilo.
    hilo_cliente.start()

'''
#Inicializacion del analizador.
parser = argparse.ArgumentParser()

#Anadir argumentos al parse.
parser.add_argument("-f", "--file", dest = "ruta_archivo", nargs = 1, required = True, help = "Ruta de archivo de entrada")
parser.add_argument("-p", "--port", dest = "puerto", nargs = "?", default = 8080, const = 8080, type = int, help = "Numero de puerto")

#Convocar argumentos a una variable.
argumentos = parser.parse_args()

#print(argumentos.ruta_archivo, argumentos.puerto)
'''
