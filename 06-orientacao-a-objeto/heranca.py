class Pessoa:
  def __init__(self, nome, idade, cpf):
    self.nome = nome
    self.idade = idade
    self.cpf = cpf
  
  def show_informations(self):
    print('==========Infors==========')
    print(f'nome: {self.nome}')
    print(f'idade: {self.idade}')
    print(f'cpf: {self.cpf}')
    print('==========================')

# a classe Estudante está herdando todos os atributos e metodos da classe Pai (Pessoa)
class Estudante(Pessoa):
  # Sobrescrevendo o metodo construtor do pai
  def __init__(self, nome, idade, cpf, curso):
    super().__init__(nome, idade, cpf)
    self.curso = curso

  def show_informations(self):
    print('==========Infors==========')
    print(f'nome: {self.nome}')
    print(f'idade: {self.idade}')
    print(f'cpf: {self.cpf}')
    print(f'curso: {self.curso}')
    print('==========================')
  
  def get_study(self):
    return {
      "id": 1,
      "nome": self.nome,
      "idade": self.idade,
      "cpf": self.cpf,
      "curso": self.curso
    }

p1 = Pessoa('Maykon Freitas', 20, "000.000.000-00")
p1.show_informations()

e1 = Estudante('Bruno Sousa', 18, "000.000.000-00", "Ciência da Computação")
e1.show_informations()