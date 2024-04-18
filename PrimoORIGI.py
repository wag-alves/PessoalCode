

x = int(input(f'Digite um numero: '))
num = x - 1
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
    print(f'O número é primo')
