#!/usr/bin/python3

import socket
import threading

def parse(tamanio):
    #Formulación de string de la petición a partir del tamaño en bytes.
    string = str(tamanio)
    #División de cadena de caracteres (petición) en lista. Listado de string.
    string = string.split("\\r\\n")
    #Creación de lista solicitud.
    solicitud = {}
    for campo in string[1:-2]:
        #Toma el campo y le aplica el metodo split para adquirir dirección.
        valores = campo.split(":")
        #Devolución de cadena de caracteres en minúscula de la cadena dada.
        solicitud[valores[0].lower()] = valores[1]
    return solicitud

def manejador(cliente, direccion):
    #Se recibe la petición del cliente.
    peticion = cliente.recv(1024000)
    #Llamada a función parse para extraer dirección.
    extraccion = parse(peticion)
    #print (extraccion["host"][1:])
    #Creación de socket para conectarse a servidor remoto (S).
    servidor_remoto = socket.socket()
    #Conección a servidor remoto.
    servidor_remoto.connect((extraccion["host"][1:], 80))
    #servidor_remoto.connect(("www.coto.com.ar", 80))
    #Enviar petición a servidor remoto.
    servidor_remoto.send(peticion)
    #Tomar respuesta de servidor remoto.
    respuesta = servidor_remoto.recv(1024)
    #print(peticion)
    #print("\n")
    #Devolución de respuesta de la petición al cliente.
    cliente.send(respuesta)
    #Cierre de servidor remoto.
    #servidor_remoto.close()
    #Cierre de cliente.
    #cliente.close()

# S - P - C

#Creación de socket para comunicacion entre cliente (C) y proxy (P).
proxy_socket = socket.socket()
proxy_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Especificación de direccion del socket.
proxy_socket.bind(("127.0.0.1", 8080))
#Hacer que el servidor escuche a nuevas conexiones.
proxy_socket.listen()

while True:
    #Aceptación de nueva conexión del cliente (C).
    cliente_socket, cliente_direccion = proxy_socket.accept()
    #Creación de hilo con el nuevo socket para manejar y administrar la solicitud (petición).
    hilo_cliente = threading.Thread(target = manejador, args = (cliente_socket, cliente_direccion))
    #Inicialización de hilo.
    hilo_cliente.start()

'''
#Inicialización del analizador.
parser = argparse.ArgumentParser()

#Añadir argumentos al parse.
parser.add_argument("-f", "--file", dest = "ruta_archivo", nargs = 1, required = True, help = "Ruta de archivo de entrada")
parser.add_argument("-p", "--port", dest = "puerto", nargs = "?", default = 8080, const = 8080, type = int, help = "Numero de puerto")

#Convocar argumentos a una variable.
argumentos = parser.parse_args()

#print(argumentos.ruta_archivo, argumentos.puerto)
'''
