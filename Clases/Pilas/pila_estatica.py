# Iñigo Quintana Delgadillo

# Pilas estatica (stack) pila que no aumenta la cantidad
# de sus elementos.

# 08/06/2022

class Pila_Estatica:
     # Crear pila_vacia
     def __init__(self, n):
          self.items = []
          self.n = n


     # Insertar dato al final de la lista (top)
     def push(self, x):
          if len(self.items) < self.n:
               self.items.append(x)
          else:
               print("La pila esta llena :(")
               print(f"Solo se pueden {self.n} elementos")


     # Extraer el último dato
     def pop(self):
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
          
               

# p = Pila_Estatica(5)       # Hacemos instancia de la clase

# p.push(10)
# p.push(10)
# p.push(10)
# p.push(10)
# p.push(10)
# p.push(10)
# p.mostrar()

# p.pop()
