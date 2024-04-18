
#Faça um programa que solicite ao usuário um valor inteiro positivo e exiba os números primos de 1 até o valor informado.
'''
x = int(input(f'Digite um número: '))
contar = 0
while contar >= x:
    if contar % 1 == 0 and contar / contar == 1:
        print(f'{contar} é um número primo.')
    contar += 1

print(f'fim')'''

x = int(input(f'Digite um número: '))
con = 1
y = 1
while con <= x:
    if con == 2 or con == 3 or con == 5 or con == 7 or con == 11:
        print(f'{con} é um número primo')
        
    if con % 2 == 0 or con % 3 == 0 or con % 5 == 0 or con % 7 == 0 or con == 1 or con % 11 and con % con ==0:
        ...
    else:
        print(f'é um {con} número primo')

    con = con + 1
print(f'Você é muito foda')

'''
13 * 13 == 169
con * con != int
con ** 2 == (con ** 2) ** (1/2)'''
'''
num2 = int(input('Digite um valor inteiro: '))
cont = 1
while cont <= num2:
    num = cont
    if num > 1:    
        i = 2
        while i < num: 
            if num % i == 0:
                break
            i += 1
        else:
            print(f'{num} É PRIMO')
    cont += 1
'''