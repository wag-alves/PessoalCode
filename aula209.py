class Pessoa:
    ano = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def metodo_normal(self):
        print("Hey")

    @classmethod
    def metodo_de_classe(cls):
        print("Metodo de classe!")

    @classmethod
    def sem_nome(cls, idade):
        return cls("Anônimo", idade)

    @classmethod
    def sem_idade(cls, nome):
        return cls(nome, "idade desconhecida", Pessoa.ano)


p1 = Pessoa("wagner", 28)
p1.metodo_normal()
print(Pessoa.ano)  # Se eu quiser chamar desse modo eu tenho quer fazer o class method
Pessoa.metodo_de_classe()  # Viu?? Passei da mesma forma do atributo nome
p2 = Pessoa.sem_nome(28)
print(p2)
print(p2.nome, p2.idade)
p3 = Pessoa.sem_idade('Larissa')
print(p3)
print(p3.nome, p3.idade, p3.ano)
