#!/usr/bin/python3

import argparse
import os
import requests
import urllib.request, urllib.parse, urllib.error
#Python Imaging Library
from PIL import Image
from bs4 import BeautifulSoup

#Función de ayuda al usuario.
def OpcAyuda():
    print("\n Ejecución de Programa:\n")
    mensaje = "Modo de uso: ./Trabajo_Practico_4.py -u [URLs de sitios web]"
    ejemplo = "Ejemplo: ./Trabajo_Practico_4.py -u http://www.example.com,http://www.example1.com\n"
    print (mensaje)
    print (ejemplo)
    #Salir del programa.
    exit(0)

#Procesamiento de opciones con argparse.
Parser_Argumento = argparse.ArgumentParser()
Parser_Argumento.add_argument("-u", "--URL", dest = "direccion_web", nargs = "+", required = True, help = "Modo de uso: ./Trabajo_Practico_4.py -u [URLs de sitios web]")
argumentos = Parser_Argumento.parse_args()

#Listado de sitios web ingresados y añadidos a la aplicación.
URL_web = argumentos.direccion_web
contenido = []
links = []

#Se recorre la lista de direcciones web.
for URL in URL_web:
    #Uso de BeautifulSoup (Biblioteca de Python para analizar documentos html).
    #Conversión del contenido de cada sitio web de formato html a formato texto.
    html = BeautifulSoup(requests.get(URL).text)
    #Búsqueda y localización de imagenes a partir de la etiqueta de filtrado "img".
    imagenes = html.findAll("img")
    #Se recorre la lista de imagenes halladas.
    for imagen in imagenes:
        #Si la dirección de imagen extraída (fuente) es "relativa" (ausencia de dirección de sitio web):
        if imagen.get("src")[0] == "/":
            #Se agrega a lista links la dirección del sitio web en conjunto con la dirección de imagen (fuente).
            links.append(URL + imagen.get("src"))
        #Si la dirección de imagen extraída (fuente) es "absoluta"
        else:
            #Se agrega a lista links la dirección de imagen (fuente).
            links.append(imagen.get("src"))

#En caso de NO encontrar la carpeta que almacena las imagenes descargadas de los sitios:
if not os.path.isdir("./descarga_imagenes"):
    #Creación de carpeta que albergue imagenes descargadas.
    os.mkdir("./descarga_imagenes")

contador = 0

#Se recorre la lista que contiene las direcciones de imagenes (absolutas).
for link in links:
    try:
        #Uso de módulo urllib.request, que permite copiar un objeto de red denotado por una URL en un archivo local.
        #Toma cada dirección de imagen absoluta de la lista, sitúa dicha imagen representada en una carpeta previamente asignada y se le atribuye un valor.
        urllib.request.urlretrieve(link, "./descarga_imagenes/" + str(contador))
        contador = contador + 1
        #Se carga la imagen localizada en la carpeta que le fue asignada y se le atribuye un valor.
        imagen = Image.open("./descarga_imagenes/" + str(contador))
        #Se guarda dicha imagen en la misma carpeta que le fue asignada anteriormente, con el mismo valor, pero en formato ".ppm".
        imagen.save("./descarga_imagenes/" + str(contador) + ".ppm")
    #Manejo de errores.
    #Uso de módulo urllib.error para excepciones generadas por el módulo urllib.request.
    #HTTPError es útil cuando se manejan errores de HTTP exóticos, como solicitudes de autenticación.
    except urllib.error.HTTPError as error:
         #error.reason fundamenta la razón del error. Puede ser una cadena de mensaje u otra instancia de excepción.
         print("No es posible descargar imagen: " + error.reason)
    #OSError es aplicado cuando una función devuelve un error relacionado con el sistema.
    except OSError as error:
        print("OSError: " + str(error))
