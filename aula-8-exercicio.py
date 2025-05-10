nome = str(input('Insira seu nome: ')).title()
altura = float(input('Insira sua altura (em m): '))
peso = float(input('Insira seu peso: '))

imc = peso / (altura**2)

print(f'{nome} tem {altura:.2f}m de altura\npesa {peso}kg e o seu IMC eh\n{imc:.2f}')