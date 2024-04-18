
x = int(input(f'Digite um numero: '))
y = x - 1   
contador = 1
num = x - 1

while contador <= y:
    resposta = 0

    while num > 1:

        if x % num != 0:
            ...
        else:
            resposta += 1
        num = num - 1

    if resposta > 0:
        ...
    else:
        print(f'O número {num} é primo')
    contador = contador + 1
    num = contador
    print(f'{num}')