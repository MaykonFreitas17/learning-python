class Pessoa:
  # criando um construtor => sintaxe = def __init__(self, atr1, atr2, atrN)
  def __init__(self, nome):
    # atribuindo o valor ao atributo nome
    self.nome = nome
    # criando um atributo com valor padrão
    self.local = "Brasil"

p1 = Pessoa("Maykon Freitas") # Instanciando um objeto Pessoa e passando o valor do atributo nome
print(p1.nome, p1.local) # Imprimindo o valor do atributo nome

p2 = Pessoa("Bruno Sousa")
print(p2.nome)