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

def numeros(c):
     """Convierte de char a int"""
     if c == '1':
          return 1
     if c == '2':
          return 2
     if c == '3':
          return 3
     if c == '4':
          return 4
     if c == '5':
          return 5
     if c == '6':
          return 6
     if c == '7':
          return 7
     if c == '8':
          return 8
     if c == '9':
          return 9


pila_operadores = Pila()
pila_operando = Pila()
postfijo = ''
expresion = input("Ingresa la expresión: ") # Colocar expresión entre parentesis, ejemplo: '((3+5)*(8+2))', '(3+2)'
resultado = int


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
               
               # Operación
               # Suma
               if(pila_operadores.top() == '+'):
                    pila_operando.mostrar()  
                    resultado = pila_operando.top()
                    pila_operando.pop()

                    resultado += pila_operando.top()
                    pila_operando.pop()
                    pila_operando.push(resultado)


               # Resta
               if(pila_operadores.top() == '-'):
                    pila_operando.mostrar()  
                    resultado = pila_operando.top()
                    pila_operando.pop()

                    resultado = pila_operando.top() - resultado 
                    pila_operando.pop()
                    pila_operando.push(resultado)


               # Multiplicación
               if(pila_operadores.top() == '*'):
                    pila_operando.mostrar()  
                    resultado = pila_operando.top()
                    pila_operando.pop()

                    resultado *= pila_operando.top()
                    pila_operando.pop()
                    pila_operando.push(resultado)


               # División
               if(pila_operadores.top() == '/'):
                    pila_operando.mostrar()  
                    resultado = pila_operando.top()
                    pila_operando.pop()

                    resultado = pila_operando.top() / resultado 
                    pila_operando.pop()
                    pila_operando.push(resultado)
                    

               # Exponente    
               if(pila_operadores.top() == '^'):
                    pila_operando.mostrar()  
                    resultado = pila_operando.top()
                    pila_operando.pop()

                    resultado = pila_operando.top() ** resultado
                    pila_operando.pop()
                    pila_operando.push(resultado)
               
               
               postfijo += pila_operadores.pop()       # concatenamos el último elemento



          pila_operadores.pop()                        # Elimina el '(' de la pila
                    

     else:
          # Añadimos a la cadena postfijo
          postfijo += c                                # concatenamos
          x = numeros(c)
          pila_operando.push(x)



while not pila_operadores.is_empty():                  # Agrega los elementos faltantes
     postfijo += pila_operadores.pop()


print("\nPila de operadores: ")
pila_operadores.mostrar()
print("Pila de operando: ")
pila_operando.mostrar()
print(f'Postfijo: {postfijo} = {resultado}')



