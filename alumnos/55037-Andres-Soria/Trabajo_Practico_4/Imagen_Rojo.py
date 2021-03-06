#!/usr/bin/python3

import os
import array

def color(ruta):
    #Apertura de imagen en formato ".ppm".
    fd = os.open(ruta + ".ppm", os.O_RDONLY)
    #Lectura de cabecera.
    cabecera = os.read(fd,15)

    #Extracción del contenido de la imagen.
    extraccion_imagen = str(cabecera).split("\\n")
    #Análisis de los datos de imagen.
    imagen_datos = {
        "tipo": extraccion_imagen[0][2:],
        "ancho": int(extraccion_imagen[1].split()[0]),
        "alto": int(extraccion_imagen[1].split()[1]),
        "valor_maximo": int(extraccion_imagen[2])
    }

    #Uso de ancho y alto de imagen.
    ancho_img = imagen_datos["ancho"]
    altura_img = imagen_datos["alto"]

    #Lectura de imagen sin cabecera.
    contenido = os.read(fd, ancho_img * altura_img * 3)

    #Declaración de nuevo formato para dicha imagen.
    formato_ppm = "{} {} {} {}\n".format(imagen_datos["tipo"], imagen_datos["ancho"], imagen_datos["alto"], imagen_datos["valor_maximo"])
    #Datos de imagen en formato ".ppm".
    imagen_completa = array.array('B', [0, 0, 0] * imagen_datos["ancho"] * imagen_datos["alto"])

    for x in range(0, imagen_datos["alto"]):
        for y in range(0, imagen_datos["ancho"]):
            index = 3 * (x * imagen_datos["ancho"] + y)
            imagen_completa[index] = contenido[index]

    #Apertura de nueva imagen en formato ".ppm".
    nuevo_archivo =  open(ruta + '_rojo.ppm', 'wb')
    #Asignación y escritura de nuevo formato a la imagen.
    nuevo_archivo.write(bytearray(formato_ppm, 'ascii'))
    #Función tofile es aplicable para el almacenamiento rápido de datos de matriz.
    imagen_completa.tofile(nuevo_archivo)
