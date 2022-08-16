# Iñigo Quintana Delgadillo

# Funciones

# 03/06/2022

def saludar():
     """Función que mandara un saludo al ser llamada"""
     print('Hola')

def saludar_2(n, ap):
     print(f'Hola '+ n + ap)

def saludar_3(n, ap):
     texto = 'Hola ' + n + ap
     return texto;

def despedir(nombre):
     """
     Función que solicita `nombre` 
     para mandar una despedida al ser llamada
     """
     print(f'Adios {nombre}')


saludar()
despedir('Iñigo')

nombre = input('Ingresa tu nombre: ')
apellidos = input('Ingresa apellidos: ')

#saludar_2(nombre, apellidos)

t = saludar_3(nombre, apellidos)


