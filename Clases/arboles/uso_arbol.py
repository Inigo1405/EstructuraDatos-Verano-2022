# Iñigo Quintana Delgadillo

# 07/07/2022

class Nodo:
     def __init__(self, dato):
          self.dato = dato
          self.izq = None
          self.der = None





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



def get_profundidad_mismo_nivel(arbol, suma):
     if arbol is None:
          return suma
     else:
          return  get_profundidad_mismo_nivel(arbol.izq, suma=suma+1)



def get_profundidad(arbol):
     if arbol is None:
          return 0
     
     else:
          prof_izq = get_profundidad(arbol.izq)
          prof_der = get_profundidad(arbol.der)
          if prof_izq > prof_der:
               return prof_izq + 1
          else:
               return prof_der + 1 



def es_perfecto(arbol, deep, nivel=0):
     if arbol is None:
          return None
     
     if arbol.izq is None and arbol.der is None:
          return (deep == nivel + 1)
     if arbol.izq is None or arbol.der is None:
          return False   

     return es_perfecto(arbol.izq, deep, nivel+1) and es_perfecto(arbol.der, deep, nivel+1)
     


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


def sucesor(arbol):
     if arbol.izq is None:
          return arbol
     else:
          return sucesor(arbol.izq)




def eliminar(arbol, dato):
     if arbol is None:
          return None
     
     if dato < arbol.dato:
          arbol.izq = eliminar(arbol.izq, dato)

     elif dato > arbol.dato:
          arbol.der = eliminar(arbol.der, dato)


     else:
          # Caso 1: Cuando solo tiene un hijo 
          if arbol.izq is None:
               temp = arbol.der
               arbol = None
               return temp

          elif arbol.der is None:
               temp = arbol.izq
               arbol = None
               return temp
     
          # Caso 2: Cuando tiene dos hijos
          # encontrar el sucesor en inorden
          temp = sucesor(arbol.der)
          arbol.dato = temp.dato

          
          arbol.der = eliminar(arbol.der, temp.dato)
     
     return arbol


          


raiz = None
raiz = inserta(raiz, 8)
raiz = inserta(raiz, 3)
raiz = inserta(raiz, 1)
raiz = inserta(raiz, 6)
raiz = inserta(raiz, 7)
raiz = inserta(raiz, 10)
raiz = inserta(raiz, 14)
raiz = inserta(raiz, 4)



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



print(f'\nLa profundidad del arbol es: {get_profundidad(raiz)}')
print(f'El arbol tiene {cuantos_nodos(raiz)} nodos')


if es_perfecto(raiz, get_profundidad(raiz)):
     print("\nEl arbol binario es perfecto")
else:
     print("\nEl arbol binario no es perfecto")


num = 6
if busqueda(raiz, num):
     print(f'Encontre {num}')
else:
     print(f'No encontre {num}')

print()

delet = 1
print(f'Elimino el {delet}')
eliminar(raiz, delet)
inorden(raiz)