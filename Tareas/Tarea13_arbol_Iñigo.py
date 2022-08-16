# Iñigo Quintana Delgadillo
# Estructura de datos no lineal: ÁRBOL
# 01/07/2022


class Nodo:
     def __init__(self, dato):
          self.dato = dato
          self.izq = None
          self.der = None

raiz = Nodo(1)
print(raiz.dato)
print()

raiz.izq = Nodo(12)
raiz.der = Nodo(9)
raiz.izq.izq = Nodo(5)
raiz.izq.der = Nodo(6)
raiz.izq.der.izq = Nodo(2)
raiz.izq.der.der = Nodo(10)


def preorden(arbol):
     """
     1. Visita el nodo raíz
     2. Visita todos los nodos en el subárbol izquierdo
     3. Visita todos los nodos en el subárbol derecho
     """
     if arbol:
          print(f'{arbol.dato}', end=' -> ')
          preorden(arbol.izq)
          preorden(arbol.der)

print("El recorrido en preorden es: ")
preorden(raiz)



def postorden(arbol):
     """
     1. Visita todos los nodos en el subárbol izquierdo
     2. Visita todos los nodos en el subárbol derecho
     3. Visita el nodo raíz
     """
     if arbol:
          postorden(arbol.izq)
          postorden(arbol.der)
          print(f'{arbol.dato}', end=' -> ')


print("\nEl recorrido en postorden es: ")
#postorden(raiz)




def inorden(arbol):
     """
     1. Visita todos los nodos en el subárbol izquierdo
     2. Visita el nodo raíz
     3. Visita todos los nodos en el subárbol derecho
     """
     if arbol:
          inorden(arbol.izq)
          print(f'{arbol.dato}', end=' -> ')
          inorden(arbol.der)

print("\nEl recorrido en inorden es: ")
inorden(raiz)