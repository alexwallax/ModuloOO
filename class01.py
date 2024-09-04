class Pessoa:
    def __init__(self, nome, sobreNome):
        self.nome = nome
        self.sobreNome = sobreNome

p1 = Pessoa("Alex", "Wallace")

p2 = Pessoa("João", "Araujo")

print(p1.nome, p1.sobreNome)
print(p2.nome)
print(p2.sobreNome)