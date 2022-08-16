"""
Iñigo Quintana Delgadillo

Convertir una expresion prefijas a postfijas, 
utilizando las pilas.

09/06/2022 - 15/06/2022


REGLAS: 
-----------
- Operador = prioridad  --->  Cambiarlos
- Operador > prioridad  --->  Se agrega a la pila
- Operador < prioridad  --->  Se saan los operadores
- Parentesís derecho    --->  Vaciar pila*
-----------


* pila = operadores
* cadena = postfijo

Prefija       Postfija
3 + 4   --->  34+



EJEMPLO:
-----------                             Operadores
(3+5)*(8+2)                                 |
↑↑                                          |                     # Operadores:  +, -, *, /, ^, sqrt
(3                                          |   +                 # Operando:    Números
.                                       +   | ( , )
.                                     ( , ) |   *                 # Al encontrar ) va sacando los operadores y los coloca en posfijo
.                                                                 # hasta encontrar (, y luego se eliminan.
Postfijo:    35+82+*
"""

from Pilas.pila import Pila 
from posfija import calculardora_posfijo, calcular_prioridad, es_operador;



pila_operadores = Pila()
postfijo = '';


expresion = input('Ingresa una expresión matemática: ')

print(expresion)
for c in expresion:
     if es_operador(c):
          while not pila_operadores.is_empty() and calcular_prioridad(c) <= calcular_prioridad(pila_operadores.top()) and pila_operadores.top() != '(':
               # print("La pila no esta vacia")
               # print(f'{c} <= {pila_operadores.top()}')
               postfijo += c
               pila_operadores.pop()
          pila_operadores.push(c)


     elif c == '(':
          # print(f'{c} es el primer parentesis')
          pila_operadores.push(c)
          

     elif c == ')':
          # print(f'{c} es el segundo parentesis')
          while pila_operadores.top() != '(':
               # print(pila_operadores.top())
               postfijo += pila_operadores.pop()       # concatenamos el último elemento
          pila_operadores.pop()                        # Elimina el '(' de la pila
                    

     else:
          # Añadimos a la cadena postfijo
          postfijo += c                                # concatenamos



while not pila_operadores.is_empty():                  # Agrega los elementos faltantes
     postfijo += pila_operadores.pop()



calculardora_posfijo(postfijo)



