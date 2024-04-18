

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

contador = 11

for item in lista:
    contador -= 1
    x = contador * item
    print(f'{contador}x{contador-item}={x}')
