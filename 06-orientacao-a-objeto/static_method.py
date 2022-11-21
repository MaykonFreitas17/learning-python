class Pessoa:
  def __init__(self, nome):
    self.nome = nome

  # metodo de instancia
  def method_instancie(self):
    print('metodo de instancia', self)

  # metodo de class
  @classmethod
  def method_class(cls):
    print('metodo de class', cls)
  
  # metodo estatico
  @staticmethod
  def method_static():
    print('Metodo Estatico')

p1 = Pessoa("Maykon Freitas")

p1.method_instancie()
p1.method_class()
p1.method_static()