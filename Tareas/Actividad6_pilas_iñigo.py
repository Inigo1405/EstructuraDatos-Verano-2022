# Iñigo Quintana Delgadillo

# Pilas (stack)

# 07/06/2022

class Pila:
     # Crear pila_vacia
     def __init__(self):
          self.items = []


     # Insertar dato al final de la lista (top)
     def push(self, x):
          self.items.append(x)


     # Extraer el último dato
     def pop(self):
          if self.is_empty():
               print("Pila vacia", self.items)
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
          
               

pila = Pila()       # Hacemos instancia de la clase

# Llena la pila con números ingresados por el usuario
x = int(input("Cuantos datos desea ingresar a la pila?: "))
for i in range(x):
     pila.push(int(input(': ')))


print("\nPila llena: ")
pila.mostrar()

# Borra los datos de la pila
print("\nBorrando pila: ")
for j in range(x):
     pila.mostrar()
     pila.pop()

print("\nPila vacia:", pila.is_empty())

