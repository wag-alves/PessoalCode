class A:
    atributo_a = "A"

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print("A")


class B(A):
    atributo_b = "B"

    def __init__(self, atributo, mais_uma_coisa):  # Se eu não fizer assim vou acabar sobrecrevendo o __init__ de A
        super().__init__(atributo)  # Consequentemente perco o __init__ de A...
        self.mais_uma_coisa = mais_uma_coisa

    def metodo(self):
        print("B")


class C(B):
    atributo_c = "C"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Burlei papai")

    def metodo(self):
        super(C, self).metodo()  # Aqui estou olhando para C e procurando o método no seu "Superior" que é B
        # super().metodo() Isso é a mesma coisa do código de cima, a diferença é que o outro é explicito isso...
        super(B, self).metodo()  # Aqui estou olhando para B e procurando o método no seu "Superior" que é A
        print("C")


c = C("Se eu não botar nada aqui dá erro, pois o C herda o __init__ de A", "Esse aqui é o __init__ de B")
print(c.atributo)
print(c.mais_uma_coisa)
print(c.atributo_a)  # Herdou foi tudo...
print(c.atributo_b)
print(c.atributo_c)
c.metodo()
print(C.__mro__)
print(C.mro())  # O nome disso é Method resolution order
print(help(C))  # Tá tudo escrito aqui...
