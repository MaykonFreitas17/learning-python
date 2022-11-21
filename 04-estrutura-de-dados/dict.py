# Dicts ou Dicionários (Objetos em outras linguagens)

# Sintaxe => nome_dict = { key: valor, key2: valor2 }
notas = {
  "maykon": [10, 10, 10, 10],
  "bruno": [8, 8, 8, 8],
}

# Acessando os valores do dicionário
print(notas["maykon"])
print(notas["bruno"])

# Dicionários com chaves númericos(inteiros)
weekdays = {
  1: "Domingo",
  2: "Segunda-Feira",
  3: "Terça-Feira",
}

print(weekdays[1], weekdays[2], weekdays[3])

# Pegando todas as chaves do objeto - .keys()
print(notas.keys())

# Pegando todos os valores dos objetos - .values()
print(notas.values())

# Pegando todos os conjuntos key-value - .items()
print(notas.items())