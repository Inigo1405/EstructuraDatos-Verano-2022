# Iñigo Quintana Delgadillo

# Invierte una cadena usando pilas

# 08/06/2022

from pila import Pila

p = Pila()
p2 = Pila()


word = input("Ingrese una palabra: ")
for i in word:                               # Registra en la pila por caracter el string ingresado
     p.push(i)   

p.mostrar()


for i in range(len(p.items)):
     print(p.top())
     p2.push(p.top())
     p.pop()
     
p2.mostrar()




