nome = input('Insira seu nome: ').title()
idade = input('Insira sua idade: ')
if idade:
    int_idade = int(idade)

if nome and idade:
    print(f'Seu nome eh {nome}')
    print(f'Voce tem {int_idade} anos')
    print(f'Seu nome invertido eh {nome[::-1]}')#fatiamento de strings
    if " " in nome:
        print("Seu nome contem espacos!")
        print(f'Seu nome tem {len(nome)-1} letras!')
    elif " " not in nome:
        print('Seu nome nao contem espacos!')
        print(f'Seu nome tem {len(nome)} letras!')
    print(f'A primeira letra do seu nome eh {nome[0]}')
    print(f'A ultima letra do seu nome eh {nome[-1]}')
else:
    print('Desculpe, voce deixou campos vazios.')
