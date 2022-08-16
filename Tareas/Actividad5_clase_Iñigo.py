# Iñigo Quintana Delgadillo

# Desarrolla un TDA (clase) del método de la burbuja

# 06/06/2022


import random

class Burbuja:
     """
     class Burbuja
     ---------
     Clase llamada Burbuja, realiza el método burbuja para ordenar
     """
     def __init__(self, lista, n):
          """
          Función `__init__` 
          ---------
          Esta función se realiza una vez que es llamada la clase,
          datos a pedir: 
               * `lista`: 
               * `length`: longitud de la lista
          """

          self.lista = lista
          self.n = n
          # Método de la burbuja: 
          for i in range(self.n - 1):
               for j in range(self.n - 1):
                    if self.lista[j] > self.lista[j+1]:               # Usa j por ser el for interno que va a comparar
                         self.tmp = self.lista[j]
                         self.lista[j] = self.lista[j+1]
                         self.lista[j+1] = self.tmp
                    
          print("Lista ordenada: ")
          print(self.lista)
          

lista_random = random.sample(range(100), 10)
n = len(lista_random)
print(lista_random)


Burbuja(lista_random, n)