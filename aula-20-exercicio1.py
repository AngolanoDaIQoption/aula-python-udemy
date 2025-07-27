num = input("digite um numero inteiro: ")

try:
    num_int = int(num)
    if num_int % 2 == 0:
        print(f'{num_int} eh par!')
    else:
        print(f'{num_int} eh impar!')
except ValueError:
    print(f"{num} nao eh um numero inteiro!")