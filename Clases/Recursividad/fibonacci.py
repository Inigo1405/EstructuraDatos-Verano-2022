# Iñigo Quintana Delgadillo

# Desarrolla la función fibonacci en Python.
# Nota: En formato iterativo

# 23/06/2022


# def fibonacci(x, y):
#      z = x + y
#      print(z)
#      if z <= 10000:
#           fibonacci(y , z) 

# print('0')
# print('1')
# fibonacci(0, 1)           


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
