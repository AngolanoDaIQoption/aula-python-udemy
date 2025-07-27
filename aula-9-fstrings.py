#:.xf -->formata os numeros que vem depois do ponto, sendo x o numero de casas decimais que voce quer.

a = 'abc'
b = '6969'
c = 1.24

string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)
print(formato)