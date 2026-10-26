class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def bonus(self):
        return self.salario * 0.10
class Diretor(Funcionario):
    def bonus(self):
        return self.salario * 0.30
diretor = Diretor("Roberto", 10000.00)
print("Nome:", diretor.nome)
print(f"Bônus: R$ {diretor.bonus():.2f}")