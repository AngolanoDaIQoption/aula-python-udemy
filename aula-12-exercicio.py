primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite um valor: ')

if primeiro_valor>segundo_valor:
    print(f'{primeiro_valor=} eh maior que {segundo_valor=}')
elif primeiro_valor == segundo_valor:
    print(f'{primeiro_valor=} eh igual ao {segundo_valor=}')
else:
    print(f'{segundo_valor=} eh maior que {primeiro_valor=}')