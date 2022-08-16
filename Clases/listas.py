# Iñigo Quintana Delgadillo

# Ejemplo con listas

# 02/06/2022

alumnos = list()


# alumnos.append('Ana Sofia')
# alumnos.append('Manuel')
# alumnos.append('Stevanato')
# alumnos.append('Iñigo')

a = '' 
"""
Variable en la que recibira los `nombres` para la lista
"""

op = ''

# Agrega nombres hasta que el usuario lo deseé
while op != 2:
     print('\nMENU\nIngresa 1 para añadir\nIngresa 2 para salir')
     op = input(':')
     
     if op == '1':
          a = input("\nIngrese el nombre del alumno:")
          alumnos.append(a)

# Imprime la lista
for alumno in alumnos:
     print(alumno)


"""

Crea una aplicación que permita añadir alumnos a un diccionario
Nota: Es similar a este ejemplo

"""


