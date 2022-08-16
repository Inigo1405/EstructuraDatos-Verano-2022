from colas import Cola
from clases import Alumno


cola = Cola()
alumno = Alumno()

print(cola.is_empty())

cola.enqueue(3)
cola.enqueue(5)
cola.enqueue(8)
cola.enqueue(2)

cola.display()

cola.dequeue()

cola.display()

alumno.saludar('Iñigo')



