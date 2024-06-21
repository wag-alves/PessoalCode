class Foo:
    def __init__(self):
        self.public = 'Isso é public'
        self._protected = 'Isso é protected'
        self.__private = 'Isso é private'  # Nem dá para usar fora da classe, somente dentro dela

    def public_method(self):
        print(self.__private)             # Só consigo usar aqui... como deve ser...
        return 'public_method'

    def _protected_method(self):      # É bom usar somente na classe ou em suas subclasses...
        return '_protected_method'

    def __private_method(self):       # O nome disso em python é name mangling
        return '__private_method'


f = Foo()
print(f.public)
print(f._Foo__private_method())
print(f._Foo__private)        # Só consigo usar assim, mas NÃO É PARA USAR!!!!!!!!!!!!!!
print(f._protected)           # NÃO É PARA USAR ISSO!!!!!!!!!!!!!!!!!!!!
print(f.public_method())
print(f._protected_method())  # NÃO É PARA USAR ISSO!!!!!!!!!!!!!!!!!!!!
# OBS.: É para usar o método protected dentro da instância como atributo ou dentro de um método
