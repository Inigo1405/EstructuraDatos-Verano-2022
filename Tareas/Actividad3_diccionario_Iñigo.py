# Iñigo Quintana Delgadillo
# Crea una aplicación que permita añadir alumnos a un diccionario.
# 02/06/2022

alumnos = dict()
"""
Diccionario que contiene los nombres de los alumnos con una llave, datos a ingresar: 
\n`Llave`
\n`Nombre`
"""

op = ''
while op != 2:
     print('\nMENU\nIngresa 1 para añadir\nIngresa 2 para salir')
     op = int(input(': '))
     
     if op == 1:
          llave = input('\nIngrese llave: ')
          nombre = input('Ingrese nombre: ')
          alumnos[llave] = nombre


print(alumnos)

