
x = float(input(f'Digite um valor: '))

y = (x)**(1/2)

if y % 1 == 0:
    print(f'A raiz é um número inteiro igual a {y} ')

else:
    print(f'A raiz {y:.2f} não é inteira')