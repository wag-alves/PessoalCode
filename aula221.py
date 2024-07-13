class MinhaString(str):  # Se o método tem o mesmo nome ele é sobreposto...
    def upper(self):  # Por estar usando herança do str e utilizando o upper, eu acabo sobrescrevendo ele, então eu preciso usar o super para pegar o upper original de novo...
        print("Meu Upper")
        contexto = super().upper()
        # contexto = super(MinhaString, self).upper() ISSO É A MESMA COISA DO CÓDIGO ACIMA...
        print("Mexendo mais um pouco...")
        return contexto


string = MinhaString("wagner")
print(string.upper())
