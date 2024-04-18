x = input(f'Digite seu ano de nascimento: ')
y = x.split('/')
mes = int(y[1])
meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
print(f'{y[0]} de {meses[mes - 1]} de {y[2]}')
