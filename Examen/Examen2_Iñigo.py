"""
Iñigo Quintana Delgadillo


Una librería tiene una colección de libros, se
quiere calcular el precio total de todos los libros

Crea una función recursiva que permita obtener la 
sumatoria del precio de la colección de libros.

Implementa alguna estructura de datos que permita almacenar los precios de los libros


27/06/2022
"""
from Clases.Pilas.pila import Pila


class PrecioLibros():
     def __init__(self, libros = Pila(), precio = Pila()):
          self.libros = libros
          self.precio = precio
          

     def costo(self, n):
          # Caso base
          if self.precio.is_empty() == True:
               return n
               
          # Caso general     
          else:
               precio = self.precio.pop()
               costoTotal =  n + precio
               print(f'Libro: {self.libros.pop()} precio: ${precio}, costo colección: {costoTotal}')

               return self.costo(costoTotal)
               



libros = Pila()
precio = Pila()


libros.push('libro 1')
precio.push(480)

libros.push('libro 2')
precio.push(375)

libros.push('libro 3')
precio.push(649)

libros.push('libro 4')
precio.push(112)

libros.push('libro 5')
precio.push(800)

libros.push('libro 6')
precio.push(99)


libros.mostrar()
precio.mostrar()
print()



costoTotal = PrecioLibros(libros, precio)
print(f'\nLa colección de libros tiene un costo total de: ${costoTotal.costo(0)}')
