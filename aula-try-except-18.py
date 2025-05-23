numero_str = input('Digite um numero e receba o dobro do mesmo: ')

try:
    print(f'STR: {numero_str}')
    numero_float = float(numero_str)
    print(f'FLOAT: {numero_float}')
    print(f'O dobro de {numero_str} eh {numero_float*2}')
except:
    print('Isso nao eh um numero!')