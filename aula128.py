import json

CAMINHO_ARQUIVO = 'aula128.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Wagner', 28)
p2 = Pessoa('Larissa', 26)
p3 = Pessoa('Dayse', 64)
# bd = [p1, p2, p3] Se eu tentar salvar assim não vai dar certo, pois o json não entende como salvar isso
bd = [vars(p1), p2.__dict__, vars(p3)]  # Agora dá certo

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii='false', indent=2)
