#!/usr/bin/python

import multiprocessing
import time

numeros = [10, 60, 26, 159]

def suma():
    global numeros
    resultado = numeros[0] + 40
    time.sleep(1)
    print (resultado)

def resta():
    global numeros
    resultado = numeros[1] - 9
    time.sleep(2)
    print (resultado)

def producto():
    global numeros
    resultado = numeros[2] * 2
    time.sleep(3)
    print (resultado)

def division():
    global numeros
    resultado = numeros[3] / 3
    time.sleep(4)
    print (resultado)

h1 = multiprocessing.Process(target=suma,  args=())
h2 = multiprocessing.Process(target=resta,  args=())
h3 = multiprocessing.Process(target=producto,  args=())
h4 = multiprocessing.Process(target=division,  args=())

mq = multiprocessing.Queue()
h1.start()
h2.start()
h3.start()
h4.start()

h1.join()
h2.join()
h3.join()
h4.join()
