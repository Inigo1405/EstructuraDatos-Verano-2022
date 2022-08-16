# Iñigo Quintana Delgadillo
# Imprime los números multiplos de 3 desdes el 0 al 100
# 01/06/2022

for i in range(0, 100):
     multiplo = i % 3
     if multiplo == 0:
          print(i)
          