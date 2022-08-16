# Iñigo Quintana Delgadillo

# Clase para método burbuja

# 06/06/2022



class Alumno:
     """
     Requiere de un nombre para mandarle un saludo
     """
     def __init__(self, nombre):           # Constructor: método especial que es llamada siempre que se instancia
          self.nombre = nombre
          

     def saludar(self):                    # self : significa que esta función solo funciona por medio de Alumno
          print(f"Hola {self.nombre}")


# Se comenta porque si no aparece 
# en los códigos donde se imporatn

# alumno = Alumno('Iñigo')
# print(alumno)

# alumno.saludar()
# print(alumno.nombre)





