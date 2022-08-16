class Nodo:
     def __init__(self, dato):
          self.dato = dato
          self.izq = None
          self.der = None



class Arbol():
     def __init__():
          pass

     def preorden(self, arbol):
          if arbol:
               print(f'{arbol.dato}', end=' -> ')
               self.preorden(arbol.izq)
               self.preorden(arbol.der)



     def postorden(self, arbol):
          if arbol:
               self.postorden(arbol.izq)
               self.postorden(arbol.der)
               self.print(f'{arbol.dato}', end=' -> ')



     def inorden(self, arbol):
          if arbol:
               self.inorden(arbol.izq)
               print(f'{arbol.dato}', end=' -> ')
               self.inorden(arbol.der)
          


     def estaLleno(self, arbol):
          if arbol is None:
               return None

          if arbol.izq is None and arbol.der is None:
               return True

          if arbol.izq is not None and arbol.der is not None:
               return self.estaLleno(arbol.izq) and self.estaLleno(arbol.der)
          return False



     def get_profundidad_mismo_nivel(self, arbol, suma):
          if arbol is None:
               return suma
          else:
               return  self.get_profundidad_mismo_nivel(arbol.izq, suma=suma+1)



     def get_profundidad(self, arbol):
          if arbol is None:
               return 0
          
          else:
               prof_izq = self.get_profundidad(arbol.izq)
               prof_der = self.get_profundidad(arbol.der)
               if prof_izq > prof_der:
                    return prof_izq + 1
               else:
                    return prof_der + 1 



     def es_perfecto(self, arbol, deep, nivel=0):
          if arbol is None:
               return None
          
          if arbol.izq is None and arbol.der is None:
               return (deep == nivel + 1)
          if arbol.izq is None or arbol.der is None:
               return False   

          return self.es_perfecto(arbol.izq, deep, nivel+1) and self.es_perfecto(arbol.der, deep, nivel+1)
          


     def busqueda(self, arbol, dato):
          if arbol is None:
               return None

          if dato == arbol.dato:
               return True

          if dato < arbol.dato:
               return self.busqueda(arbol.izq, dato)

          elif dato > arbol.dato:
               return self.busqueda(arbol.der, dato)
          return False



     def cuantos_nodos(self, arbol):
          if arbol is None:
               return 0
          return (1 + self.cuantos_nodos(arbol.izq) + self.cuantos_nodos(arbol.der))



     def inserta(self, arbol, dato):
          if arbol is None:
               return Nodo(dato)
          
          if dato < arbol.dato:
               arbol.izq = self.inserta(arbol.izq, dato)

          elif dato > arbol.dato:
               arbol.der = self.inserta(arbol.der, dato)

          return arbol


     def sucesor(self, arbol):
          if arbol.izq is None:
               return arbol
          else:
               return self.sucesor(arbol.izq)




     def eliminar(self, arbol, dato):
          if arbol is None:
               return None
          
          if dato < arbol.dato:
               arbol.izq = self.eliminar(arbol.izq, dato)

          elif dato > arbol.dato:
               arbol.der = self.eliminar(arbol.der, dato)


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
               temp = self.sucesor(arbol.der)
               arbol.dato = temp.dato

               
               arbol.der = self.eliminar(arbol.der, temp.dato)
          
          return arbol