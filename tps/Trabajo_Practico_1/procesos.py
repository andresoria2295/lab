#!/usr/bin/python
# coding=utf-8

import sys
import getopt
import os
import multiprocessing

#Función para abrir y leer archivo ingresado por terminal.
def LecturaArchivo(ruta, tamanio, cola_inicial):
    EOF = False

    #Abrir archivo para lectura.
    fd = os.open(ruta, os.O_RDONLY)

    #Bucle para particionar y leer archivo por bloques.
    while not EOF:
        #Leer "x" bytes del archivo.
        lectura_actual = os.read(fd, tamanio)
        #Colocar los datos de la lectura del archivo en la cola.
        cola_inicial.put(lectura_actual)
        """Cuando el número de elementos sea menor que los "x" bytes exigidos por el usuario,
        implica que el archivo fue leído en su totalidad y sale del bucle."""
        if len(lectura_actual) < tamanio:
            EOF = True
    #Cerrar archivo.
    os.close(fd)

#Función para contar los elementos de un arreglo cuyo contenido es el archivo leído.
def ContadorPalabras(lectura):
    for caracter in "\n":
        #Recorrer el contenido del archivo y reemplazar
        lectura = lectura.replace(caracter, " ")
    #Devolucón del número de elementos del arreglo que contiene los datos del archivo.
    return len(lectura.split())

#Función para colocar las palabras en la cola resultante.
def PalabrasCola(cola_inicial, cola_final):
    #Mientras que la cola que contiene los datos leídos no se encuentre vacía:
    while cola_inicial.qsize() != 0:
        #Extraer los datos de la cola y guardarlos dentro de una variable.
        lectura = cola_inicial.get()
        #Invocar la función ContadorPalabras.
        palabras = ContadorPalabras(lectura)
        #Colocar el número de elementos del arreglo que contiene los datos en una nueva cola.
        cola_final.put(palabras)
    return

#Función para apertura y ejecución de procesos hijos.
def AperturaProcesos():
    #Declarar lista.
    procesos = []
    #Colocar en lista el número de procesos.
    for contador in range(numero_procesos):
        #Apertura de procesos hijos.
        ap_proceso = multiprocessing.Process(target = PalabrasCola, args=(cola_entrada, cola_salida))
        #Adjuntar a lista la apertura de procesos hijos.
        procesos.append(ap_proceso)
        #Puesta en marcha y ejecución de procesos hijos.
        ap_proceso.start()
    #Lista con procesos hijos.
    return procesos

#Función para vincular y enlazar procesos en ejecución.
def UnionProcesos(listado_procesos):
    #Recorrer lista que contiene procesos.
    for p in listado_procesos:
        #Bloqueo de proceso.
        p.join()

#Función de ayuda al usuario.
def OpcAyuda():
    print "\n Ejecución de Programa:\n"
    mensaje = "Modo de uso: ./procesos.py -f [archivo o ruta de archivo]"
    mensaje += " -n [tamaño en bytes para lectura de archivo en bloques]"
    mensaje += " -p [número de procesos para ejecución de archivo]\n"
    print mensaje
    print "Ejemplo: ./procesos.py -f prueba.txt -n 1024 -p 2\n"
    #Salir del programa.
    exit(0)

#Creación de colas por multiprocesamiento.
cola_entrada = multiprocessing.Queue()
cola_salida = multiprocessing.Queue()

"""Uso de getopt para indicar el archivo o ruta de archivo por consola y
el número de bytes para la lectura en bloques del mismo."""
opciones, argumentos = getopt.getopt(sys.argv[1:], "f:n:p:h")

"""Bucle para recorrer el arreglo y localizar el archivo o
ruta de archivo, y el número de bytes ingresados."""
ruta_archivo = ""
valor_bytes = 0
numero_procesos = 2

for i in opciones:
    if i[0] == "-h":
        #Llamada a función de ayuda para guiar al usuario.
        OpcAyuda()
    if i[0] == "-f":
        #La pos. 1 del arreglo constituye la dirección del archivo.
        ruta_archivo = i[1]
    if i[0] == "-n":
        #La pos. 1 del arreglo constituye los "x" bytes para la lectura en bloques del archivo.
        valor_bytes = int(i[1])
    if i[0] == "-p":
        numero_procesos = int(i[1])

#Llamada a función AperturaProcesos para la puesta en marcha y ejeción de procesos.
listado_procesos = AperturaProcesos()

#Llamada a función LecturaArchivo para abrir y leer archivo.
LecturaArchivo(ruta_archivo, int(valor_bytes), cola_entrada)

#Llamada a función UnionProcesos para enlazar procesos.
UnionProcesos(listado_procesos)

#Contador de palabras.
nro_palabras = 0

#Mientras que la cola salida no se encuentre vacía:
while cola_salida.qsize() != 0:
    #Sumatoria del número de palabras que contiene la cola salida.
    nro_palabras = nro_palabras + int(cola_salida.get())
    print "Palabras totales del archivo ingresado:", nro_palabras, "palabras."
