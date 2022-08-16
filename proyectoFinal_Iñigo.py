"""
Mostrar un menú de opciones para realizar lo
siguiente:
     * Genera 20 números aleatorios y almacénalos en una estructura de datos
     * Inserta esos números a un árbol binario de búsqueda
     * Su recorrido en inorden deberá mostrar los números de menor a mayor.
     * ¿Cuáles son nodos hoja?
     * ¿Cuál es el nodo raíz?
     * ¿Cuál es la profundidad que tiene el árbol?
     * ¿Cuál es su peso?
     * ¿Es un árbol binario lleno?
     * ¿Es un árbol binario perfecto?
     * Eliminar nodo
     * Dibuja el árbol
"""


from random import randint
from Clases.Pilas.pila import Pila


class Nodo:
     def __init__(self, dato, prof=None):
          self.dato = dato
          self.deep = prof
          self.izq = None
          self.der = None


def inorden(arbol):
     if arbol:
          inorden(arbol.izq)
          print(f'{arbol.dato}', end=' -> ')
          inorden(arbol.der)


def cuantos_nodos(arbol):
     if arbol is None:
          return 0
     return (1 + cuantos_nodos(arbol.izq) + cuantos_nodos(arbol.der))


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


def nodoHoja(arbol):
     if arbol:
          if arbol.izq is None and arbol.der is None:
               print(arbol.dato)
               
          nodoHoja(arbol.izq)
          nodoHoja(arbol.der)
     
     
def estaLleno(arbol):
     if arbol is None:
          return None

     if arbol.izq is None and arbol.der is None:
          return True

     if arbol.izq is not None and arbol.der is not None:
          return estaLleno(arbol.izq) and estaLleno(arbol.der)
     return False


def llenarCola(arbol, colaNums = list()):
     if arbol:
          llenarCola(arbol.izq, colaNums)
          colaNums.append(arbol)
          llenarCola(arbol.der, colaNums)

          return colaNums


def inserta(arbol, dato, prof=1):
     if arbol is None:
          return Nodo(dato, prof)

     if dato < arbol.dato:
          arbol.deep = prof
          arbol.izq = inserta(arbol.izq, dato, arbol.deep + 1)

     elif dato > arbol.dato:
          arbol.deep = prof
          arbol.der = inserta(arbol.der, dato, arbol.deep + 1)


     return arbol


def subirProfundidad(arbol):
     if arbol:
          inorden(arbol.izq)
          inorden(arbol.der)
          arbol.deep -= 1

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
               arbol.der.deep -= 1
               temp = arbol.der
               arbol = None
               return temp

          elif arbol.der is None:
               arbol.izq.deep -= 1
               temp = arbol.izq
               arbol = None
               return temp
     
          # Caso 2: Cuando tiene dos hijos
          # encontrar el sucesor en inorden
          temp = sucesor(arbol.der)
          arbol.dato = temp.dato
          subirProfundidad(arbol.der)
          subirProfundidad(arbol.izq)  

          arbol.der = eliminar(arbol.der, temp.dato)
     
     return arbol


def es_perfecto(arbol, deep, nivel=0):
     if arbol is None:
          return None
     
     if arbol.izq is None and arbol.der is None:
          return (deep == nivel + 1)
     if arbol.izq is None or arbol.der is None:
          return False   

     return es_perfecto(arbol.izq, deep, nivel+1) and es_perfecto(arbol.der, deep, nivel+1)


# def preorden(arbol):
#      if arbol:
#           print(f'{arbol.dato}', end=' -> ')
#           print()
#           hilo1 = threading.Thread(target=preorden(arbol.izq))
#           hilo2 = threading.Thread(target=preorden(arbol.der))

#           hilo1.start()
#           hilo2.start()

          


def display(arbol, colaNums = list(), nivel=1):
     if arbol:
          for i in range(len(colaNums)):
               # print(colaNums[i].dato, end=' -> ')
               # print(colaNums[i].deep)
               # print(f'nivel: {nivel}')
               print()
               for j in range(len(colaNums)):
                    if colaNums[j].deep == nivel:
                         print(colaNums[j].dato, end='        ')
               nivel += 1
                    


def menu():
     print()
     print("1. Generar 20 números aleatorios")
     print("2. Mostrar los números de menor a mayor")
     print("3. ¿Cuáles son nodos hoja?")
     print("4. ¿Cuál es el nodo raíz?")
     print("5. ¿Cuál es la profundidad que tiene el árbol?")
     print("6. ¿Cuál es su peso?")
     print("7. ¿Es un árbol binario lleno?")
     print("8. ¿Es un árbol binario perfecto?")
     print("9. Eliminar nodo")
     print("10. Dibujar el árbol")
     print("11. salir")

     print("Ingrese la opción deseada: ")
     opc = int(input(": "))

     return opc






colaNums = list()
numeros = Pila()

opc = 0
while(opc != 11):
     opc = menu()
     if(opc == 1):
          print("\nGenerar 20 números aleatorios")
          # for x in range(20):
          #      numeros.push(randint(1, 50))
          numeros.push(16)
          numeros.push(6)
          numeros.push(17)
          numeros.push(36)
          numeros.push(7)
          numeros.push(40)
          numeros.push(29)
          numeros.push(27)
          numeros.push(26)
          numeros.push(11)
          numeros.push(35)
          numeros.push(22)
          numeros.push(1)
          numeros.push(2)
          numeros.push(37)
          numeros.push(38)
          numeros.push(12)
          numeros.push(23)
          numeros.push(19)
          numeros.push(24)

          numeros.mostrar()

          raiz = None
          for i in range(20):
               raiz = inserta(raiz, numeros.items[i])

          print("Árbol generado!")
     


     if(opc == 2):
          print("\nMostrar los números de menor a mayor")
          inorden(raiz)
          print()


     if(opc == 3):
          print("\n¿Cuáles son nodos hoja?")
          print(nodoHoja(raiz))


     if(opc == 4):
          print("\n¿Cuál es el nodo raíz?")
          print(f'La raíz del árbol es: {raiz.dato}')


     if(opc == 5):
          print("\n¿Cuál es la profundidad que tiene el árbol?")
          print(get_profundidad(raiz))

     if(opc == 6):
          print("\n¿Cuál es su peso?")
          print(cuantos_nodos(raiz))


     if(opc == 7):
          print("\n¿Es un árbol binario lleno?")
          if estaLleno(raiz):
               print("El arbol binario es lleno")
          else:
               print("El arbol binario no es lleno")


     if(opc == 8):
          print("\n¿Es un árbol binario perfecto?")
          if es_perfecto(raiz, get_profundidad(raiz)):
               print("El arbol binario es perfecto")
          else:
               print("El arbol binario no es perfecto")


     if(opc == 9):
          print("\nEliminar nodo")
          delet = int(input("Eliminar: "))
          raiz = eliminar(raiz, delet)


     if(opc == 10):
          print("\nDibujar el árbol")
          llenarCola(raiz, colaNums)
          # for x in range(len(colaNums)):
          #      print(colaNums[x].dato, end=' -> ')
          #      print(colaNums[x].deep)
          display(raiz, colaNums)
          colaNums.clear()
          
         


