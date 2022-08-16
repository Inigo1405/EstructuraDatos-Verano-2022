# Iñigo Quintana Delgadillo

# Cola dinamica

# 10/06/2022


class Cola:
     """
     Class Cola Dinamica
     ---------
     Clase que contiene las funciones para manejar una cola:
     * `enqueue`: agregar dato
     * `dequeue`: eliminar dato
     * `is_empty`: comprobar si esta vacío
     * `first`: buscar primer dato
     * `last`: buscar último dato
     * `size`: tamaño de la cola
     * `display`: imprimir lista
     """
     
     def __init__(self):
          self.items = list()
          

     # Insertar (Encolar)
     def enqueue(self, x):
          """Insertar datos en la cola"""
          self.items.append(x)


     # Eliminar (Desencolar)
     def dequeue(self):
          """Eliminar datos de la cola"""
          return self.items.pop(0)                       # Eliminamos el primer elemento
          

     #Si esta vacía
     def is_empty(self):
          return True if self.items else False    # if Ternarios


     def first(self):
          return self.items[0]


     def last(self):
          return self.items[-1]                           


     def size(self):
          return len(self.items)


     def display(self):
          print(self.items)
          
