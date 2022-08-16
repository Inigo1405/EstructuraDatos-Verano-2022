# Iñigo Quintana Delgadillo

# Remplaza las letras del árbol visto en clase, por números. El resultado deberá ser un árbol binario de búsqueda.
# Crea el mismo árbol en Python y ejecuta los 3 recorridos en profundidad.
# Comprueba los resultados.
# ¿Qué recorrido imprimió los nodos del árbol en orden?

# 01/07/2022

class Nodo:
     def __init__(self, dato):
          self.dato = dato
          self.izq = None
          self.der = None

"""
.                   ←10→
     ←5→                                ←16→
2         ←7→                   ←12→             18
     6          8           11        ←14→
.                                 13        15
"""
raiz = Nodo(10)

raiz.izq = Nodo(5)
raiz.der = Nodo(16)

raiz.izq.izq = Nodo(2)
raiz.izq.der = Nodo(7)
raiz.der.izq = Nodo(12)
raiz.der.der = Nodo(18)

raiz.izq.der.izq = Nodo(6)
raiz.izq.der.der = Nodo(8)
raiz.der.izq.izq = Nodo(11)
raiz.der.izq.der = Nodo(14)

raiz.der.izq.der.izq = Nodo(13)
raiz.der.izq.der.der = Nodo(15)


def preorden(arbol):
     if arbol:
          print(f'{arbol.dato}', end=' -> ')
          preorden(arbol.izq)
          preorden(arbol.der)

def postorden(arbol):
     if arbol:
          postorden(arbol.izq)
          postorden(arbol.der)
          print(f'{arbol.dato}', end=' -> ')

def inorden(arbol):
     if arbol:
          inorden(arbol.izq)
          print(f'{arbol.dato}', end=' -> ')
          inorden(arbol.der)




print("\nEl recorrido en preorden es: ")
preorden(raiz)
print("\nEl recorrido en postorden es: ")
postorden(raiz)
print("\nEl recorrido en inorden es: ")
inorden(raiz)

