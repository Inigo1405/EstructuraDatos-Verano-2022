# Iñigo Quintana Delgadillo

# Crear una clase llamada Nodo

# 21/06/2022


class Nodo():
     def __init__(self, data):
          self.data = data
          self.next = None




class ListaLigada:
     def __init__(self):
          self.cabeza = None


     def insertar(self, nuevo_nodo):
          # Comprobar si la lista ligada esta vacía
          if self.cabeza:
               # Obtener último nodo
               ultimo_nodo = self.cabeza
               while ultimo_nodo.next != None:
                    ultimo_nodo = ultimo_nodo.next
               # Asignar el nuevo nodo al siguiente puntero del ultimo nodo
               ultimo_nodo.next = nuevo_nodo

          else: #La cabeza esta vacía
               # Asignamos el nodo a la cabeza
               self.cabeza = nuevo_nodo

     
     def eliminar(self):
          # Comprobar si la lista ligada no esta vacía
          if self.cabeza:
               # Obtener último nodo
               nodo_temporal = self.cabeza
               while nodo_temporal.next != None:
                    nodo_anterior = nodo_temporal
                    nodo_temporal = nodo_temporal.next
               # Eliminar nodo
               nodo_anterior.next = None
               
          else:
               print("Esta vacía!")


     def limpiar_nodo(self):
          if self.cabeza.next:
               nodo_temporal = self.cabeza
               while nodo_temporal.next != None:
                    nodo_temporal = nodo_temporal.next
               print(nodo_temporal.data)
               print(nodo_temporal.next)
               
               nodo_temporal.data = None
               nodo_temporal.next = None

          else:
               print("Esta vacía!")
     

     def display(self):
          nodo_temporal = self.cabeza
          while nodo_temporal != None:
               print(f'{nodo_temporal.data}', end=' -> ')
               nodo_temporal = nodo_temporal.next
          print('Null')




mi_lista_ligada = ListaLigada()
n1 = Nodo(4)  

mi_lista_ligada.insertar(n1)
mi_lista_ligada.insertar(Nodo(6))
mi_lista_ligada.insertar(Nodo(8))
mi_lista_ligada.insertar(Nodo(10))

mi_lista_ligada.display()


mi_lista_ligada.eliminar()
mi_lista_ligada.display()

mi_lista_ligada.eliminar()
mi_lista_ligada.display()   

mi_lista_ligada.eliminar()
mi_lista_ligada.display()
