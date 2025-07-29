import time
from time import sleep

contador = 0

while contador < 10:
    contador += 1
    time.sleep(0.3)
    print(contador)

print('Acabou!')