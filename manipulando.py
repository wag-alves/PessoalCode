import json

caminho = 'manipulando.txt'  # Também posso passar o caminho completo

nomes = ['Wagner', 'Larissa']


# Super obs.: o encoding serve para o computador entender os tipos de caracteres, como no nome Atenção!
with open(caminho, 'w+', encoding='utf-8') as arquivo:  # O 'w' apaga tudo e escreve as coisas, o 'a' ele dá um append no final, sem apagar
    print(type(arquivo))
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0)  # O arquivo desce as linhas e para lá embaixo, isso serve para voltar ao começo do arquivo
    print(arquivo.read())
    print('ReadLines')
    arquivo.seek(0, 0)
    for linha in arquivo:
        print(linha.strip())  # Precisa desse strip pois se não ele vai mostrar as quebras de linha tbm, ou posso botar o separador end=''

with open(caminho, 'r+', encoding='utf8') as arquivo:
    print(arquivo.readlines())
