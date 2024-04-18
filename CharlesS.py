
from bdb import GENERATOR_AND_COROUTINE_FLAGS
from mailbox import NotEmptyError

'''
valor = int(input(f'Digite um valor: '))
multiplicador = 0

while multiplicador <=10:
    print(f'{multiplicador} x {valor} = {multiplicador * valor}')
    multiplicador += 1
print('Acabou-se')
'''

#Questão_01.py


while True:
    nota_1 = int(input(f'Informe a nota de etapa 1'))
    nota_2 = int(input(f'Informe a nota de etapa 2'))
    media = ((nota_1 * 2) + (nota_2 * 3)) / 5
    print(f'A média foi {media}')
    continuar = input(f'Deseja continuar (S/N)')
    if continuar == 's' or continuar == 'S':
        break

print('fim do programa')
