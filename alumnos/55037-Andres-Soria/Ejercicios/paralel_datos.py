#!/usr/bin/python

import threading
import time

europa = ["Portugal", "Francia", "Alemania", "Suiza"]

def norte():
    global europa
    europa_norte = [paises.upper() for paises in europa[0]]
    time.sleep(1)
    print (europa_norte)

def sur():
    global europa
    europa_sur = [paises.upper() for paises in europa[1]]
    time.sleep(2)
    print (europa_sur)

def este():
    global europa
    europa_este = [paises.upper() for paises in europa[2]]
    time.sleep(3)
    print (europa_este)

def oeste():
    global europa
    europa_oeste = [paises.upper() for paises in europa[3]]
    time.sleep(4)
    print (europa_oeste)

t1 = threading.Thread(target=norte, args=())
t2 = threading.Thread(target=sur, args=())
t3 = threading.Thread(target=este, args=())
t4 = threading.Thread(target=oeste, args=())

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
