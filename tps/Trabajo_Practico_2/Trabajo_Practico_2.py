#!/usr/bin/python3

import threading
import time
import random

bote = []
hinchas = []

def hincha_river():
    hinchas.append('r')
    a_bordo()

def hincha_boca():
    hinchas.append('b')
    a_bordo()

def barra_brava_river(num_hinchas):
    """ Generacion de hinchas de River"""
    viajes = 0
    while viajes < num_hinchas:
        time.sleep(random.randrange(0, 5))
        riv = threading.Thread(target = hincha_river)
        riv.start()
        viajes = viajes + 1

def barra_brava_boca(num_hinchas):
    """ Generacion de hinchas de Boca"""
    viajes = 0
    while viajes < num_hinchas:
        time.sleep(random.randrange(0, 5))
        boc = threading.Thread(target = hincha_boca)
        boc.start()
        viajes = viajes + 1

def a_bordo():
        hincha = random.choice(hinchas)
        hinchas.remove(hincha)

        if hincha == 'b':
                print("vamos Boca")
        else:
                print("vamos River")

        bote.append(hincha)

        if len(bote) == 4:
                a_remar()

def a_remar():
        print("A remar!")
        while True:
            bote.pop()
            if len(bote) == 0:
                break;

#t1 = threading.Thread()
#t2 = threading.Thread()

barra_boca = threading.Thread(target=barra_brava_river, args=(8,))
barra_river = threading.Thread(target=barra_brava_boca, args=(8,))

barra_boca.start()
barra_river.start()

barra_boca.join()
barra_river.join()

print("Terminaron los viajes ")
