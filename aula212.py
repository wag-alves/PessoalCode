class Caneta:
    def __init__(self, cor):
        self._cor = cor    # Com um underline eu estou dizendo "NÃO USE ISSO FORA DA CLASSE!!!"

    @property                    # Aqui é um método
    def cor(self):
        print('Property')
        return self._cor

    @cor.setter
    def cor(self, valor):
        if valor == 'Rosa':   # O bom do setter é isso, para eu restringir algumas coisas...
            # Aqui estou levantando um erro para não usar essa cor, para erros mais genéricos eu poderia usar Exception
            raise ValueError("Não aceito essa cor!")
        print("Agora estou no setter", valor)
        self._cor = valor


caneta = Caneta('azul')
print(caneta._cor)            # Não é legal ficar usando isso...
print(caneta.cor)             # Aqui é um atributo, ou seja, o método se comporta como atributo por causa do property que é o modo pythonico do get
caneta.cor = "Roxo"
print(caneta._cor)            # Não é legal ficar usando isso...
print(caneta.cor)             # Aqui é o property
