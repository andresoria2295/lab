#!/usr/bin/python3

#Proporciona interfaz de alto nivel para iniciar tareas asincronicas.
from concurrent.futures import ProcessPoolExecutor
from time import sleep

#Espera 2 segundos antes de devolver el mensaje.
def processing(sms):
   sleep(2)
   return sms

def main():
   #Construccion de ProcessPoolExecutor con el número de procesos que se quiere en el grupo.
   executor = ProcessPoolExecutor(5)
   #Envio de una tarea al ejecutor del grupo de procesos. (a función processing)
   future = executor.submit(processing, ("Work done!"))
   #El objeto executor posee un metodo done(), que manifiesta si el ejecutor se ha resuelto.
   print(future.done())
   sleep(3)
   #Devuelve true si la llamada se cancelo o termino de ejecutarse. Caso contrario, devuelve false.
   print(future.done())
   #Se adquiere el resultado del objeto executor (sms) llamando al metodo result().
   print(future.result())

if __name__ == '__main__':
    main()
