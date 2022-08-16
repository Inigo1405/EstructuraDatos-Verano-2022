# Iñigo Quintana Delgadillo

# Ingresa 5 datos enteros en un arreglo y otros 7 en otro arreglo,
# los datos se ingresan ya ordenados de menor a mayor. Genera un
# tercer array de 12 elementos ordenados, uniendo los 2 anteriores arreglos.

# 03/06/2022


def ordenarArray(arrayFinal):                          # Se define una función llamada Array
     """
     Esta función que ordena de manera ascendente los 
     datos del arreglo que se ingrese.
     """

     n = len(arrayFinal)

     for i in range(n-1):
          for j in range(n-1):
               if arrayFinal[j] > arrayFinal[j+1]:
                    burbuja = arrayFinal[j]
                    arrayFinal[j] = arrayFinal[j+1]
                    arrayFinal[j+1] = burbuja

     print('\nArreglo final: ', arrayFinal)            # Imprime el arreglo ya ordenado 


array = []
array_2 = []
arrayFinal = []

# --- Main ---
print('Ingresa los datos del primer arreglo: ')
for i in range(5):
     array.append(int(input(': ')))                    # Agrega el dato ingresado a un arreglo
     arrayFinal.append(array[i])                  
print(array)                                           # Imprime el primer arreglo


print('\nIngresa los datos del segundo arreglo: ')
for i in range(7):
     array_2.append(int(input(': '))) 
     arrayFinal.append(array_2[i])
print(array_2)                                         # Imprime el segundo arreglo


ordenarArray(arrayFinal)

# print('\nArreglo final: ', arrayFinal)
