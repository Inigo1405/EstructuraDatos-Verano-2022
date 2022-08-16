# Iñigo Quintana Delgadillo



# Factorial iterativo

def factorial(x):
     fact = 1
     for i in range(1, x+1):
          fact = fact * i
     return fact

# n = -5
# res = factorial(n)
# print(f'El factorial de {n} es {res}')



# Factorial recursiva
def factorial_recursivo(x):
     # Caso base
     if x == 1:
          return 1
     # Caso general
     else:
          return (x * factorial_recursivo(x-1))

# Optimizado --> Ternarios
def factorial_recursivo_mini(x):
     return 1 if x == 1 else (x * factorial_recursivo(x-1))

n = 5
print(f'El factorial de {n} es {factorial_recursivo_mini(n)}')          