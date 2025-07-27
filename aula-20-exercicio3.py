nome_usuario = input('Insira seu nome: ').title()
nome_partes = nome_usuario.split()
nome = nome_partes[0]
sobrenome = " ".join(nome_partes[1:])
nome_junto = nome_usuario.replace(' ', '')

try:
    if not nome_junto.isalpha():
        raise ValueError

    if len(nome)<= 4:
        print(f'{nome_usuario}, seu primeiro nome eh curto!')
    if len(nome) > 4 and len(nome) <= 6:
        print(f'{nome_usuario}, seu primeiro nome tem um tamanho normal!')
    if len(nome) > 6:
        print(f'{nome_usuario}, seu primeiro nome eh muito grande!')

except ValueError:
    print('Pedi para digitar seu nome, nao numeros, voce eh um robo por acaso?')
