class Pessoa:

    def __init__(self, nome, idade):
        self .nome = nome
        self .idade = idade

Pessoa = Pessoa('Luiza', 21)

class Pet(Pessoa):
    
    def __init__(self, nomePet, idadePet):
        self.nomePet = nomePet
        self.idadePet = idadePet

    def idadePet(self):
        nascimento = int(input(f'Digite a data de nascimento do seu Pet {self.Pet} nasceu: '))
        idade = 2019 - nascimento
        print(f" A {self.nome} é dona da {self.Pet} que tem {idade} aninhos.")


pet = Pet("Luiza", 20, "nina") 
pet.idadePet()
print(f" a (o) {pessoa.nome} tem  {pessoa.idade}")