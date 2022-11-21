name_list = ["Maykon", "Ryan", "Freitas"] # Uma list feita em python

# For com uma lista
for name in name_list:
  print(name)

# For com uma String
for str in "String":
  print(str)

# For com a função Range -> range([start], stop[, step])
list_with_range = list(range(0, 10, 2)) # Lembrando que o range vai de 0 até 9 - 10 não é incluso, e como o step é de 2, então ele vai pular sempre de 2 em 2 números
print(list_with_range)
for number in range(0, 100):
  # Imprimindo uma sequencia númerica de 1 a 100
  print(number + 1)