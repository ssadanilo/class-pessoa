# Crie um classe chamada pessoa com os atributos: nome, idade, peso, gênero

class Pessoa:
    def __init__(self, nome, idade, peso, genero):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero


# Uso da classe Pessoa
pessoa1 = Pessoa('Jão Grilo', 33, 60, 'Masculino')
print('Nome', pessoa1.nome)
print('Idade', pessoa1.idade)
print('Peso', pessoa1.peso)
print('Gênero', pessoa1.genero)
