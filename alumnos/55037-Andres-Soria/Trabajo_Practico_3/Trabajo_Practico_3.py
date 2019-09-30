#!/usr/bin/python3

import socket, threading

def manejador(cliente, direccion):
    peticion = cliente.recv(1024000)
    #Creación de socket para conectarse a servidor remoto (S).
    servidor_remoto = socket.socket()
    # Conección a servidor remoto.
    servidor_remoto.connect(("www.coto.com.ar", 80))
    #Enviar petición a servidor remoto.
    servidor_remoto.send(peticion)
    #Tomar respuesta de servidor remoto.
    respuesta = servidor_remoto.recv(1024)
    print(peticion)
    print("\n")
    cliente.send(respuesta)
    #servidor_remoto.close()
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
