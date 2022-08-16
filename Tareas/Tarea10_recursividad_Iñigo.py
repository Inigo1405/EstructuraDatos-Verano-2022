# Iñigo Quintana Delgadillo

# Desarrolla la función fibonacci en Python.
# Nota: En formato iterativo

# 23/06/2022

def fibonacci(x, y):
     z = x + y
     print(z)
     if z <= 10000:
          fibonacci(y , z)

print('0')
print('1')
fibonacci(0, 1) 



