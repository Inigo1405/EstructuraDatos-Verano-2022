# Iñigo Quintana Delgadillo

# Continua el programa de fibonacci recursivo, 
# donde ahora imprima la secuencia de 0 hasta n

# 26/06/2022


def fibonacci(x):
     if x == 0:
          return 0

     if x == 1:
          return 1

     else:
          return fibonacci(x-1) + fibonacci(x-2)


n = 7
print(f'Fibonacci de {n} es: {fibonacci(n)}') 

for i in range(n+1):
     print(fibonacci(i), end=', ')
