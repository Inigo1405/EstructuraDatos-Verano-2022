# Iñigo Quintana Delgadillo

# Crea un programa en Python que dada una
# expresión en notación postfija, la evalue y
# devuelva su resultado

# 13/06/2022

from Clases.Pilas.pila import Pila


def es_operador(c):
     operadores = list('+-*/^')
     return c in operadores


def calcular_prioridad(c):
     if c == '+' or c == '-':
          return 1
     if c == '*' or c == '/':
          return 2
     else:
          return 3


def calcular(op1, op2, c):
     if c == '+':
          return int(op1) + int(op2)         # Casting --> Cambia de tipo de variable (Str -> Int)
     elif c == '-':
          return int(op1) - int(op2)
     elif c == '*':
          return int(op1) * int(op2)
     elif c == '/':
          return int(op1) / int(op2)
     elif c == '^':
          return int(op1) ** int(op2)      



pila_operadores = Pila()
pila_operandos = Pila()
expresion = '((3+5)*2)-1' # input("Ingresa la expresión: ") # Colocar expresión entre parentesis, ejemplo: '((3+5)*(8+2))', '(3+2)'
postfijo = ''


print(expresion)
for c in expresion:
     if es_operador(c):
          while not pila_operadores.is_empty() and calcular_prioridad(c) <= calcular_prioridad(pila_operadores.top()) and pila_operadores.top() != '(':
               print("La pila no esta vacia")
               print(f'{c} <= {pila_operadores.top()}')
               postfijo += c
               pila_operadores.pop()
          
          pila_operadores.push(c)


     elif c == '(':
          # print(f'{c} es el primer parentesis')
          pila_operadores.push(c)
          

     elif c == ')':
          # print(f'{c} es el segundo parentesis')
          while pila_operadores.top() != '(':
               print(pila_operadores.top())       
               postfijo += pila_operadores.pop()       # concatenamos el último elemento

          pila_operadores.pop()                        # Elimina el '(' de la pila
                    

     else:
          # Añadimos a la cadena postfijo
          postfijo += c                                # concatenamos
          



while not pila_operadores.is_empty():                  # Agrega los elementos faltantes
     postfijo += pila_operadores.pop()


# for i, c in enumerate(postfijo):
#      print(f'{i}: {c}')


for c in postfijo:
     print(c) 
     if es_operador(c):
          op2 = pila_operandos.pop()
          op1 = pila_operandos.pop()
          res = calcular(op1, op2, c)
          pila_operandos.push(res)

     else: # es operando
          pila_operandos.push(c)

print("Último dato")
res = pila_operandos.pop()




print("\nPila de operadores: ")
pila_operadores.mostrar()
print("Pila de operando: ")
pila_operandos.mostrar()
print(f'Postfijo: {postfijo} = {res}')






