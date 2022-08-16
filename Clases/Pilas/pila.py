# Iñigo Quintana Delgadillo

# Pilas (stack)

# 07/06/2022

class Pila:
     """
     Class Pila Dinamica (stack)
     ---------
     Clase que contiene las funciones para manejar una pila:
     * `push`: agregar dato
     * `pop`: eliminar dato
     * `is_empty`: comprobar si esta vacío
     * `top`: buscar último dato
     * `mostrar`: imprimir lista
     """
     
     # Crear pila_vacia
     def __init__(self):
          self.items = []


     # Insertar dato al final de la lista (top)
     def push(self, x):
          """Agrega datos a la pila"""
          self.items.append(x)


     # Extraer el último dato
     def pop(self):
          """Elimina datos de la pila"""
          if self.is_empty():
               print("La pila ya esta vacia", self.items)
          else:
               return self.items.pop()
          


     # Pregunta si esta vacia la lista
     def is_empty(self):
          if self.items:
               return False
          else:
               return True
     

     # Regresa el último dato de la pila
     def top(self):
          return self.items[-1]  

     # Imprime la pila
     def mostrar(self):
          print(self.items)
          
               


# pila = Pila()       # # Hacemos instancia de la clase

# pila.push(4)
# pila.push(6)

# print("Pila llena: ")
# pila.mostrar()

# while pila.is_empty != True:
#      pila.pop()
#      pila.mostrar()

