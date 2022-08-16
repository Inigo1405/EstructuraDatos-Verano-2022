"""
Iñigo Quintana Delgadillo

# En un pequeño banco existen tres cajeros que atienden a los clientes que van llegando, 
# cada cliente tiene una duración diferente que es el tiempo que estará con el cajero. 
# La fila de clientes deberá ser una cola. 
# Al inicio los tres cajeros estarán disponibles, posteriormente se irán liberando los cajeros conforme al tiempo del cliente. 
# Cuando un cajero se libere, este podrá atender a otro cliente. 
# Muestra en pantalla como los cajeros se van liberando y al cliente que atienden. 

# Nota: crea una clase llamada cajero con el atributo “disponible” (bool). Así podrás crear 3 instancias de cajero


26/06/2022
"""

from Colas.cola import Cola
import threading
import time


class Cajero():
     def __init__(self, name, cola = Cola(), x = Cola()):
          self.disponible = True
          self.cola = cola
          self.name = name
          self.timeClient = x
          

     def is_available(self):
          if self.disponible == True:
               print(f'{self.name} ya disponible!\n')
               return True

          else: 
               print(f'{self.name} no disponible!\n') 
               return False


     def atender(self):
          if self.cola:
               for i in range(self.cola.size()):
                    if self.cola.is_empty() == True: 

                         cliente = self.cola.dequeue()
                         # print(cliente)
                         tiempo = self.timeClient.dequeue()
                         # print(tiempo)
                         

                         time.sleep(int(tiempo))
                         print(f'{self.name} atendio a: {cliente}, tardo {tiempo}s')

          else:
               print("No hay datos")
          


fila_banco = Cola()
tiempo_cliente = Cola()

# fila_banco.enqueue({3:'Iñigo'})
# fila_banco.enqueue({1:'Sabine'})
# fila_banco.enqueue({2:'Naomi'})
# fila_banco.enqueue({6:'Alexis'})
# fila_banco.enqueue({2:'Xime'})


# print(fila_banco.first())
# print(fila_banco.first()['Iñigo'])


fila_banco.enqueue('Iñigo')
tiempo_cliente.enqueue(10)

fila_banco.enqueue('Sabine')
tiempo_cliente.enqueue(1)

fila_banco.enqueue('Naomi')
tiempo_cliente.enqueue(2)

fila_banco.enqueue('Alexis')
tiempo_cliente.enqueue(6)

fila_banco.enqueue('Xime')
tiempo_cliente.enqueue(2)

fila_banco.enqueue('Alfredo')
tiempo_cliente.enqueue(2)

fila_banco.enqueue('Dani')
tiempo_cliente.enqueue(4)

print("Cola que se forma en el banco: ")
fila_banco.display()



cajero1 = Cajero('Cajero 1', fila_banco, tiempo_cliente)
cajero2 = Cajero('Cajero 2', fila_banco, tiempo_cliente)
cajero3 = Cajero('Cajero 3', fila_banco, tiempo_cliente)



C1 = threading.Thread(target=cajero1.atender)     
C2 = threading.Thread(target=cajero2.atender)
C3 = threading.Thread(target=cajero3.atender)




C1.start()
C2.start()
C3.start()



