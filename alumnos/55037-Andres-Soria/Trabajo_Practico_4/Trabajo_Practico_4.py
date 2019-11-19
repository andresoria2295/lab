#!/usr/bin/python3

import argparse
import os
import requests
import urllib.request, urllib.parse, urllib.error
#Python Imaging Library
from PIL import Image
from bs4 import BeautifulSoup
import Color_Imagenes

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
#contenido = []
links = []

#Se recorre la lista de direcciones web.
for URL in URL_web:
    #Uso de BeautifulSoup (Biblioteca de Python para analizar documentos html).
    #Conversión del contenido de cada sitio web de formato html a formato texto.
    html = BeautifulSoup(requests.get(URL).text, "html.parser")
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
    #Se cuenta internamente cada dirección de imagen.
    cantidad = len(link)
    #Si la imagen corresponde a formato ".png":
    if (link[cantidad-3::] == "png"):
        try:
            #Uso de módulo urllib.request, que permite copiar un objeto de red denotado por una URL en un archivo local.
            #Toma cada dirección absoluta de imagen de la lista, sitúa dicha imagen representada en una carpeta previamente asignada y se le atribuye un valor y formato.
            urllib.request.urlretrieve(link, "./descarga_imagenes/" + str(contador) + ".png")
            #Designación de ruta/dirección de la imagen.
            ruta = 'descarga_imagenes/' + str(contador)
            #Cargado de imagen, conversión a RGB y posteriormente guardado en ruta previamente declarada en formato ".ppm".
            imagen = Image.open(ruta + ".png").convert('RGB').save(ruta + ".ppm")
            #Eliminación de imagen de previo formato descargado. (".png")
            os.remove(ruta + ".png")
            contador = contador + 1
            Color_Imagenes.color(ruta)
        #Manejo de errores.
        #Uso de módulo urllib.error para excepciones generadas por el módulo urllib.request.
        #HTTPError es útil cuando se manejan errores de HTTP exóticos, como solicitudes de autenticación.
        except urllib.error.HTTPError as error:
            #error.code manifiesta el código y tipo de error.
            print('Estado: ', error.code)
             #error.reason fundamenta la razón del error. Puede ser una cadena de mensaje u otra instancia de excepción.
            print('Causa/Motivo: ', error.reason)
        #OSError es aplicado cuando una función devuelve un error relacionado con el sistema.
        except OSError as error:
            print("OSError: " + str(error))

    #Si la imagen corresponde a formato ".jpg":
    if (link[cantidad-3::] == "jpg"):
        try:
            #Uso de módulo urllib.request, que permite copiar un objeto de red denotado por una URL en un archivo local.
            #Toma cada dirección absoluta de imagen de la lista, sitúa dicha imagen representada en una carpeta previamente asignada y se le atribuye un valor y formato.
            urllib.request.urlretrieve(link, "./descarga_imagenes/" + str(contador) + ".jpg")
            #Designación de ruta/dirección de la imagen.
            ruta = 'descarga_imagenes/'+str(contador)
            #Cargado de imagen, conversión a RGB y posteriormente guardado en ruta previamente declarada en formato ".ppm".
            imagen = Image.open(ruta + ".jpg").convert('RGB').save(ruta + ".ppm")
            #Eliminación de imagen de previo formato descargado. (".jpg")
            os.remove(ruta + ".jpg")
            contador = contador + 1
            Color_Imagenes.color(ruta)
        #Manejo de errores.
        #Uso de módulo urllib.error para excepciones generadas por el módulo urllib.request.
        #HTTPError es útil cuando se manejan errores de HTTP exóticos, como solicitudes de autenticación.
        except urllib.error.HTTPError as error:
            #error.code manifiesta el código y tipo de error.
            print('Estado: ', error.code)
             #error.reason fundamenta la razón del error. Puede ser una cadena de mensaje u otra instancia de excepción.
            print('Causa/Motivo: ', error.reason)
        #OSError es aplicado cuando una función devuelve un error relacionado con el sistema.
        except OSError as error:
            print("OSError: " + str(error))
