
#Fazer um programa que solicite ao usuário um valor inteiro positivo e gere o seu valor em binário. ATENÇÃO: Deverá ser utilizada divisões inteiras para a solução.

y = int(input(f'Digite um número positivo para ver seu correspondente em binário: '))
if y % 1 == 0:
    while y % 1 == 0:
        if y % 2 != 0 or y % 2 != 1:
            x = y
    
print(f'O resto da divisao é {x}')
    