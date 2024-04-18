n1 = float(input(f'qual é a sua primeira nota:'))
n2 = float(input(f'Qual é a sua segunda nota:'))
s = ((n1*2)+(n2*3))/5
aula = int(input(f'Quantas aulas você teve?'))
falta = int(input(f'Quantas vezes você faltou, em??'))
fr = 100-((falta*100)/aula)

print(f'Sua média ficou sendo, {s}')
print(f'Sua frequência é de, {fr:.2f}%')