import unittest

from app import somar, subtrair, multiplicar, dividir

# Classe para testar a função somar
class TestSomar(unittest.TestCase):
  def test_soma_de_dois_numeros(self):
    self.assertEqual(somar(1, 1), 2)
  
  def test_soma_de_numero_com_zero(self):
    self.assertEqual(somar(1, 0), 1)

# Classe para testar a função subtrair
class TestSubtrair(unittest.TestCase):
  def test_subtracao_de_dois_numeros(self):
    self.assertEqual(subtrair(1, 1), 0)
  
  def test_subtracao_de_numero_com_zero(self):
    self.assertEqual(somar(1, 0), 1)

# Classe para testar a função multiplicar
class TestMultiplicar(unittest.TestCase):
  def test_multiplicacao_de_dois_numeros(self):
    self.assertEqual(multiplicar(1, 1), 1)
  
  def test_multiplicacao_de_numero_com_zero(self):
    self.assertEqual(multiplicar(1, 0), 0)

# Classe para testar a função dividir
class TestSubtrair(unittest.TestCase):
  def test_divisao_de_dois_numeros(self):
    self.assertEqual(dividir(1, 1), 1)
  
  # def test_dividir_de_numero_com_zero(self):
  #   self.assertEqual(dividir(1, 0), 1)

unittest.main()