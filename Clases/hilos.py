# Programación en paralelo

import threading

def contador():
     for i in range(5):
          print(f'Hilo {threading.current_thread()}: {i}')

hilo1 = threading.Thread(target=contador)
hilo2 = threading.Thread(target=contador)

# hilo1.start()
# hilo2.start()

print("Hola desde el principal")


