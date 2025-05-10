nome = input('Insira seu nome: ').capitalize()
sobrenome = input('Insira seu sobrenome: ').capitalize()
idade = int(input('Insira sua idade: '))
ano_nascimento = 2025-idade
if idade>=18:
    print('Voce eh maior de idade!')
else:
    print('Voce eh menor de idade')
altura_metros = int(input('Insira sua altura (em CM): '))
if len(str(altura_metros))==3:
    print(f'Sua altura eh {altura_metros/100:.2f}m')
else:
    print('Voce inseriu valores incorretos!')

print(f'Ola {nome} {sobrenome};\nde idade {idade} anos,\nvoce nasceu em {ano_nascimento}!')