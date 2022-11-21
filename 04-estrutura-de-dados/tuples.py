# Estrutura de duplas -> nome_da_tupla = (valor1, valor2, valorN)
# Estrutura de duplas Alternativa -> nome_da_tupla = valor1, valor2, valorN

pessoa1 = ("Maykon", 20, 1.65, 60)
pessoa2 = "Maykon", 20, 1.65, 60,

# pegando valores pelo os index
print(pessoa1[0]) # Pegando o primeiro valor da tupla

# Desempacotamento de Tuplas
name, idade, altura, massa = pessoa1
print(name) # A variavel nome foi usada para receber o primeiro valor da tupla - Maykon
print(idade) # A variavel idade foi usada para receber o segundo valor da tupla - 20
print(altura) # A variavel altura foi usada para receber o terceiro valor da tupla - 1.65
print(massa) # A variavel massa foi usada para receber o ultimo valor da tupla - 60

"""
  Uma diferença de tuplas para listas, é que normalmente, tuplas são usadas com valores de tipos
  diferentes;

  exemplo:
  pessoa = ("Maykon", 20, 1.65, 60)

  Outra diferença entre Tuplas e Listas, é que Tuplas não aceitam atribuições,
  logo, você não poderar alterar os valores já existentes na Tupla.

  exemplo:
  pessoa = ("Maykon", 20, 1.65, 60)
  pessoa[0] = "Fernando"

  Ao rodar o código acima, vai da error, pois as tuplas não podem ser alteradas,
  elas são imudaveis.
"""