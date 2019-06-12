#!/usr/bin/python3

import threading
import time
import random

condition = threading.Condition()

bote = []
hinchas = []

def hincha_river():
    river_plate = 'riverplatense'
    hinchas.append(river_plate)
    condition.acquire()
    #restriccion_hincha()
    a_bordo()

    if len(bote) == 4:
        print("Cupo completo")
        condition.wait()

def hincha_boca():
    boca_jrs = 'bostero'
    hinchas.append(boca_jrs)
    condition.acquire()
    #restriccion_hincha()
    a_bordo()

    if len(bote) == 4:
        print("Cupo completo")
        condition.wait()

def barra_brava_river(num_hinchas_river):
    viajes = 0
    while viajes < num_hinchas_river:
        time.sleep(random.randrange(0, 5))
        riv = threading.Thread(target=hincha_river)
        riv.start()
        viajes += 1

def barra_brava_boca(num_hinchas_boca):
    viajes = 0
    while viajes < num_hinchas_boca:
        time.sleep(random.randrange(0, 5))
        boc = threading.Thread(target=hincha_boca)
        boc.start()
        viajes += 1

def a_bordo():
    hincha_abordo = hinchas.pop()

    if hincha_abordo == 'bostero':
        print ("Abordando al bote hincha bostero.")
    else:
        print ("Abordando al bote hincha riverplatense.")
    #time.sleep(2)

    bote.append(hincha_abordo)

    if len(bote) == 4:
        restriccion_hincha()
        print ("\n")
        print ("Listado final de hinchas presentes en el bote: ")
        print (bote)
        print ("\n Bote completo sin riesgo")
        a_remar()

    condition.release()

def a_remar():
    print ("\n Zarpamos al Santiago Berabeu!!\n")

    while True:
        for hincha_pasajero in range(4):
            print("El hincha", bote.pop(), "ha descendido del bote.")
            #time.sleep(2)
        if len(bote) == 0:
            print("\n Bote vacío\n")
            break

def restriccion_hincha():
    print('\n')
    print ("Listado preliminar de hinchas presentes en el bote: ")
    print (bote)
    while bote.count("bostero") == 3 or bote.count("riverplatense") == 3:
        hinchas.append(bote.pop(0))
        bote.append(hinchas.pop(0))

"""def restriccion_hincha():
    while bote.count("bostero") != 3 and bote.count("riverplatense") != 3:
        a_bordo()
"""

River_Plate = threading.Thread(target=barra_brava_river, args=(12,))
Boca_Juniors = threading.Thread(target=barra_brava_boca, args=(12,))

River_Plate.start()
Boca_Juniors.start()

River_Plate.join()
Boca_Juniors.join()
