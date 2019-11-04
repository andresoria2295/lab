#!/usr/bin/python3

import sys
import getopt

#Función de ayuda al usuario.
def OpcAyuda():
    print("\n Ejecución de Programa:\n")
    mensaje = "Modo de uso: ./Trabajo_Practico_4.py -u [URLs de sitios web]"
    ejemplo = "Ejemplo: ./Trabajo_Practico_4.py -u http://www.example.com,http://www.example1.com\n"
    print (mensaje)
    print (ejemplo)
    #Salir del programa.
    exit(0)

#Uso de función getopt para ingreso de URLs de sitios web.
opciones, argumentos = getopt.getopt(sys.argv[1:], "u:h")

#Bucle para recorrer el arreglo y localizar las direcciones web.
URLs_html = ""

for i in opciones:
    if i[0] == "-h":
        #Llamada a función de ayuda para guiar al usuario.
        OpcAyuda()
    if i[0] == "-u":
        #La pos. 1 del arreglo constituye las diferentes URLs web.
        URLs_html = i[1]

direcciones_web = URLs_html

#Listado de direcciones web.
URL_web = direcciones_web.split(",")

print("Listado de URLs añadidas a la aplicación: ", URL_web)
