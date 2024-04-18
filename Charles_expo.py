

num = int(input(f'Digite um número: '))
expo = int(input(f'Digite seu expoente: '))
cont = 1
x = num

while cont < expo:
    x = num * x       
    cont = cont + 1
print(x)