"""
  Sintaxe:
  class NomeClass:
    ...
"""

# Definindo uma class Evento
class Evento:
  # criando um metodo
  def set_name(self, name):
    self.nome = name # self faz referencia a propria instancia

# Instanciando uma class - criando um objeto Evento
evento = Evento() # Criando uma instancia da classe Evento

# Criando um atributo dinamicamente
evento.nome = "Aula de Python"
print(evento.nome)

# utilizando o metodo set_name
evento02 = Evento()
evento02.set_name("Aula de Orientação a Objeto em Python")
print(evento02.nome)