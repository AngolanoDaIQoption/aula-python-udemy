idade = input('Digite sua idade: ')

int_idade = int(idade)

if int_idade>18:
    print('Voce eh de maior!')
elif int_idade==18:
    print('Voce ja eh de maior, mas no limite!')
else:
    print('Voce ainda eh de menor, aproveite a vida!')