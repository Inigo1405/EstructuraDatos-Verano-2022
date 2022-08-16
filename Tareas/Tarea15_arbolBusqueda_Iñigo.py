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
     ←5→                               ←16→
2         ←7→                   ←12→             18
     6          8           11        ←14→
.                                 13        15
"""
# raiz = Nodo(10)

# raiz.izq = Nodo(5)
# raiz.der = Nodo(16)

# raiz.izq.izq = Nodo(2)
# raiz.izq.der = Nodo(7)
# raiz.der.izq = Nodo(12)
# raiz.der.der = Nodo(18)

# raiz.izq.der.izq = Nodo(6)
# raiz.izq.der.der = Nodo(8)
# raiz.der.izq.izq = Nodo(11)
# raiz.der.izq.der = Nodo(14)

# raiz.der.izq.der.izq = Nodo(13)
# raiz.der.izq.der.der = Nodo(15)


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
     
     



def estaLleno(arbol):
     if arbol is None:
          return None

     if arbol.izq is None and arbol.der is None:
          return True

     if arbol.izq is not None and arbol.der is not None:
          return estaLleno(arbol.izq) and estaLleno(arbol.der)
     return False


def get_profundidad(arbol, suma):
     if arbol is None:
          return suma
     else:
          return get_profundidad(arbol.izq, suma=suma+1)



def es_perfecto(arbol, deep, nivel=0):
     if arbol is None:
          return None
     
     if arbol.izq is None and arbol.der is None:
          return (deep == nivel + 1)
     if arbol.izq is None or arbol.der is None:
          return False   

     return es_perfecto(arbol.izq, deep, nivel+1) and es_perfecto(arbol.der, deep, nivel+1)
     


def cuantos_nodos(arbol):
     if arbol is None:
          return 0
     return (1 + cuantos_nodos(arbol.izq) + cuantos_nodos(arbol.der))


def inserta(arbol, dato):
     if arbol is None:
          return Nodo(dato)
     
     if dato < arbol.dato:
          arbol.izq = inserta(arbol.izq, dato)

     elif dato > arbol.dato:
          arbol.der = inserta(arbol.der, dato)


     return arbol



def busqueda(arbol, dato):
     if arbol is None:
          return None

     if dato == arbol.dato:
          return True

     if dato < arbol.dato:
          return busqueda(arbol.izq, dato)

     elif dato > arbol.dato:
          return busqueda(arbol.der, dato)
     return False

     




raiz = None
raiz = inserta(raiz, 8)
raiz = inserta(raiz, 3)
raiz = inserta(raiz, 10)



# print("\nEl recorrido en preorden es: ")
# preorden(raiz)
# print("\nEl recorrido en postorden es: ")
# postorden(raiz)

print("\nEl recorrido en inorden es: ")
inorden(raiz)

print()
if estaLleno(raiz):
     print("El arbol binario es lleno")
else:
     print("El arbol binario no es lleno")



print(f'La profundidad del arbol es: {get_profundidad(raiz, 0)}')
print(f'El arbol tiene {cuantos_nodos(raiz)}')


if es_perfecto(raiz, get_profundidad(raiz, 0)):
     print("\nEl arbol binario es perfecto")
else:
     print("\nEl arbol binario no es perfecto")


num = 10
if busqueda(raiz, num):
     print(f'Encontre {num}')
else:
     print(f'No encontre {num}')