# Iñigo Quintana Delgadillo

# Clase para método burbuja

# 06/06/2022

import random

lista = [5,3,8,6,15,1,4]


def mostrar_lista(lista):
     print(lista)


def burbuja(lista):
     n = len(lista)
     # Método de la burbuja: 
     for i in range(n-1):
          for j in range(n-1):
               if lista[j] > lista[j+1]:               # Usa j por ser el for interno que va a comparar
                    tmp = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = tmp
     return lista


def generar_lista(x):
     lista_random = random.sample(range(100), x)       # Genera una lista con números aleatorios de 0 al rango indicado (100) guardando x cantidad
     return lista_random

# mostrar_lista(lista)
# mostrar_lista(burbuja(lista))

mostrar_lista(generar_lista(5))