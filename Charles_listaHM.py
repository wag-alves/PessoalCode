'''
h = m = 1
con = 1
while con <= 5:
    idade = int(input(f'Quantos anos você tem? '))
    sexo = (input(f'Se você for homem digite H, se você for mulher digite M. '))
    if sexo == 'h' or sexo =='H':
        h = sexo + 1
        x = idade / sexo

    m = sexo + 1
    y = idade / sexo
    total = idade / sexo
    con = con + 1
print(f'{x} {y} {total}')'''

#Faça um programa que leia a idade de 5 pessoas e o sexo de cada uma (assuma que só podem ser informados a letra H para homes e a letra M para mulheres) e que calcule e mostre: a. A idade média das 5 pessoas; b. A idade média dos homens; c. A idade média das mulheres.

contador = 1

while contador <=5:
    idade = int(input(f'Digite a sua idade: '))
    sexo = (input(f'Digite o seu sexo: '))
    if sexo == 'H' or sexo == 'h':
        sexo = int(0)
        sexo = sexo + 1
        print(f'Você é homem {sexo}')
    elif sexo == 'm' or sexo =='M':
        sexo = 0
        sexo = sexo + 1
        print(f'Você é mulher {sexo}')
    contador = contador + 1
print(f'{idade/contador}')



'''
qwertyuiop
asdfghjklç
zxcvbnm,.;/~e]é[1
1234567890-='   KAKSDKFGGGUghgjJfdvb 