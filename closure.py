
def saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao} {nome}!'
    return saudar


s1 = saudacao('Bom dia!', 'Wagner')
s2 = saudacao('Boa noite!', 'Wagner')

print(s1)
print(s2())  # também posso fazer para passar os parametros aqui, basta na função saudar ele usar um parametro como o nome...
