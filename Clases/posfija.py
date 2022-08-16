# Iñigo Quintana Delgadillo

# Crea un programa en Python que dada una
# expresión en notación postfija, la evalue y
# devuelva su resultado

# 13/06/2022

from Pilas.pila import Pila


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



pila_operandos = Pila()

def calculardora_posfijo(postfijo):
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


     print(f'\nPostfijo: {postfijo} = {res}')






