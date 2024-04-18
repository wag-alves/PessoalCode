


num1 = int(input('Digite o valor'))
print('Os numeros primos serão exibidos abaixo: ')

currentNum = num1
cont = 2

while cont < num1:
    currentNum -= 1
    cache = 0
    cont2 = 1
    while cont2 < currentNum + 1:
        if currentNum % cont2 == 0:
            cache += 1
        cont2 += 1
    if cache > 2:
        ...
    else:
        print(f'{currentNum}')
    cont += 1