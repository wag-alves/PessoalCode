
def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('Wagner')
adiciona_clientes('Larissa', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Isis')  # assim tá passando ainda para a mesma lista cliente 1
print(cliente2)

# Assim é melhor porque ele faz uma lista nova direto


def adiciona(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


c1 = adiciona('José')
adiciona('Lara', c1)
print(c1)

c2 = adiciona('Fulano')
adiciona('Cicrano', c2)
c2.append('Beltrano')
print(c2)
