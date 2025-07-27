import time
from time import sleep

hora = input('Insira a hora atual: ')
minutos = input('Agora insira os minutos: ')

try:
    hora_int = int(hora)
    minutos_int = int(minutos)
    if hora_int > 0 and hora_int <= 6:
        print(f'{hora_int}:{minutos_int} eh madrugada, va dormir!!')
    if hora_int > 6 and hora_int <= 11:
        print(f'{hora_int}:{minutos_int} eh dia! ou seja...')
        time.sleep(1)
        print('Bom dia campeao!!!')
    if hora_int > 11 and hora_int <= 17:
        print(f'{hora_int}:{minutos_int} esta a tarde! ou seja...')
        time.sleep(1)
        print('Boa tarde campeao!!!')
    if hora_int > 17 and hora_int <= 24:
        print(f'{hora_int}:{minutos_int} eh noite! ou seja...')
        time.sleep(1)
        print('Boa tarde campeao!!!')
    if hora_int >= 25:
        print('Isso nem horario eh!')
except ValueError:
    print('Era pra inserir a hora e os minutos, nao letras, BURRO!')