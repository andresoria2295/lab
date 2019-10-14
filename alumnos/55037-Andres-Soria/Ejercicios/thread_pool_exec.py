#!/usr/bin/python3

#Proporciona interfaz de alto nivel para iniciar tareas asincronicas.
from concurrent.futures import ThreadPoolExecutor
from time import sleep

#Espera 3 segundos antes de devolver el mensaje.
def message_processing(sms):
    sleep(3)
    return sms

#Construccion de ThreadPoolExecutor con el número de hilos que se quiere en el grupo.
#El número por defecto de hilos es de 5.
pool = ThreadPoolExecutor(3)

#Envio de una tarea al ejecutor del grupo de subprocesos. (a función message_processing)
future = pool.submit(message_processing, ("A good day for learn this!"))
#El objeto future posee un metodo done(), que manifiesta si el futuro se ha resuelto.
print(future.done())
sleep(5)
#Devuelve true si la llamada se cancelo o termino de ejecutarse. Caso contrario, devuelve false.
print(future.done())
#Se adquiere el resultado del objeto future (sms) llamando al metodo result().
print(future.result())
