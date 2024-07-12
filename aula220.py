class Pessoa():
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

### HERANÇA ###


class Cliente(Pessoa):
    ...

### HERANÇA ###


class Aluno(Cliente):
    pass


c1 = Cliente('Wagner', 'Alves')
c1.nome_classe()
a1 = Aluno('Larissa', 'Deborah')
a1.nome_classe()
help(a1)
