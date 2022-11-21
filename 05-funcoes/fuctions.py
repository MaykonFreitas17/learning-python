"""
  Sintaxe:
  def nome_função():
    código
"""
# Criando uma função que imprime uma mensagem
def greetings():
  print('Good Morning!')

greetings() # Chamando a função para que ela seja executada

# Criando uma função com parametros
def greetings_with_name(name):
  print(f'Good Morning, {name}!')

greetings_with_name("Maykon Freitas") # Chamando a função para que ela seja executada
greetings_with_name(name="Bruno Sousa") # Chamando a função e nomeando o parametro

# Definindo uma função vázia
def soma(number1, number2):
  ...

soma(10, 10) # Ao chamar a função sum, não vai acontecer não, pois a função está vazia

# Retornando valores com funções
def calcular_conta(consumo, taxa_servico, desconto):
  if taxa_servico == 0 and desconto == 0:
    return consumo

  servico = consumo * taxa_servico
  desconto = consumo * desconto
  valor = consumo + servico
  total_pagar = valor - desconto

  return total_pagar # Retornando o valor total_pagar

total_pagar = calcular_conta(consumo=100, taxa_servico=0.15, desconto=0.1)
print(total_pagar)

total_pagar = calcular_conta(100, 0, 0)
print(total_pagar) # teste passando a taxa_servico e desconto como 0

# Criando funções com valores de parametros padrões
def calcular_conta_padrao(consumo, taxa_servico, desconto=0):
  if taxa_servico == 0 and desconto == 0:
    return consumo

  servico = consumo * taxa_servico
  desconto = consumo * desconto
  valor = consumo + servico
  total_pagar = valor - desconto

  return total_pagar # Retornando o valor total_pagar

total_pagar = calcular_conta_padrao(consumo=100, taxa_servico=0)
print(total_pagar)