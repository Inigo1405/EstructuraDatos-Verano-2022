# Herencias

class Poligono:                                   # Clase papá
     """
     Class Poligono
     --------
     Hereda el constructor, recibiendo los datos
     * `base`
     * `altura`
     """
     def __init__(self, base, altura):            
          self.b = base
          self.h = altura


class Rectangulo(Poligono):
     def area(self):                              # Función
          return self.b * self.h


class Triangulo(Poligono):
     def area(self):
          return(self.b * self.h) / 2



rectangulo = Rectangulo(5, 3)
t1 = Triangulo(12, 7)
print(f"El rectangulo de base {rectangulo.b} y altura {rectangulo.h} tiene un área de: {rectangulo.area()}")
print(f"El rectangulo de base {t1.b} y altura {t1.h} tiene un área de: {t1.area()}")






