num_1 = input('Insira um numero: ')
num_2 = input('Insira outro numero: ')

while True:
    float_num_1 = float(num_1)
    float_num_2 = float(num_2)
    print('Escolha uma opcao abaixo')
    print('1 - adicao\n2 - subtracao\n3 - multiplicacao\n4 - divisao')
    escolha = input('Insira sua opcao: ')
    try:
        if escolha == '1':
            print(f'A soma entre {float_num_1} e {float_num_2} eh de {float_num_1+float_num_2}')
        elif escolha == '2':
            print(f'A subtracao de {float_num_1} - {float_num_2} eh de {float_num_1-float_num_2}')
        elif escolha == '3':
            print(f'A multiplicacao de {float_num_1} e {float_num_2} eh {float_num_1*float_num_2}')
        elif escolha == '4':
            print(f'A divisao entre {float_num_1} e {float_num_2} eh {float_num_1/float_num_2}')
        else:
            print('Escolha uma operacao valida!')
            continue

        escolha2 = input('Deseja fazer outra operacao? s/n: ')
        try:
            if escolha2 == 's':
                num_1 = input('Insira um numero: ')
                num_2 = input('Insira outro numero: ')
                continue
            elif escolha2 == 'n':
                print('Voce escolheu nao continuar!')
                break
            else:
                print('Escolha uma opcao valida!!')
                continue

        except Exception as erro:
            print(f'Ocorreu um erro inesperado: {erro}')

    except Exception as e:
        print(f'Erro inesperado: {e}')


