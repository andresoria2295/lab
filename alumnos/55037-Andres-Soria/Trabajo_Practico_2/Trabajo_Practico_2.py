#!/usr/bin/python3

import threading
import time
import random

condition = threading.Condition()

bote = []
hinchas = []

def hincha_river():
    condition.acquire()
    river_plate = 'riverplatense'
    hinchas.append(river_plate)
    a_bordo()

    if len(bote) == 4:
        print("Cupo completo")
        condition.wait()

def hincha_boca():
    condition.acquire()
    boca_jrs = 'bostero'
    hinchas.append(boca_jrs)
    a_bordo()

    if len(bote) == 4:
        print("Cupo completo")
        condition.wait()

def barra_brava_river(num_hinchas_river):
    viajes = 0

    while viajes < num_hinchas_river:
        riv = threading.Thread(target=hincha_river)
        riv.start()
        viajes += 1

def barra_brava_boca(num_hinchas_boca):
    viajes = 0

    while viajes < num_hinchas_boca:
        boc = threading.Thread(target=hincha_boca)
        boc.start()
        viajes += 1

def a_bordo():
    hincha_abordo = hinchas.pop()

    if hincha_abordo == 'bostero':
        print ("Abordando al bote hincha bostero.")
    else:
        print ("Abordando al bote hincha riverplatense.")
    time.sleep(2)

    bote.append(hincha_abordo)

    if len(bote) == 4:
        print ("\n Bote completo")
        a_remar()

    condition.release()

def a_remar():
    print ("\n Zarpamos al Santiago Berabeu!!\n")
    print ("Listado de hinchas presentes en el bote: ")
    print (bote)
    print ("\n")

    while True:
        for hincha_pasajero in range(4):
            print("El hincha", bote.pop(), "ha descendido del bote.")
            time.sleep(2)
        if len(bote) == 0:
            print("\n Bote vacío\n")
            break

River_Plate = threading.Thread(target=barra_brava_river, args=(12,))
Boca_Juniors = threading.Thread(target=barra_brava_boca, args=(12,))

River_Plate.start()
Boca_Juniors.start()

River_Plate.join()
Boca_Juniors.join()
