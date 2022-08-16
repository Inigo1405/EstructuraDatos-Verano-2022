# Iñigo Quintana Delgadillo

# Ejemplo con Diccionarios

# 02/06/2022

"""

dic = {'llave': 5}
dic['otra'] = 6
dic[40] = 'aqui estoy'

print(dic[40])
print(dic)

"""

alumnos = {
     '195141': {'nombre': 'Diego', 'apellidos': 'Pacheco Valdez', 'asistencia': True},
     '187397': {'nombre': 'Iñigo', 'apellidos': 'Quintana Delgadillo', 'asistencia': True},
     '195201': {'nombre': 'Erick', 'apellidos': 'Guevara Morales', 'asistencia': True},
}

alumnos['187397']['asistencia'] = False

# print(alumnos['187397']['nombre'])
print(alumnos)
print(alumnos['187397'])


