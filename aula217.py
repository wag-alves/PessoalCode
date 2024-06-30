class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        # Por estar sendo criado aqui, quando eu apagar o cliente o endereço vai junto...
        # Python não sabe como representar uma classe, por isso o __dict__
        self.enderecos.append(Endereco(rua, numero))

    ##### ISSO É UMA ALTERNATIVA PARA NÃO USAR __DICT__ #####
    # OBS: Só esta comentado por causa do dict, ou seja, ou um ou outro
    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    # Para conferir se o cliente está relacionado ao endereço, eu posso usar esse seguinte método
    def __del__(self):
        print("Apagando, ", self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print("Apagando, ", self.rua, self.numero)


cliente1 = Cliente("Wagner")
cliente1.inserir_endereco("Av Laranjeiras", 1008)
cliente1.inserir_endereco("Av Brasil", 3008)

print(cliente1)
print()
print(cliente1.__dict__)
print()
print(cliente1.enderecos)
print()
print(vars(cliente1))


# cliente1.listar_enderecos()
