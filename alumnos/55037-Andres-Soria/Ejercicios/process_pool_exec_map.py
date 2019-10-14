#!/usr/bin/python3

from concurrent.futures import ProcessPoolExecutor
#from concurrent.futures import as_completed

#Arreglo de valores arbitrarios.
valores = [2,3,4,5]

#Funcion que efectua operacion matematica.
def operador(n):
   return n * n

def main():
   #executor = ProcessPoolExecutor(max_workers = 3)
   with ProcessPoolExecutor(max_workers = 3) as executor:
      #Función executor.map utilizada para aplicar la función operador() a cada valor del arreglo declarado.
      resultados = executor.map(operador, valores)
   for numero in resultados:
      print(numero)

if __name__ == '__main__':
   main()
