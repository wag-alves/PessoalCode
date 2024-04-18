
num = int(input(f'Digite um número: '))
expo = int(input(f'Digite seu expoente: '))
cont = 1
x = num

while cont < expo:
    if num == 0:
        print(f'0 elevado a {expo} é 1.')
        break
    else:
        x = num * x     
        cont = cont + 1  

if cont > 1:
    print(f'O número {num} elevado a {expo} é igual a {x}')
    