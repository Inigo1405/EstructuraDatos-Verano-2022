# Iñigo Quintana Delgadillo

# Implementa una cola circular en Python

# 16/06/2022


class ColaCircular():
     """
     Class ColaCircular (Estática)
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
     

     def __init__(self, n):
          self.items = [None] * 5
          self.n = n
          self.front = -1      
          """ Apuntador -> First"""
          self.rear = -1      
          """Apuntador -> Last"""


     # Insertar (Encolar)
     def enqueue(self, dato):
          """Insertar datos en la cola"""
          if (self.rear + 1) % self.n == self.front:
               print("\n-- La pila esta llena :(      -- ")
               print(f"-- Solo se pueden {self.n} elementos --\n")
              
          elif self.front == -1:
               self.front = 0
               self.rear = 0
               self.items[self.rear] = dato
         
          else:
               self.rear = (self.rear + 1) % self.n
               self.items[self.rear] = dato


     # Eliminar (Desencolar)
     def dequeue(self):
          """Eliminar datos de la cola"""
          if self.front == -1:
               print("\n-- La pila esta vacía :(      -- ")
          
          elif self.front == self.rear:
               temp = self.items[self.front]
               self.front = -1
               self.rear = -1
               return temp

          else:
               temp = self.items[self.front]
               self.front = (self.front + 1 ) % self.n
               return temp


     #Si esta vacía
     def is_empty(self):
          return True if self.items else False    # if Ternarios


     def first(self):
          """Regresa el elemento al inicio de la cola"""
          return self.items[self.front]


     def last(self):
          """Regresa el elemento al final de la cola"""
          return self.items[self.rear]                           


     def size(self):
          """Regresa el tamaño de la cola"""
          return len(self.items)


     def display(self):
          """Imprime la cola circular"""
          if self.front == -1:
               print("No hay elementos en la Cola Circular :(")
          
          elif self.rear > self.front:
               for i in range(self.front, self.rear+1):
                    print(self.items[i], end=', ')                # Imprime de manera horizontal
               print()

          else:                                                   # self.front > self.rear
               sp = self.front
               for i in range(self.n):
                    print(self.items[sp % self.n], end=', ')
                    sp += 1
               print()
                    

               

# -- OPCION 1 -- 
# for i in range(self.front, self.n):
#      print(self.items[i], end=' ')
# print()
#                
# for i in range(self.rear+1):
#      print(self.items[i], end=' ')
# print()


# -- OPCION 2 --
# elif self.front > self.rear:
#      sp = self.front
#      for i in range(self.n):
#           pos = sp % self.n
#           print(self.items[pos], end=', ')
#           sp += 1


c = ColaCircular(5)

c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
c.enqueue(4)

print(c.items)
print(f'Size: {c.size()}\n')

c.display()
print(f'Head element: {c.first()}')
print(f'Tail element: {c.last()}\n')



c.dequeue()
c.enqueue(5)
c.enqueue(6)

c.display()
print(f'Head element: {c.first()}')
print(f'Tail element: {c.last()}\n')



c.dequeue()
c.dequeue()
c.enqueue(7)
c.enqueue(8)

c.display()
print(f'Head element: {c.first()}')
print(f'Tail element: {c.last()}\n')



c.dequeue()
c.enqueue(9)

c.display()
print(f'Head element: {c.first()}')
print(f'Tail element: {c.last()}\n')


print(c.items)