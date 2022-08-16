# Iñigo Quintana Delgadillo

# Completar el método eliminar_inicio

# 21/06/2022 - 22/06/2022


class Nodo():
     def __init__(self, data):
          self.data = data
          self.next = None




class ListaLigada:
     def __init__(self):
          self.cabeza = None
          self.contador = 0

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
          self.contador = self.contador + 1


     def insertar_inicio(self, nuevo_nodo):
          primer_nodo = self.cabeza
          self.cabeza = nuevo_nodo
          nuevo_nodo.next = primer_nodo
          self.contador = self.contador + 1


     def insertar_pos(self, nuevo_nodo, pos):
          if self.cabeza:
               if pos == 0:
                    self.insertar_inicio(nuevo_nodo)
               
               elif pos >= self.contador:
                    print("Ese indice no existe, overflow!")

               else: 
                    print('\nBuscando...')
                    i = 0
                    actual_nodo = self.cabeza
                    while i < pos and actual_nodo.next != None:
                         print(f'Buscando... {i}')
                         actual_nodo = actual_nodo.next
                         i += 1
                    print(F'Te encontre! pos: {i}, dato: {actual_nodo.data}')

                    nuevo_nodo.next = actual_nodo.next
                    actual_nodo.next = nuevo_nodo
          else:
               print("Aún no tengo datos :(")
          
          self.contador = self.contador + 1
               
     def cantidad(self):
          return self.contador


     
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
          self.contador = self.contador - 1


     def eliminar_inicio(self):
          if self.cabeza:
               self.cabeza = self.cabeza.next
          self.contador = self.contador - 1


     def eliminar_pos(self, pos):
          if self.cabeza:
               if pos == 0:
                    self.eliminar_inicio()

               elif pos >= self.contador:
                    print("Ese indice no existe, overflow!")

               else:
                    print('\nBuscando...')
                    i = 0
                    actual_nodo = self.cabeza
                    while i < pos:
                         print(f'Buscando... {i}')
                         nodo_anterior = actual_nodo
                         actual_nodo = actual_nodo.next
                         i += 1
                    print(F'Te encontre! pos: {i}, dato: {actual_nodo.data}')
                    siguiente_nodo = actual_nodo.next
                    nodo_anterior.next = siguiente_nodo

          else:
               print("Aún no tengo datos :(")
          self.contador = self.contador - 1


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


     def obtener(self, pos):
          if self.cabeza:
               if pos == 0:
                    nodo = self.cabeza
                    return nodo.data
               
               elif pos >= self.contador:
                    return None

               else:
                    i = 0
                    actual_nodo = self.cabeza
                    while i < pos and actual_nodo.next != None:
                         actual_nodo = actual_nodo.next
                         i += 1
                    return actual_nodo.data

          else:
               return None #No hay nodos



mi_lista_ligada = ListaLigada()
n1 = Nodo(4)  

mi_lista_ligada.insertar(n1)
mi_lista_ligada.insertar(Nodo(6))
mi_lista_ligada.insertar(Nodo(8))
mi_lista_ligada.insertar(Nodo(10))
mi_lista_ligada.insertar_inicio(Nodo(2))

print(f'Cantidad de nodos: {mi_lista_ligada.cantidad()}')
mi_lista_ligada.display()

mi_lista_ligada.insertar_pos(Nodo(1), 2)
mi_lista_ligada.display()


# mi_lista_ligada.eliminar()
# mi_lista_ligada.display()

# mi_lista_ligada.eliminar_inicio()
# mi_lista_ligada.display()

mi_lista_ligada.eliminar_pos(3)
mi_lista_ligada.display()





