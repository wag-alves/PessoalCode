import json

pessoa = {
    'nome': 'Wagner',
    'sobrenome': 'Alves',
    'endereco': [
        {'rua': 'juvino', 'numero': 123},
        {'rua': 'subindo', 'numero': 456},
    ],
    'altura': 1.93,
    'numeros_preferidos': (3, 7, 13),
    'dev': True,
    'nada': None,
}

# Assim eu escrevo
with open('PessoalCode/aula117.json', 'w') as arquivo:
    json.dump(pessoa, arquivo, indent=2)

# Assim eu leio um arquivo
with open('aula117.json', 'r') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))
